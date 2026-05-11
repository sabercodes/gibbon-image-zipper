# 🗜️ Gibbon Image Zipper

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/Pillow-9.0%2B-green?style=for-the-badge" alt="Pillow"/>
  <img src="https://img.shields.io/badge/OpenCV-4.0%2B-red?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge" alt="MIT License"/>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge" alt="PRs Welcome"/>
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Cross Platform"/>
</p>

<p align="center">
  A lightweight Python CLI utility that <strong>detects faces</strong>, <strong>auto-crops</strong>, <strong>validates</strong>, <strong>auto-resizes</strong>, and <strong>packages</strong> images into a single ZIP archive — purpose-built for school and event photo collection workflows.
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Image Requirements](#-image-requirements)
- [Face Detection & Crop Behaviour](#-face-detection--crop-behaviour)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [Security](#-security)
- [License](#-license)

---

## 🔍 Overview

**Gibbon Image Zipper** solves a common pain point in educational and event administration: collecting profile photos from participants that must conform to strict size and format requirements (e.g., student ID cards, event badges, or school management systems like Gibbon SIS).

Instead of manually cropping, checking, and resizing each image, drop all photos in the `photos/` folder, run one command, and receive a clean, compliant `output.zip` archive ready for upload. The script now automatically detects each person's face, crops tightly around the head and shoulders, then validates and resizes the result — all offline, with no external API required.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Face Detection** | Automatically detects the largest face in each image using OpenCV Haar Cascade |
| **Smart Face Crop** | Crops around the face with configurable padding for hair, chin, and sides |
| **Centre-Crop Fallback** | If no face is detected, falls back to a centred aspect-ratio crop instead of skipping |
| **Zero Configuration** | Just drop images in the `photos/` folder and run |
| **Dynamic Paths** | Input and output paths are resolved automatically relative to the script location |
| **Filename Validation** | Enforces `username.extension` naming convention |
| **Dimension Checking** | Validates images are within 360×480 px |
| **Aspect Ratio Enforcement** | Ensures ratio falls between 1:1.4 and 1:1.2 |
| **Auto-Resizing** | Resizes non-compliant images to 240×320 px (Lanczos interpolation) |
| **ZIP Packaging** | Bundles all processed images into a single `.zip` file |
| **Multi-Format Support** | Handles `.jpg`, `.jpeg`, and `.png` inputs |
| **Processing Summary** | Prints a full summary at the end (added / cropped / resized / skipped) |
| **Error Resilience** | Skips corrupted or invalid files with clear console output |
| **Fully Offline** | No API calls — face detection runs entirely on your local machine |
| **Cross-Platform** | Works on Windows, macOS, and Linux |

---

## 🔄 How It Works

Every image goes through a 4-step pipeline:

```
📸 Input Image
      │
      ▼
 Step 1 — Face Detection (OpenCV Haar Cascade)
      │  Face found?  ──Yes──▶  Crop around face with padding
      │  No face?     ──────▶  Centre-crop to correct aspect ratio
      │
      ▼
 Step 2 — Dimension & Ratio Validation
      │  Within 360×480 px AND ratio 1:1.2–1:1.4?  ──Yes──▶  Keep as-is
      │  Non-compliant?  ──────────────────────────────────▶  Resize to 240×320 px
      │
      ▼
 Step 3 — Save to in-memory buffer (original files never touched)
      │
      ▼
 Step 4 — Write to output.zip
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Face Detection:** [OpenCV](https://opencv.org/) (`opencv-python-headless`) ≥ 4.0 — Haar Cascade, fully offline
- **Image Processing:** [Pillow (PIL Fork)](https://python-pillow.org/) ≥ 9.0.0
- **Archiving:** Python standard library (`zipfile`, `io`, `os`)
- **Packaging:** `setuptools`

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### From Source

```bash
# Clone the repository
git clone https://github.com/sabercodes/gibbon-image-zipper.git
cd gibbon-image-zipper

# Install dependencies (now includes OpenCV)
pip install -r requirements.txt
```

### Dependencies (`requirements.txt`)

```
Pillow>=9.0.0
opencv-python-headless>=4.0.0
numpy>=1.21.0
```

> **Note:** `opencv-python-headless` is used instead of `opencv-python` because it has no GUI dependencies — lighter and works in headless server environments.

### Verify Installation

```bash
python -c "from PIL import Image; print('✔ Pillow ready')"
python -c "import cv2; print('✔ OpenCV', cv2.__version__)"
```

---

## 📖 Usage

### Basic Usage

1. Place all participant images inside the `photos/` folder in the project directory.
2. Run the script:

```bash
python image_zipper.py
```

3. The output ZIP file will be created as `output.zip` in the same project directory.

That's it — no paths to configure, no settings to change.

### Example Output

```
Processing student_001.jpg …
   ✔ Added to ZIP.
Processing student_002.png …
   No face detected — applying centre crop.
   Resizing to 240×320.
   ✔ Added to ZIP.
Processing student_003.jpeg …
   ✔ Added to ZIP.
[SKIP] document.pdf: unsupported extension.

────────────────────────────────────────
ZIP created : output.zip
✔ Added     : 3
✂ Face-crop : 3
↻ Resized   : 1
✗ Skipped   : 1
────────────────────────────────────────
```

### Windows Quick Start

```cmd
cd C:\path\to\gibbon-image-zipper
pip install -r requirements.txt

REM Drop your images into the photos\ folder, then:
python image_zipper.py
```

---

## 🖼️ Image Requirements

All images placed in the `photos/` folder are validated and processed against these rules:

| Requirement | Accepted Value | Action if Non-Compliant |
|---|---|---|
| **Max Width** | ≤ 360 px | Auto-resized to 240×320 px |
| **Max Height** | ≤ 480 px | Auto-resized to 240×320 px |
| **Aspect Ratio** | 1:1.4 – 1:1.2 (portrait) | Auto-resized to 240×320 px |
| **File Format** | `.jpg`, `.jpeg`, `.png` | Skipped with warning |
| **Filename Format** | `username.ext` | Skipped with warning |

> **Note:** Images that fail filename or format validation are skipped entirely. Images that fail dimension/ratio checks are automatically resized before packaging. **Original files are never modified.**

---

## 🤖 Face Detection & Crop Behaviour

### How face cropping works

The script uses OpenCV's Haar Cascade classifier (`haarcascade_frontalface_default.xml`) — a fast, offline face detector bundled with OpenCV.

When a face is detected, the crop box is expanded with padding in all directions to include hair, forehead, chin, and shoulders. The crop is then forced into the correct portrait aspect ratio before resizing.

### Padding defaults (tunable at the top of `image_zipper.py`)

```python
FACE_PAD_TOP    = 0.8   # 80% of face height added above  (hair / forehead)
FACE_PAD_BOTTOM = 0.3   # 30% of face height added below  (chin / neck)
FACE_PAD_SIDES  = 0.4   # 40% of face width added on each side
```

Increase these values if the crop feels too tight; decrease them if too much background is included.

### Fallback when no face is detected

If the detector finds no face (e.g. the photo is a landscape, a group shot at a distance, or the face is obscured), the script falls back to a **centre crop** that respects the required aspect ratio. The image is still added to the ZIP — it is never silently skipped due to a missed detection.

### Limitations

- Works best with **front-facing, reasonably lit portraits**.
- Side profiles, extreme angles, or very small faces may not be detected — the centre-crop fallback applies in those cases.
- Group photos will crop around the **largest detected face** only.

---

## ⚙️ Configuration

No configuration is needed for basic use. The script automatically resolves paths relative to its own location:

```python
input_folder = os.path.join(os.path.dirname(__file__), 'photos')
output_zip   = os.path.join(os.path.dirname(__file__), 'output.zip')
```

- **Input:** `photos/` folder next to `image_zipper.py`
- **Output:** `output.zip` next to `image_zipper.py`

### Tunable parameters (top of `image_zipper.py`)

| Parameter | Default | Description |
|---|---|---|
| `TARGET_W` | `240` | Resize target width (px) |
| `TARGET_H` | `320` | Resize target height (px) |
| `MAX_W` | `360` | Maximum allowed width (px) |
| `MAX_H` | `480` | Maximum allowed height (px) |
| `FACE_PAD_TOP` | `0.8` | Padding above face (fraction of face height) |
| `FACE_PAD_BOTTOM` | `0.3` | Padding below face (fraction of face height) |
| `FACE_PAD_SIDES` | `0.4` | Padding left/right (fraction of face width) |

See [`docs/configuration.md`](docs/configuration.md) for full details.

---

## 📁 Project Structure

```
gibbon-image-zipper/
├── photos/                # 📸 Drop your images here before running
├── output.zip             # 📦 Generated after running the script (git-ignored)
├── haarcascade_frontalface_default.xml  # Auto-downloaded if missing
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── question.md
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── lint.yml
│   │   └── release.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── installation.md
│   ├── architecture.md
│   ├── configuration.md
│   ├── development-guide.md
│   ├── folder-structure.md
│   └── troubleshooting.md
├── image_zipper.py        # Core script
├── requirements.txt       # Python dependencies (Pillow + OpenCV + NumPy)
├── setup.py               # Package configuration
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── FAQ.md
├── LICENSE.md
├── README.md
├── ROADMAP.md
├── SECURITY.md
├── SUPPORT.md
└── .gitignore
```

---

## 🤝 Contributing

Contributions are welcome and appreciated! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
# Open a Pull Request
```

---

## 🗺️ Roadmap

See [`ROADMAP.md`](ROADMAP.md) for planned features including CLI argument support, batch processing improvements, and output reporting.

---

## 🔒 Security

For security vulnerabilities, please see [`SECURITY.md`](SECURITY.md). Do **not** open public GitHub issues for security reports.

> **Security note for face detection:** This tool processes images entirely offline using a local OpenCV classifier. No image data is sent to any external server or API.

---

## 📄 License

This project is licensed under the **MIT License** — see the [`LICENSE.md`](LICENSE.md) file for details.

---

## 🙏 Credits

Built for use with [Gibbon School Information System](https://gibbonedu.org/) photo import workflows.

Face detection powered by [OpenCV](https://opencv.org/) Haar Cascade classifiers.

---

<p align="center">If this project helped you, please consider giving it a ⭐ on GitHub!</p>