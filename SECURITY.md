# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| 1.0.x | ✅ Yes |

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub issues.**

If you discover a security issue, please report it privately by:

1. Opening a [GitHub Security Advisory](https://github.com/sabercodes/gibbon-image-zipper/security/advisories/new) (preferred)
2. Or emailing the maintainer directly (see GitHub profile)

Please include:
- A description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested fix (optional)

You can expect acknowledgment within **48 hours** and a status update within **7 days**.

---

## Security Considerations

### Image Processing

This tool processes arbitrary image files using Pillow. Be aware:

- **Only run this tool on trusted input directories.** Processing images from untrusted sources may expose you to image-parsing vulnerabilities in Pillow.
- Keep Pillow updated to the latest version: `pip install --upgrade Pillow`
- Monitor [Pillow's security advisories](https://github.com/python-pillow/Pillow/security/advisories).

### File System

- The script reads from and writes to the local file system using paths you configure.
- Ensure the `input_folder` path does not point to sensitive system directories.
- The output ZIP is written to the current working directory by default.

### No Network Access

This tool operates entirely offline. It makes no network requests and does not transmit any data externally.

### No Credentials

This tool does not use, store, or handle any credentials, API keys, or authentication tokens.
