# VS Code Prototype Documentation

[![Documentation Status](https://github.com/RAWTechLLC/vscode-prototype/actions/workflows/docs.yml/badge.svg)](https://rawtechllc.github.io/vscode-prototype)

Welcome to the documentation for our VS Code Python development environment. This documentation covers everything you need to know about setting up, using, and contributing to the project.

## Documentation

This documentation is built using MkDocs and automatically deployed to GitHub Pages. You can:

- View the latest documentation at [rawtechllc.github.io/vscode-prototype](https://rawtechllc.github.io/vscode-prototype)
- Browse different versions using the version selector
- Search content using the search bar
- Navigate through sections using the sidebar

For information about contributing to the documentation, see our [GitHub Pages Setup Guide](contributing/github-pages-setup.md).

## Overview

This project provides a standardized Python development environment using VS Code, complete with:

- Python development environment
- Jupyter notebook integration
- Test-driven development setup
- Code quality tools
- Documentation generation

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/RAWTechLLC/vscode-prototype
cd vscode-prototype
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix/macOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Open in VS Code:
```bash
code .
```

## Features

### Python Development
- Full Python language support
- IntelliSense and code navigation
- Integrated debugging
- Code formatting and linting

### Jupyter Integration
- Interactive Python development
- Notebook support
- Variable explorer
- Data visualization

### Testing
- Pytest integration
- Code coverage reporting
- Test discovery and execution
- Debug test support

### Documentation
- Automatic API documentation
- Markdown support
- Live preview
- Search functionality
- Versioned documentation

## Project Structure

```
vscode-prototype/
├── .vscode/              # VS Code configuration
├── src/                 # Source code
├── tests/              # Test suite
├── notebooks/         # Jupyter notebooks
├── docs/             # Documentation
└── scripts/         # Utility scripts
```

## Key Components

### DataProcessor Class
The `DataProcessor` class demonstrates various Python features and VS Code integrations:

```python
from src.data_processor import DataProcessor

# Create an instance
processor = DataProcessor()

# Load and process data
processor.load_data('data.csv')
processor.clean_data()

# Calculate statistics
stats = processor.calculate_statistics('value_column')
```

## Next Steps

- [Installation Guide](getting-started/installation.md)
- [Configuration Guide](getting-started/configuration.md)
- [Development Workflow](user-guide/development-workflow.md)
- [API Reference](api/data_processor.md)

## Contributing

We welcome contributions! Please see:

- [Contributing Guidelines](contributing/guidelines.md) for development practices
- [Development Setup](contributing/development-setup.md) for environment setup
- [GitHub Pages Setup](contributing/github-pages-setup.md) for documentation deployment

## Support

If you encounter any issues or have questions:

1. Check the [Documentation](user-guide/environment-setup.md)
2. Review [Best Practices](best-practices/code-style.md)
3. Submit an issue on [GitHub](https://github.com/RAWTechLLC/vscode-prototype/issues)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
