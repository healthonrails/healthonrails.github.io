# Contributing to Annolid

Contributions of every kind are welcome — from bug reports, documentation improvements, and example datasets to new tracking backends and GUI enhancements!

## How to Get Started

1. **Check existing issues first.** Before filing a new ticket, search [open issues](https://github.com/healthonrails/annolid/issues) and [closed issues](https://github.com/healthonrails/annolid/issues?q=is%3Aissue+is%3Aclosed) to see if the bug or idea is already being discussed.
2. **Open an issue to align early.** If your issue or feature request is new, open a concise [GitHub Issue](https://github.com/healthonrails/annolid/issues). Many helpful contributions (documentation guides, workflow recipes, test cases) require little or no code.
3. **Fork, branch, and submit a pull request.**
   - Fork the repository and create a focused feature/fix branch.
   - Set up a local `.venv` with `uv venv .venv --python 3.11 && source .venv/bin/activate && uv pip install -e ".[gui,test]"`.
   - Run targeted tests (`QT_QPA_PLATFORM=offscreen pytest -q ...`) and formatting/linting (`ruff check` / `ruff format --check`).
   - Open a pull request referencing the issue and enable **"Allow edits by maintainers"** so reviews go smoothly.

## Contributing to This Book & Docs

- The Annolid Book lives in `book/` (built with `jupyter-book build book`).
- The Docs Portal lives in `docs/` (built with `mkdocs build --strict` and checked via `make site-check`).
- Keep images web-optimized (under 2 MB when possible) and never commit machine-local paths or credentials.

See [CONTRIBUTING.md](https://github.com/healthonrails/annolid/blob/main/CONTRIBUTING.md) on GitHub for the complete developer standard.
