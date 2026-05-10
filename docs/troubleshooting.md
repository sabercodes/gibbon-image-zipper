# Troubleshooting

---

## "Input folder does not exist."

**Cause:** The `input_folder` path in `image_zipper.py` is wrong or the folder hasn't been created yet.

**Fix:**
- Verify the path exists: `ls /path/to/folder` (Linux/macOS) or `dir C:\path\to\folder` (Windows)
- Use a raw string on Windows: `r'C:\my\photos'`
- Create the folder if missing: `mkdir /path/to/folder`

---

## "Invalid format for X. Skipping."

**Cause:** The file has an extension that isn't `.jpg`, `.jpeg`, or `.png`.

**Fix:** Convert the file to a supported format before placing it in the input folder. The script intentionally skips unsupported formats.

---

## ZIP file is created but empty

**Cause:** No files in the input folder matched the required format.

**Check:**
1. Confirm the folder contains `.jpg`, `.jpeg`, or `.png` files
2. Check the console output for skip messages
3. Verify filenames follow the `username.ext` pattern

---

## `ModuleNotFoundError: No module named 'PIL'`

**Cause:** Pillow is not installed in the active Python environment.

**Fix:**
```bash
pip install Pillow
# or
pip install -r requirements.txt
```

If using a virtual environment, make sure it's activated before running the script.

---

## `OSError: cannot identify image file`

**Cause:** A file has a `.jpg`/`.png` extension but is not actually a valid image (e.g., a renamed document).

**Fix:** The script catches `OSError` and prints a warning — the file is skipped. Remove the invalid file from the input folder.

---

## Images in the ZIP look distorted

**Cause:** The original images had an unusual aspect ratio and were auto-resized to 240×320 px using bilinear interpolation.

**Fix:** Crop or adjust the source images to the required 1:1.2–1:1.4 portrait ratio before running the script to preserve composition.

---

## `PermissionError` writing ZIP file

**Cause:** The output path is read-only, or the file is open in another application.

**Fix:**
- Close any application that may have the ZIP open
- Choose a different output path where you have write permission

---

## Script runs but prints nothing

**Cause:** The input folder is empty.

**Fix:** Place image files in the configured `input_folder` and re-run.
