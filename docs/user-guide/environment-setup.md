# Environment Setup Guide

This guide covers the setup and configuration of your Python development environment.

## Python Environment

### Python Installation

1. Download Python:
   - Visit [python.org](https://python.org)
   - Download Python 3.8 or higher
   - Enable "Add Python to PATH" during installation

2. Verify Installation:
```bash
python --version
pip --version
```

### Virtual Environment

Create and activate a virtual environment:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Unix/macOS
python -m venv .venv
source .venv/bin/activate
```

### Dependencies

Install project dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Development Tools

### Required Tools

1. VS Code:
   - Download from [code.visualstudio.com](https://code.visualstudio.com)
   - Install recommended extensions

2. Git:
   - Download from [git-scm.com](https://git-scm.com)
   - Configure user settings:
     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```

### Optional Tools

1. GitHub Desktop:
   - Graphical Git interface
   - Repository management
   - Visual diff tool

2. Windows Terminal:
   - Modern terminal emulator
   - Multiple tabs and panes
   - Custom profiles

## VS Code Setup

### Python Extension

1. Install Python extension:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Python"
   - Install Microsoft's Python extension

2. Configure Python interpreter:
   - Open Command Palette (Ctrl+Shift+P)
   - "Python: Select Interpreter"
   - Choose `.venv` environment

### Additional Extensions

Install recommended extensions:

1. Development:
   - Pylance
   - Python Test Explorer
   - Python Docstring Generator

2. Code Quality:
   - Black Formatter
   - Ruff
   - mypy

3. Git Integration:
   - GitLens
   - Git History
   - Git Graph

## Project Configuration

### VS Code Settings

Workspace settings in `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "editor.formatOnSave": true,
    "editor.rulers": [80, 100]
}
```

### Launch Configurations

Debug configurations in `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: Tests",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["tests/"],
            "console": "integratedTerminal"
        }
    ]
}
```

## Testing Setup

### Pytest Configuration

Configure pytest in `pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
addopts = 
    --verbose
    --cov=src
    --cov-report=term-missing
```

### Test Discovery

Organize tests in `tests/` directory:
```
tests/
├── __init__.py
├── conftest.py
├── unit/
│   └── test_module.py
└── integration/
    └── test_integration.py
```

## Documentation Setup

### MkDocs Installation

Install documentation tools:

```bash
pip install mkdocs mkdocs-material mkdocstrings
```

### Local Documentation

Build and serve documentation:

```bash
# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

## Environment Validation

### Verification Steps

1. Python Environment:
```bash
python --version
pip list
```

2. Git Configuration:
```bash
git config --list
```

3. VS Code Extensions:
```bash
code --list-extensions
```

4. Project Setup:
```bash
# Run tests
pytest tests/

# Build docs
mkdocs build
```

## Troubleshooting

### Common Issues

1. Python Path Issues:
   - Verify PATH environment variable
   - Check virtual environment activation
   - Validate VS Code interpreter setting

2. Git Problems:
   - Check Git installation
   - Verify credentials
   - Review repository configuration

3. VS Code Integration:
   - Reload window
   - Check extension settings
   - Verify workspace configuration

### Getting Help

1. Documentation:
   - Project documentation
   - VS Code Python documentation
   - Tool-specific documentation

2. Support Channels:
   - GitHub Issues
   - Team chat
   - Documentation feedback

## See Also

- [VS Code Integration](vscode-integration.md)
- [Development Workflow](development-workflow.md)
- [Best Practices](../best-practices/code-style.md)
