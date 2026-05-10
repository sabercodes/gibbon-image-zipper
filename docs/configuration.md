# Configuration

## v1.0.0 — Inline Configuration

In the current release, configuration is done by editing the two variables at the bottom of `image_zipper.py`:

```python
# ── Configuration ────────────────────────────────────────
input_folder = r'C:\gibbon_image_zipper'  # Path to your image folder
output_zip   = 'output.zip'               # Output ZIP filename
# ─────────────────────────────────────────────────────────
validate_and_prepare_zip(input_folder, output_zip)
```

### `input_folder`

The absolute or relative path to the folder containing the source images.

| Platform | Example |
|---|---|
| Windows | `r'C:\Users\admin\photos'` |
| macOS/Linux | `'/home/user/photos'` |
| Relative | `'./images'` |

> **Tip:** Use a raw string (`r'...'`) on Windows to avoid backslash escape issues.

### `output_zip`

The filename (or path) for the output ZIP file. Defaults to the current working directory.

```python
output_zip = 'output.zip'               # Current directory
output_zip = r'C:\output\students.zip'  # Absolute path
output_zip = './results/batch1.zip'     # Relative path
```

---

## Hardcoded Processing Parameters

The following values are currently hardcoded in `validate_and_prepare_zip()`. They can be changed directly in the source:

| Parameter | Location in code | Default |
|---|---|---|
| Max width | `if width > 360` | 360 px |
| Max height | `or height > 480` | 480 px |
| Min aspect ratio | `1/1.4` | ~0.714 |
| Max aspect ratio | `1/1.2` | ~0.833 |
| Resize target | `img.resize((240, 320), ...)` | 240×320 px |
| Resize filter | `Image.BILINEAR` | Bilinear |

---

## Planned: CLI Arguments (v1.1.0)

Future versions will support command-line arguments:

```bash
python image_zipper.py \
  --input  ./photos \
  --output students.zip \
  --max-width  360 \
  --max-height 480 \
  --resize-to  240x320 \
  --dry-run
```

See [ROADMAP.md](../ROADMAP.md) for the full plan.
