# Architecture

## Overview

Gibbon Image Zipper is a single-file Python CLI utility. There is no server, database, or external API involved. All operations are local and offline.

---

## Component Diagram

```
┌─────────────────────────────────────────────────────┐
│                   image_zipper.py                    │
│                                                       │
│  validate_and_prepare_zip(input_folder, output_zip)  │
│                                                       │
│  ┌───────────────┐    ┌──────────────┐               │
│  │  os.listdir() │───▶│  Validation  │               │
│  │  (file scan)  │    │  - filename  │               │
│  └───────────────┘    │  - extension │               │
│                        └──────┬───────┘               │
│                               │                       │
│                        ┌──────▼───────┐               │
│                        │ PIL.Image    │               │
│                        │ - open()     │               │
│                        │ - size check │               │
│                        │ - resize()   │               │
│                        └──────┬───────┘               │
│                               │                       │
│                        ┌──────▼───────┐               │
│                        │  io.BytesIO  │               │
│                        │  (in-memory  │               │
│                        │   buffer)    │               │
│                        └──────┬───────┘               │
│                               │                       │
│                        ┌──────▼───────┐               │
│                        │ zipfile.ZIP  │               │
│                        │ .writestr()  │               │
│                        └─────────────┘               │
└─────────────────────────────────────────────────────┘
```

---

## Processing Pipeline

For each file in the input folder:

```
File Found
    │
    ▼
Extension valid? (.jpg/.jpeg/.png)
    │ No → print warning, skip
    │ Yes
    ▼
Filename format valid? (username.ext)
    │ No → print warning, skip
    │ Yes
    ▼
Open with PIL
    │
    ▼
Check size & aspect ratio
    │ Non-compliant → resize to 240×320 (BILINEAR)
    │ Compliant → proceed as-is
    ▼
Save to in-memory BytesIO buffer
    │
    ▼
Write to ZIP via zipfile.writestr()
    │
    ▼
Print confirmation
```

---

## Key Design Decisions

**In-memory processing:** Images are resized and written to a `BytesIO` buffer rather than saved back to disk. This keeps the original files untouched and avoids temporary file clutter.

**Single function:** The entire logic lives in `validate_and_prepare_zip()`. This makes the code easy to import and call programmatically from another script.

**zipfile.writestr:** Writing from a bytes buffer (instead of `zipf.write()` from disk) avoids path leakage in the archive and gives control over the stored filename.

---

## Dependencies

| Library | Role | Stdlib? |
|---|---|---|
| `os` | Directory listing, path operations | ✅ Yes |
| `zipfile` | ZIP archive creation | ✅ Yes |
| `io` | In-memory bytes buffer | ✅ Yes |
| `PIL` (Pillow) | Image open, inspect, resize, save | ❌ No (pip install) |
