# Development Setup Guide

This guide provides detailed instructions for setting up your development environment.

## Initial Setup

### System Requirements

1. Operating System:
   - Windows 10/11
   - macOS 10.15+
   - Linux (Ubuntu 20.04+ or equivalent)

2. Software Requirements:
   - Python 3.8 or higher
   - Git 2.30 or higher
   - VS Code 1.60 or higher

### Python Installation

1. Download Python:
   - Visit [python.org](https://python.org)
   - Download latest Python 3.x version
   - Enable "Add Python to PATH"

2. Verify Installation:
```bash
python --version
pip --version
```

## Repository Setup

### 1. Fork Repository

1. Visit project repository
2. Click "Fork" button
3. Select your account

### 2. Clone Repository

```bash
# Clone your fork
git clone https://github.com/your-username/vscode-prototype
cd vscode-prototype

# Add upstream remote
git remote add upstream https://github.com/original/vscode-prototype
```

### 3. Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate

# Unix/macOS
source .venv/bin/activate

# Verify activation
where python  # Windows
which python  # Unix/macOS
```

### 4. Dependencies

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

## VS Code Setup

### 1. Editor Installation

1. Download VS Code:
   - Visit [code.visualstudio.com](https://code.visualstudio.com)
   - Download appropriate version
   - Run installer

2. Launch VS Code:
```bash
code .
```

### 2. Extensions

Install required extensions:

1. Python Development:
   - Python
   - Pylance
   - Python Test Explorer

2. Code Quality:
   - Black Formatter
   - Ruff
   - mypy

3. Documentation:
   - Python Docstring Generator
   - markdownlint

4. Git Integration:
   - GitLens
   - Git Graph

### 3. Workspace Settings

Configure `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "editor.formatOnSave": true,
    "editor.rulers": [80, 100],
    "files.trimTrailingWhitespace": true
}
```

## Development Tools

### 1. Git Configuration

```bash
# Configure user
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Configure line endings
git config --global core.autocrlf input  # Unix/macOS
git config --global core.autocrlf true   # Windows
```

### 2. Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run against all files
pre-commit run --all-files
```

### 3. Testing Tools

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

## Project Structure

```
vscode-prototype/
├── .vscode/                # VS Code configuration
│   ├── settings.json
│   └── launch.json
├── src/                    # Source code
│   ├── __init__.py
│   └── data_processor.py
├── tests/                  # Test files
│   ├── __init__.py
│   └── test_data_processor.py
├── docs/                   # Documentation
│   ├── api/
│   ├── guides/
│   └── index.md
├── notebooks/             # Jupyter notebooks
├── .gitignore
├── pyproject.toml         # Project configuration
├── requirements.txt       # Dependencies
└── README.md
```

## Development Workflow

### 1. Feature Development

```bash
# Update main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "feat: add new feature"

# Push changes
git push origin feature/new-feature
```

### 2. Code Quality

```bash
# Format code
black src/ tests/

# Run linting
ruff check .

# Type checking
mypy src/

# Run tests
pytest tests/
```

### 3. Documentation

```bash
# Install documentation tools
pip install mkdocs mkdocs-material mkdocstrings

# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## Verification

### 1. Environment Check

```bash
# Python environment
python --version
pip list

# Git configuration
git config --list

# VS Code extensions
code --list-extensions
```

### 2. Project Check

```bash
# Run all checks
pytest tests/
black --check src/ tests/
ruff check .
mypy src/
```

### 3. Documentation Check

```bash
# Build documentation
mkdocs build --strict

# Check links
mkdocs serve
```

## Troubleshooting

### Common Issues

1. Virtual Environment:
   - Verify activation
   - Check Python path
   - Reinstall if needed

2. Dependencies:
   - Clear pip cache
   - Update requirements
   - Check conflicts

3. VS Code:
   - Reload window
   - Reset settings
   - Clear workspace state

### Getting Help

1. Documentation:
   - Check guides
   - Search issues
   - Review discussions

2. Support:
   - Open issue
   - Ask questions
   - Join discussions

## See Also

- [Contributing Guidelines](guidelines.md)
- [Code Style Guide](../best-practices/code-style.md)
- [Testing Guide](../best-practices/testing.md)
