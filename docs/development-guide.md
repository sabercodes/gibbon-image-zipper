# Development Guide

## Setting Up a Development Environment

```bash
git clone https://github.com/sabercodes/gibbon-image-zipper.git
cd gibbon-image-zipper

python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

pip install -r requirements.txt
pip install flake8 black
```

---

## Code Style

- Formatted with **Black** (line length 120)
- Linted with **flake8**

```bash
# Auto-format
black image_zipper.py

# Lint check
flake8 image_zipper.py --max-line-length=120
```

---

## Running the Script Locally

```bash
# Edit the paths in image_zipper.py, then:
python image_zipper.py
```

For quick testing, create a small test folder:

```bash
mkdir test_images
# Copy a few .jpg/.png files in
# Set input_folder = './test_images' in image_zipper.py
python image_zipper.py
```

---

## Using the Function Programmatically

The core function can be imported and called from another script:

```python
from image_zipper import validate_and_prepare_zip

validate_and_prepare_zip(
    input_folder='./my_photos',
    output_zip='result.zip'
)
```

---

## Making a Release

1. Update `CHANGELOG.md` with the new version section
2. Bump the version in `setup.py`
3. Commit: `git commit -m "chore: bump version to 1.1.0"`
4. Tag: `git tag v1.1.0`
5. Push: `git push origin main --tags`

The `release.yml` GitHub Action will automatically build and publish to PyPI when a version tag is pushed (requires `PYPI_API_TOKEN` secret to be configured in GitHub repository settings).
