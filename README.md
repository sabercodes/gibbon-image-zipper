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

Instead of manually checking and resizing each image, drop all photos in a folder, run one command, and receive a clean, compliant ZIP archive ready for upload.

---

## ✨ Features

| Feature | Description |
|---|---|
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

### As a Package (pip install)

```bash
pip install gibbon-image-zipper
```

### Verify Installation

```bash
python -c "from PIL import Image; print('Pillow installed successfully')"
```

---

## 📖 Usage

### Basic Usage

1. Place all participant images in an input folder.
2. Open `image_zipper.py` and set the paths at the bottom of the file:

```python
input_folder = '/path/to/your/images'   # Folder containing source images
output_zip   = 'output.zip'             # Desired output ZIP filename
```

3. Run the script:

```bash
python image_zipper.py
```

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
python image_zipper.py
```

---

## 🖼️ Image Requirements

All images in the input folder are validated and processed against these rules:

| Requirement | Accepted Value | Action if Non-Compliant |
|---|---|---|
| **Max Width** | ≤ 360 px | Auto-resized to 240×320 px |
| **Max Height** | ≤ 480 px | Auto-resized to 240×320 px |
| **Aspect Ratio** | 1:1.4 – 1:1.2 | Auto-resized to 240×320 px |
| **File Format** | `.jpg`, `.jpeg`, `.png` | Skipped with warning |
| **Filename Format** | `username.ext` | Skipped with warning |

> **Note:** Images that fail filename or format validation are skipped entirely. Images that fail dimension/ratio checks are automatically resized before packaging.

---

## 📁 Project Structure

```
gibbon-image-zipper/
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
│   └── troubleshooting.md
├── image_zipper.py        # Core script
├── requirements.txt       # Python dependencies
├── setup.py               # Package configuration
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md
├── ROADMAP.md
├── SECURITY.md
└── .gitignore
```

---

## ⚙️ Configuration

Currently the script is configured by editing the two variables at the bottom of `image_zipper.py`:

```python
input_folder = r'C:\path\to\images'  # Input directory (absolute or relative)
output_zip   = 'output.zip'          # Output ZIP filename
```

See [`docs/configuration.md`](docs/configuration.md) for planned CLI argument support.

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

This project is licensed under the **MIT License** — see the [`LICENSE`](LICENSE) file for details.

---

## 🙏 Credits

Built for use with [Gibbon School Information System](https://gibbonedu.org/) photo import workflows.

---

<p align="center">If this project helped you, please consider giving it a ⭐ on GitHub!</p>
