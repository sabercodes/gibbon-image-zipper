# Roadmap

This document outlines the planned development direction for Gibbon Image Zipper.

---

## v1.1.0 — CLI Interface

- [ ] Replace hardcoded path variables with CLI arguments using `argparse`
  ```bash
  python image_zipper.py --input ./photos --output students.zip
  ```
- [ ] Add `--dry-run` flag to preview what would be processed without writing
- [ ] Add `--verbose` / `--quiet` flags

---

## v1.2.0 — Enhanced Reporting

- [ ] Print a processing summary at completion:
  ```
  ✔ 42 images added
  ↻  8 images resized
  ✗  3 images skipped
  ```
- [ ] Optional `--report` flag to write a CSV report of all processed files and actions taken

---

## v1.3.0 — Extended Format Support

- [ ] Add support for `.webp` input images
- [ ] Add support for `.bmp` input images
- [ ] Configurable output format (convert all to JPEG in ZIP)

---

## v1.4.0 — Configuration File

- [ ] Support a `config.json` or `config.ini` for setting defaults (dimensions, aspect ratio tolerance, etc.)
- [ ] Allow custom filename validation patterns (regex)

---

## v2.0.0 — Web Interface (Optional / Community)

- [ ] Optional lightweight Flask or FastAPI web UI
- [ ] Drag-and-drop image upload
- [ ] Download ZIP directly from browser

---

## Ideas Under Consideration

- GitHub Actions integration for automated processing in CI pipelines
- Docker image for containerized, environment-independent execution
- Unit test suite with `pytest`

---

Want to contribute to any of these? Open an issue or pull request — all contributions are welcome!
