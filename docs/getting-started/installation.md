# Installation Guide

This guide walks you through the process of setting up the VS Code Python development environment.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (3.8 or higher)
- [VS Code](https://code.visualstudio.com/Download)
- [Git](https://git-scm.com/downloads)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rawtech/vscode-prototype
cd vscode-prototype
```

### 2. Set Up Python Environment

#### Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Unix/macOS
python -m venv .venv
source .venv/bin/activate
```

#### Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. VS Code Setup

#### Install Required Extensions

Launch VS Code Quick Open (Ctrl+P) and run the following commands:

```
ext install ms-python.python
ext install ms-python.vscode-pylance
ext install ms-toolsai.jupyter
ext install charliermarsh.ruff
ext install ms-python.black-formatter
```

Or install our recommended extensions:

1. Open VS Code
2. Go to Extensions view (Ctrl+Shift+X)
3. Type `@recommended` in the search box
4. Install all workspace recommended extensions

#### Configure VS Code Settings

Our workspace settings are automatically applied through `.vscode/settings.json`. Key configurations include:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "editor.formatOnSave": true
}
```

### 4. Verify Installation

Run the following checks to verify your setup:

#### Test Python Environment
```bash
python -c "import pandas; print(pandas.__version__)"
```

#### Run Test Suite
```bash
python -m pytest tests/
```

#### Launch Jupyter Notebook
```bash
jupyter notebook notebooks/data_analysis_example.ipynb
```

## Common Issues and Solutions

### Virtual Environment Not Recognized

**Problem**: VS Code doesn't recognize the virtual environment.

**Solution**: 
1. Open Command Palette (Ctrl+Shift+P)
2. Select "Python: Select Interpreter"
3. Choose the `.venv` environment

### Import Errors

**Problem**: Unable to import project modules.

**Solution**: Ensure you're:
1. Using the correct virtual environment
2. Running commands from the project root
3. Have installed all dependencies

### Jupyter Notebook Kernel Missing

**Problem**: Jupyter notebooks show "No kernel" error.

**Solution**:
1. Select kernel from the top-right corner
2. Choose "Python (.venv)"
3. If missing, run: `python -m ipykernel install --user`

## Next Steps

After installation:

1. Review the [Configuration Guide](configuration.md)
2. Try the [First Steps Tutorial](first-steps.md)
3. Explore the [Development Workflow](../user-guide/development-workflow.md)

## Troubleshooting

If you encounter issues:

1. Verify Python version:
```bash
python --version
```

2. Check virtual environment:
```bash
# Should show .venv path
which python  # Unix/macOS
where python  # Windows
```

3. Validate VS Code extensions:
```bash
code --list-extensions
```

4. Review VS Code Python output:
   - Open Command Palette (Ctrl+Shift+P)
   - Type "Python: Show Output"
   - Select "Python"

Still having problems? Check our [GitHub Discussions](https://github.com/rawtech/vscode-prototype/discussions) or create a new issue.
