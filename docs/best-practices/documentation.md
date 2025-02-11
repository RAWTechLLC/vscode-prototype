# Documentation Guide

This guide outlines our documentation standards and best practices.

## Documentation Types

### 1. Code Documentation

#### Docstrings

Use Google-style docstrings:

```python
def process_data(
    data: pd.DataFrame,
    columns: list[str],
    *,
    aggregation: str = "mean",
) -> dict[str, float]:
    """Process data using specified aggregation method.
    
    Args:
        data: Input DataFrame containing numeric data
        columns: List of column names to process
        aggregation: Statistical operation to perform
            Options: "mean", "median", "std"
            
    Returns:
        Dictionary mapping column names to aggregated values
        
    Raises:
        ValueError: If aggregation method is not supported
        KeyError: If column not found in DataFrame
        
    Examples:
        >>> df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        >>> process_data(df, ["A", "B"], aggregation="mean")
        {"A": 2.0, "B": 5.0}
    """
```

#### Type Hints

Use type hints consistently:

```python
from typing import Optional, Sequence, TypeVar

T = TypeVar('T', int, float)

def calculate_statistics(
    values: Sequence[T],
    weights: Optional[Sequence[float]] = None,
) -> dict[str, T]:
    """Calculate weighted statistics."""
```

### 2. API Documentation

#### Function Documentation

```python
class DataProcessor:
    """Process and analyze data with various methods.
    
    This class provides methods for loading, cleaning, and analyzing
    data using pandas DataFrames. It supports various statistical
    operations and data transformations.
    
    Attributes:
        data: pandas DataFrame containing the data
        column_types: Dictionary mapping columns to their types
        
    Examples:
        >>> processor = DataProcessor()
        >>> processor.load_data("data.csv")
        >>> processor.clean_data()
        >>> stats = processor.calculate_statistics()
    """
    
    def __init__(self, data: Optional[pd.DataFrame] = None):
        """Initialize the DataProcessor.
        
        Args:
            data: Optional DataFrame to process
        """
```

#### Module Documentation

```python
"""Data processing and analysis module.

This module provides functionality for processing and analyzing
data using pandas DataFrames. It includes:

- Data loading and validation
- Statistical analysis
- Data transformation
- Result visualization

Typical usage example:
    from data_processor import DataProcessor
    
    processor = DataProcessor()
    processor.load_data("data.csv")
    results = processor.analyze()
"""
```

### 3. Project Documentation

#### README Structure

```markdown
# Project Name

Brief description of the project.

## Features

- Feature 1: Description
- Feature 2: Description

## Installation

```bash
pip install project-name
```

## Quick Start

```python
from project_name import MainClass

obj = MainClass()
result = obj.process()
```

## Documentation

Full documentation at [GitHub Pages](https://rawtech.github.io/vscode-prototype)
```

#### Contributing Guide

```markdown
# Contributing Guide

## Development Setup

1. Clone repository
2. Install dependencies
3. Run tests

## Code Style

Follow [Code Style Guide](code-style.md)

## Pull Request Process

1. Create feature branch
2. Make changes
3. Run tests
4. Submit PR
```

## Documentation Tools

### 1. MkDocs Configuration

```yaml
# mkdocs.yml
site_name: Project Documentation
theme:
  name: material
  features:
    - navigation.tabs
    - search.suggest
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          paths: [src]
          options:
            show_source: true
```

### 2. Jupyter Notebooks

Use notebooks for tutorials and examples:

```python
# Example.ipynb
"""
# Data Processing Tutorial

This notebook demonstrates how to use the DataProcessor class.
"""

from data_processor import DataProcessor

# Create processor
processor = DataProcessor()

# Load and process data
processor.load_data("example.csv")
results = processor.process()

# Display results
display(results)
```

## Best Practices

### 1. Documentation Organization

```
project/
├── docs/
│   ├── index.md
│   ├── getting-started/
│   │   ├── installation.md
│   │   └── quickstart.md
│   ├── user-guide/
│   │   ├── basic-usage.md
│   │   └── advanced-features.md
│   ├── api/
│   │   └── reference.md
│   └── best-practices/
│       └── guidelines.md
└── README.md
```

### 2. Writing Style

#### Clear and Concise

```python
# Good
def validate_input(data: pd.DataFrame) -> bool:
    """Check if input data meets requirements.
    
    Validates:
    - No missing values
    - Numeric columns
    - Proper date format
    """

# Bad
def validate_input(data: pd.DataFrame) -> bool:
    """This function takes a pandas DataFrame as input and checks
    whether or not it meets the requirements we need for our
    processing pipeline which includes making sure there aren't
    any missing values and that the columns are numeric and the
    dates are formatted correctly as per our needs."""
```

#### Examples and Usage

```python
def calculate_metrics(data: pd.Series) -> dict[str, float]:
    """Calculate statistical metrics for a series.
    
    Args:
        data: Numeric series to analyze
        
    Returns:
        Dictionary with metrics
        
    Examples:
        >>> series = pd.Series([1, 2, 3, 4, 5])
        >>> calculate_metrics(series)
        {
            'mean': 3.0,
            'std': 1.58,
            'min': 1.0,
            'max': 5.0
        }
    """
```

### 3. Documentation Maintenance

#### Version Control

```bash
# Update docs with code changes
git add docs/
git commit -m "docs: update API reference for new features"

# Release documentation
git tag -a v1.0.0-docs -m "Documentation for version 1.0.0"
```

#### Review Process

1. Documentation Review Checklist:
   - Accuracy
   - Completeness
   - Examples
   - Links
   - Formatting

2. Automated Checks:
   - Spelling
   - Dead links
   - Code examples

## Tools Integration

### 1. VS Code Extensions

- markdownlint
- Markdown All in One
- Python Docstring Generator

### 2. Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: check-yaml
      - id: check-json
      - id: check-merge-conflict
      - id: check-case-conflict
      - id: check-docstring-first
```

### 3. CI/CD Integration

```yaml
# .github/workflows/docs.yml
name: Documentation

on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'mkdocs.yml'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```

## See Also

- [Code Style Guide](code-style.md)
- [Development Workflow](../user-guide/development-workflow.md)
- [Contributing Guidelines](../contributing/guidelines.md)
