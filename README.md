# 🗜️ Gibbon Image Zipper

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/Pillow-9.0%2B-green?style=for-the-badge" alt="Pillow"/>
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge" alt="MIT License"/>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge" alt="PRs Welcome"/>
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Cross Platform"/>
</p>

<p align="center">
  A lightweight Python CLI utility that <strong>validates</strong>, <strong>auto-resizes</strong>, and <strong>packages</strong> images into a single ZIP archive — purpose-built for school and event photo collection workflows.
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Image Requirements](#-image-requirements)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [Security](#-security)
- [License](#-license)

---

## 🔍 Overview

**Gibbon Image Zipper** solves a common pain point in educational and event administration: collecting profile photos from participants that must conform to strict size and format requirements (e.g., student ID cards, event badges, or school management systems like Gibbon SIS).

Instead of manually checking and resizing each image, drop all photos in the `photos/` folder, run one command, and receive a clean, compliant `output.zip` archive ready for upload — no configuration needed.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Zero Configuration** | Just drop images in the `photos/` folder and run |
| **Dynamic Paths** | Input and output paths are resolved automatically relative to the script location |
| **Filename Validation** | Enforces `username.extension` naming convention |
| **Dimension Checking** | Validates images are within 360×480 px |
| **Aspect Ratio Enforcement** | Ensures ratio falls between 1:1.4 and 1:1.2 |
| **Auto-Resizing** | Resizes non-compliant images to 240×320 px (bilinear interpolation) |
| **ZIP Packaging** | Bundles all processed images into a single `.zip` file |
| **Multi-Format Support** | Handles `.jpg`, `.jpeg`, and `.png` inputs |
| **Error Resilience** | Skips corrupted or invalid files with clear console output |
| **Cross-Platform** | Works on Windows, macOS, and Linux |

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
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

# Install dependencies
pip install -r requirements.txt
```

### Verify Installation

```bash
python -c "from PIL import Image; print('Pillow installed successfully')"
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
Resizing student_001.jpg to fit required size and aspect ratio.
Added student_001.jpg to ZIP file.
Added student_002.png to ZIP file.
Invalid format for document.pdf. Skipping.
Added student_003.jpeg to ZIP file.
ZIP file created: output.zip
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
| **Aspect Ratio** | 1:1.4 – 1:1.2 | Auto-resized to 240×320 px |
| **File Format** | `.jpg`, `.jpeg`, `.png` | Skipped with warning |
| **Filename Format** | `username.ext` | Skipped with warning |

> **Note:** Images that fail filename or format validation are skipped entirely. Images that fail dimension/ratio checks are automatically resized before packaging. Original files are never modified.

---

## 📁 Project Structure

```
gibbon-image-zipper/
├── photos/                # 📸 Drop your images here before running
├── output.zip             # 📦 Generated after running the script (git-ignored)
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
├── requirements.txt       # Python dependencies
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

## ⚙️ Configuration

No configuration is needed. The script automatically resolves paths relative to its own location:

```python
input_folder = os.path.join(os.path.dirname(__file__), 'photos')
output_zip   = os.path.join(os.path.dirname(__file__), 'output.zip')
```

- **Input:** `photos/` folder next to `image_zipper.py`
- **Output:** `output.zip` next to `image_zipper.py`

This means the script works correctly regardless of where the project is placed on any machine — no hardcoded paths.

See [`docs/configuration.md`](docs/configuration.md) for details on the hardcoded processing parameters (dimensions, aspect ratio) and planned CLI argument support.

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

---

## 📄 License

This project is licensed under the **MIT License** — see the [`LICENSE.md`](LICENSE.md) file for details.

---

## 🙏 Credits

Built for use with [Gibbon School Information System](https://gibbonedu.org/) photo import workflows.

---

<p align="center">If this project helped you, please consider giving it a ⭐ on GitHub!</p>