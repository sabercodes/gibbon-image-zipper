# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2024-01-01

### Added
- Initial release of Gibbon Image Zipper
- Image validation for filename format (`username.extension`)
- Dimension checking against 360×480 px maximum
- Aspect ratio enforcement (1:1.4 – 1:1.2)
- Auto-resizing to 240×320 px using bilinear interpolation for non-compliant images
- ZIP packaging of all valid and processed images
- Support for `.jpg`, `.jpeg`, and `.png` input formats
- Graceful error handling for corrupted or unreadable files
- `setup.py` for pip-installable packaging
- MIT License

---

## [Unreleased]

### Planned
- CLI argument support (`--input`, `--output`, `--dry-run`)
- Processing summary report (total images, resized count, skipped count)
- Configurable target resize dimensions
- Support for `.webp` and `.gif` input formats
- Logging to file option

See [ROADMAP.md](ROADMAP.md) for the full plan.
