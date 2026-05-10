# Frequently Asked Questions

---

**Q: What image formats are supported?**

A: `.jpg`, `.jpeg`, and `.png`. Other formats (e.g., `.webp`, `.bmp`, `.gif`) are skipped with a warning. Extended format support is planned — see [ROADMAP.md](ROADMAP.md).

---

**Q: Will the original images be modified?**

A: No. The script reads the originals, processes them in memory, and writes the results only into the ZIP archive. Your source files are never modified.

---

**Q: What happens to images that already meet the size requirements?**

A: They are added to the ZIP as-is, without any resizing.

---

**Q: My image is 350×400 px (within limits) but the aspect ratio is outside the required range. Will it be resized?**

A: Yes. Both the dimension limits AND the aspect ratio must be satisfied. If either fails, the image is resized to 240×320 px.

---

**Q: What does the required aspect ratio (1:1.4 – 1:1.2) mean?**

A: The image height must be 1.2× to 1.4× the image width — a portrait orientation. For example, 240×288 (1:1.2) to 240×336 (1:1.4) are both valid.

---

**Q: What filename format is required?**

A: Filenames must follow the pattern `username.extension` — a single dot separating the name from the extension. Files like `my.photo.jpg` (multiple dots) are handled by splitting on the first dot only.

---

**Q: Can I process multiple folders at once?**

A: Not yet in v1.0.0. Batch folder processing is on the roadmap. For now, run the script once per folder.

---

**Q: The ZIP file is empty or missing files — why?**

A: Check the console output for warning messages about skipped files. Common causes:
- Filename doesn't match `username.extension` format
- File extension is not `.jpg`, `.jpeg`, or `.png`
- File is corrupted or not a valid image

---

**Q: Can I change the target resize dimensions?**

A: In v1.0.0, the resize target is hardcoded at 240×320 px. Configurable dimensions are planned for v1.4.0.

---

**Q: Does this tool send images anywhere?**

A: No. The tool is entirely offline. It only reads from and writes to your local file system.

---

**Q: Is this compatible with Gibbon SIS?**

A: Yes, it was designed for Gibbon's photo import workflow, which requires portrait images ≤ 360×480 px in `.jpg`, `.jpeg`, or `.png` format.
