# Installation Guide

## Requirements

| Requirement | Minimum Version |
|---|---|
| Python | 3.8 |
| Pillow | 9.0.0 |
| OS | Windows, macOS, or Linux |

---

## Method 1: Clone from GitHub (Recommended)

```bash
git clone https://github.com/sabercodes/gibbon-image-zipper.git
cd gibbon-image-zipper
pip install -r requirements.txt
```

---

## Method 2: Install via pip

```bash
pip install gibbon-image-zipper
```

---

## Method 3: Using a Virtual Environment (Best Practice)

```bash
# Create the virtual environment
python -m venv venv

# Activate it
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Verify the Installation

```bash
python -c "from PIL import Image; print('✔ Pillow ready')"
python -c "import zipfile, os, io; print('✔ Standard library ready')"
```

---

## Upgrading Pillow

```bash
pip install --upgrade Pillow
```

---

## Troubleshooting

See [troubleshooting.md](troubleshooting.md) for common installation issues.
