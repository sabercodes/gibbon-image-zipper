# Contributing to Gibbon Image Zipper

Thank you for taking the time to contribute! 🎉

We welcome bug reports, feature requests, documentation improvements, and code contributions.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Message Convention](#commit-message-convention)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Requesting Features](#requesting-features)

---

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold these standards.

---

## How to Contribute

1. **Fork** the repository.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/sabercodes/gibbon-image-zipper.git
   cd gibbon-image-zipper
   ```
3. **Create a branch** for your change:
   ```bash
   git checkout -b feat/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```
4. **Make your changes** following the coding standards below.
5. **Test** your changes manually.
6. **Commit** using the convention described below.
7. **Push** and open a Pull Request.

---

## Development Setup

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Install dev tools
pip install flake8 black
```

---

## Coding Standards

- Follow [PEP 8](https://pep8.org/) for Python style.
- Use **Black** for auto-formatting: `black image_zipper.py`
- Use **flake8** for linting: `flake8 image_zipper.py`
- Keep functions focused and well-documented with docstrings.
- All new functionality should include inline comments explaining intent.

---

## Commit Message Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <short description>

[optional body]
[optional footer]
```

**Types:**

| Type | When to use |
|---|---|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only changes |
| `style` | Formatting, missing semicolons, etc. |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `test` | Adding or updating tests |
| `chore` | Build process, dependency updates |

**Examples:**
```
feat: add CLI argument support for input/output paths
fix: handle images with no format attribute gracefully
docs: update installation instructions for Linux
```

---

## Pull Request Process

1. Ensure your branch is up to date with `main`:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
2. Fill in the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md).
3. Link any relevant issues (e.g., `Closes #42`).
4. A maintainer will review your PR within a few business days.
5. Address any requested changes and push updates to the same branch.

---

## Reporting Bugs

Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md). Include:

- Python version (`python --version`)
- Pillow version (`pip show Pillow`)
- OS and version
- Steps to reproduce
- Expected vs actual behavior
- Any relevant error output

---

## Requesting Features

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md). Describe:

- The problem you're trying to solve
- Your proposed solution
- Any alternatives you've considered
