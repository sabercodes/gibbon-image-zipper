import os
import zipfile
import io
import urllib.request

import cv2
import numpy as np
from PIL import Image

# ── Target output dimensions ──────────────────────────────────────────────────
TARGET_W = 240
TARGET_H = 320
MAX_W    = 360
MAX_H    = 480
MIN_AR   = 1 / 1.4   # ~0.714  (width / height)
MAX_AR   = 1 / 1.2   # ~0.833

# ── Padding around the detected face (fraction of face size) ──────────────────
# e.g. 0.5 means add 50 % of the face height above/below the face box
FACE_PAD_TOP    = 0.8   # extra space above face (for hair / forehead)
FACE_PAD_BOTTOM = 0.3   # extra space below face (for chin / neck)
FACE_PAD_SIDES  = 0.4   # extra space left and right


# ── Haar Cascade loader ───────────────────────────────────────────────────────
def _get_cascade():
    """
    Return a cv2 face cascade. Tries the OpenCV built-in path first;
    if missing, downloads the XML from the official GitHub mirror.
    """
    # Built-in path bundled with opencv-python / opencv-python-headless
    builtin = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    if os.path.exists(builtin):
        return cv2.CascadeClassifier(builtin)

    # Fallback: download once to a temp file
    local = os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_default.xml")
    if not os.path.exists(local):
        print("Downloading Haar Cascade XML …")
        url = (
            "https://raw.githubusercontent.com/opencv/opencv/master/"
            "data/haarcascades/haarcascade_frontalface_default.xml"
        )
        urllib.request.urlretrieve(url, local)
    return cv2.CascadeClassifier(local)


FACE_CASCADE = _get_cascade()


# ── Face crop ─────────────────────────────────────────────────────────────────
def crop_face_region(pil_img):
    """
    Detect the largest face in pil_img and return a portrait crop centred on
    it with padding.  If no face is found, fall back to a centred crop that
    respects the required aspect ratio.

    Always returns a PIL Image ready for the next validation step.
    """
    img_w, img_h = pil_img.size

    # Convert to OpenCV BGR for the detector
    cv_img = cv2.cvtColor(np.array(pil_img.convert("RGB")), cv2.COLOR_RGB2BGR)
    gray   = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    if len(faces) == 0:
        # ── No face found: centre-crop to the required aspect ratio ──────────
        print("   No face detected — applying centre crop.")
        return _centre_crop(pil_img)

    # Pick the largest detected face
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])

    # Apply padding
    pad_top    = int(h * FACE_PAD_TOP)
    pad_bottom = int(h * FACE_PAD_BOTTOM)
    pad_sides  = int(w * FACE_PAD_SIDES)

    x1 = max(0, x - pad_sides)
    y1 = max(0, y - pad_top)
    x2 = min(img_w, x + w + pad_sides)
    y2 = min(img_h, y + h + pad_bottom)

    crop_w = x2 - x1
    crop_h = y2 - y1

    # Force the crop to the target aspect ratio (expand the shorter dimension)
    target_ar = TARGET_W / TARGET_H          # ~0.75
    actual_ar = crop_w / crop_h

    if actual_ar > target_ar:
        # Crop is too wide — increase height
        new_h  = int(crop_w / target_ar)
        delta  = new_h - crop_h
        y1     = max(0, y1 - delta // 2)
        y2     = min(img_h, y1 + new_h)
    else:
        # Crop is too tall — increase width
        new_w  = int(crop_h * target_ar)
        delta  = new_w - crop_w
        x1     = max(0, x1 - delta // 2)
        x2     = min(img_w, x1 + new_w)

    cropped = pil_img.crop((x1, y1, x2, y2))
    return cropped


def _centre_crop(pil_img):
    """Centre-crop the image to the target aspect ratio (fallback)."""
    img_w, img_h = pil_img.size
    target_ar    = TARGET_W / TARGET_H

    if img_w / img_h > target_ar:
        # Image is wider than needed — crop sides
        new_w = int(img_h * target_ar)
        left  = (img_w - new_w) // 2
        return pil_img.crop((left, 0, left + new_w, img_h))
    else:
        # Image is taller than needed — crop top/bottom (keep upper portion for face)
        new_h = int(img_w / target_ar)
        return pil_img.crop((0, 0, img_w, new_h))


# ── Main pipeline ─────────────────────────────────────────────────────────────
def validate_and_prepare_zip(input_folder, output_zip):
    if not os.path.exists(input_folder):
        print("Input folder does not exist.")
        return

    stats = {"added": 0, "cropped": 0, "resized": 0, "skipped": 0}

    with zipfile.ZipFile(output_zip, "w") as zipf:
        for filename in os.listdir(input_folder):
            if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
                continue

            try:
                # ── Filename validation ───────────────────────────────────────
                if "." not in filename:
                    print(f"[SKIP] {filename}: filename must be 'username.extension'.")
                    stats["skipped"] += 1
                    continue

                name, ext = filename.split(".", 1)
                if ext.lower() not in ("jpg", "jpeg", "png"):
                    print(f"[SKIP] {filename}: unsupported extension.")
                    stats["skipped"] += 1
                    continue

                image_path = os.path.join(input_folder, filename)

                with Image.open(image_path) as img:
                    img = img.convert("RGB")  # normalise (handles RGBA / palette PNGs)
                    original_format = img.format  # may be None after convert — save separately
                    save_format = "JPEG" if ext.lower() in ("jpg", "jpeg") else "PNG"

                    # ── Step 1: Face crop ─────────────────────────────────────
                    print(f"Processing {filename} …")
                    img = crop_face_region(img)
                    stats["cropped"] += 1

                    # ── Step 2: Dimension / ratio check & resize ──────────────
                    width, height = img.size
                    aspect_ratio  = width / height

                    if (width > MAX_W or height > MAX_H or
                            not (MIN_AR <= aspect_ratio <= MAX_AR)):
                        print(f"   Resizing to {TARGET_W}×{TARGET_H}.")
                        img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
                        stats["resized"] += 1

                    # ── Step 3: Save to buffer and add to ZIP ─────────────────
                    buf = io.BytesIO()
                    img.save(buf, format=save_format)
                    buf.seek(0)
                    zipf.writestr(filename, buf.read())
                    print(f"   ✔ Added to ZIP.")
                    stats["added"] += 1

            except OSError as e:
                print(f"[ERROR] {filename}: {e}")
                stats["skipped"] += 1
            except Exception as e:
                print(f"[ERROR] {filename}: Unexpected — {e}")
                stats["skipped"] += 1

    # ── Summary ───────────────────────────────────────────────────────────────
    print()
    print("─" * 40)
    print(f"ZIP created : {output_zip}")
    print(f"✔ Added     : {stats['added']}")
    print(f"✂ Face-crop : {stats['cropped']}")
    print(f"↻ Resized   : {stats['resized']}")
    print(f"✗ Skipped   : {stats['skipped']}")
    print("─" * 40)


# ── Entry point ───────────────────────────────────────────────────────────────
input_folder = os.path.join(os.path.dirname(__file__), "photos")
output_zip   = os.path.join(os.path.dirname(__file__), "output.zip")
validate_and_prepare_zip(input_folder, output_zip)