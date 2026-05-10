# Folder Structure

```
gibbon-image-zipper/
│
├── .github/                          # GitHub community & automation files
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md             # Bug report issue template
│   │   ├── feature_request.md        # Feature request template
│   │   └── question.md               # Question template
│   ├── workflows/
│   │   ├── ci.yml                    # CI: install & import test (multi-OS, multi-Python)
│   │   ├── lint.yml                  # Lint: flake8 + black check
│   │   └── release.yml               # Release: build & publish to PyPI on tag push
│   ├── FUNDING.yml                   # GitHub Sponsors / funding links
│   └── PULL_REQUEST_TEMPLATE.md      # PR checklist template
│
├── docs/                             # Extended developer documentation
│   ├── installation.md
│   ├── architecture.md
│   ├── configuration.md
│   ├── troubleshooting.md
│   ├── development-guide.md
│   └── folder-structure.md           # This file
│
├── image_zipper.py                   # ★ Core script — entire logic lives here
├── requirements.txt                  # Runtime dependency: Pillow>=9.0.0
├── setup.py                          # Package metadata for pip install
├── .gitignore                        # Excludes venv, __pycache__, *.zip, /images/, etc.
│
├── README.md                         # Project overview and quick-start
├── CHANGELOG.md                      # Version history
├── CONTRIBUTING.md                   # Contribution guidelines
├── CODE_OF_CONDUCT.md                # Community standards
├── FAQ.md                            # Frequently asked questions
├── LICENSE / LICENSE.md              # MIT License
├── ROADMAP.md                        # Planned features
├── SECURITY.md                       # Vulnerability reporting policy
└── SUPPORT.md                        # How to get help
```

## Notes

- There is **no `src/` layout** — the single module `image_zipper.py` lives at the root, consistent with `setup.py`'s `py_modules=["image_zipper"]`.
- There is **no database, server, or configuration file** — the project is a pure CLI utility.
- The `docs/` folder contains long-form documentation. The `README.md` links to these files for detail.
