# Configuration Guide

This guide covers the configuration of your VS Code Python development environment.

## VS Code Settings

### Workspace Settings

Our workspace settings are pre-configured in `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.testing.pytestEnabled": true,
    "editor.formatOnSave": true,
    "editor.rulers": [80, 100]
}
```

### User Settings

Consider adding these helpful settings to your user configuration:

```json
{
    "editor.renderWhitespace": "all",
    "editor.wordWrap": "on",
    "files.trimTrailingWhitespace": true,
    "terminal.integrated.defaultProfile.windows": "Command Prompt"
}
```

## Python Environment

### Virtual Environment

The project uses a virtual environment for dependency isolation:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix/macOS

# Verify activation
where python  # Windows
which python  # Unix/macOS
```

### Dependencies

Project dependencies are managed through `requirements.txt`:

```bash
# Install dependencies
pip install -r requirements.txt

# Verify installations
pip list
```

## Code Quality Tools

### Black Formatter

Black is configured with default settings:

```json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

### Ruff Linter

Ruff configuration in `pyproject.toml`:

```toml
[tool.ruff]
line-length = 100
select = ["E", "F", "I"]
ignore = ["E501"]
```

### Pytest

Pytest configuration in `pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
addopts = 
    --verbose
    --cov=src
    --cov-report=term-missing
```

## Git Configuration

### Git Ignore

Project-specific exclusions in `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
.Python
*.egg-info/

# Virtual Environment
.venv/
venv/

# VS Code
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json
!.vscode/launch.json

# Testing
.coverage
coverage_html/
.pytest_cache/
```

### Git Attributes

Configure line endings in `.gitattributes`:

```gitattributes
* text=auto
*.py text diff=python
*.md text diff=markdown
*.json text
```

## Jupyter Configuration

### Kernel Setup

```bash
# Install IPython kernel
python -m ipykernel install --user --name=vscode-prototype

# Verify installation
jupyter kernelspec list
```

### Notebook Settings

VS Code Jupyter settings:

```json
{
    "jupyter.notebookFileRoot": "${workspaceFolder}",
    "jupyter.askForKernelRestart": false,
    "jupyter.enableNativeInteractiveWindow": true
}
```

## Debugging

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

## Documentation

### MkDocs Configuration

Documentation settings in `mkdocs.yml`:

```yaml
site_name: VS Code Prototype Documentation
theme:
  name: material
  features:
    - navigation.tabs
    - search.suggest
    - content.code.copy
plugins:
  - search
  - mkdocstrings
```

## Environment Variables

### Development Settings

Create `.env` file for local settings:

```env
PYTHONPATH=${workspaceFolder}
PYTEST_ADDOPTS="--color=yes"
```

### Production Settings

Create `.env.production` for production settings:

```env
PYTHONPATH=${workspaceFolder}
DEBUG=False
```

## Verification

### Configuration Check

Run these commands to verify your setup:

```bash
# Python environment
python --version
pip list

# Git configuration
git config --list

# VS Code extensions
code --list-extensions

# Jupyter kernels
jupyter kernelspec list
```

### Test Configuration

Verify testing setup:

```bash
# Run tests with coverage
pytest tests/ --cov=src

# Generate HTML coverage report
pytest tests/ --cov=src --cov-report=html
```

## Troubleshooting

### Common Issues

1. **Path Issues**
   - Verify PYTHONPATH in environment
   - Check virtual environment activation
   - Validate VS Code Python interpreter

2. **Linting Problems**
   - Verify tool installations
   - Check configuration files
   - Reload VS Code window

3. **Jupyter Errors**
   - Reinstall kernel if needed
   - Clear notebook output
   - Restart Jupyter server

## See Also

- [Installation Guide](installation.md)
- [First Steps](first-steps.md)
- [VS Code Integration](../user-guide/vscode-integration.md)
