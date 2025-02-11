# VS Code Prototype Environment

[![Documentation Status](https://github.com/RAWTechLLC/vscode-prototype/actions/workflows/docs.yml/badge.svg)](https://rawtechllc.github.io/vscode-prototype)

## Overview
Test environment for validating VS Code configurations, development workflows, and Python tooling integration. The project documentation is available at [rawtechllc.github.io/vscode-prototype](https://rawtechllc.github.io/vscode-prototype).

## Structure
```
vscode-prototype/
├── .vscode/              # VS Code configuration
├── src/                 # Source code
├── tests/              # Test suite
├── notebooks/         # Jupyter notebooks
├── docs/             # Documentation
└── scripts/         # Utility scripts
```

## Features
- Python development environment
- Jupyter notebook integration
- Interactive Python window
- Git integration
- Custom theme configuration

## Setup
1. Create virtual environment:
```bash
python -m venv .venv
```

2. Activate environment:
```bash
# Windows
.venv\Scripts\activate
# Unix/macOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## VS Code Configuration
- Theme: Atom One Dark
- Icons: Material Icon Theme
- Extensions: See .vscode/extensions.json

## Testing
```bash
pytest tests/
```

## Development
- Interactive Python window available
- Jupyter notebooks in notebooks/
- Auto-formatting enabled
- Git integration configured

## Documentation
Our comprehensive documentation is available online at [rawtechllc.github.io/vscode-prototype](https://rawtechllc.github.io/vscode-prototype), covering:
- Development workflow
- Environment setup
- Testing procedures
- Best practices
- API reference

### Local Documentation
To build and serve documentation locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Serve documentation (with live reload)
mkdocs serve

# Build documentation
mkdocs build
```

The documentation will be available at `http://127.0.0.1:8000`.
