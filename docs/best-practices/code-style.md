# Code Style Guide

This guide outlines the coding standards and style guidelines for the VS Code Prototype environment.

## Python Style Guidelines

### Code Formatting

We use Black for code formatting with a line length of 88 characters:

```python
# Good
def long_function_name(
    long_parameter_name: str,
    another_parameter: int,
    final_parameter: bool = False
) -> dict:
    return {"result": True}

# Bad
def long_function_name(long_parameter_name: str, another_parameter: int, final_parameter: bool = False) -> dict:
    return {"result": True}
```

### Import Organization

Use isort for organizing imports:

```python
# Standard library
import os
import sys
from typing import Dict, List, Optional

# Third-party imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Local imports
from src.data_processor import DataProcessor
from src.utils import load_config
```

### Type Hints

Use type hints for function arguments and return values:

```python
def process_data(
    input_data: pd.DataFrame,
    columns: List[str],
    threshold: Optional[float] = None
) -> Dict[str, Any]:
    """
    Process input data based on specified columns.
    
    Args:
        input_data: Input DataFrame
        columns: Columns to process
        threshold: Optional processing threshold
        
    Returns:
        Dictionary containing processed results
    """
    pass
```

### Documentation

Use Google-style docstrings:

```python
def calculate_metrics(
    predictions: np.ndarray,
    targets: np.ndarray,
    weights: Optional[np.ndarray] = None
) -> Dict[str, float]:
    """
    Calculate evaluation metrics.
    
    Args:
        predictions: Model predictions
        targets: Ground truth values
        weights: Optional sample weights
        
    Returns:
        Dictionary containing metrics:
            - accuracy: Classification accuracy
            - f1_score: F1 score
            - auc: Area under ROC curve
            
    Raises:
        ValueError: If predictions and targets have different shapes
    """
    pass
```

## Project Structure

### Directory Organization

```
project/
├── src/
│   ├── __init__.py
│   ├── data_processor.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_data_processor.py
│   └── test_utils.py
├── docs/
│   └── api/
├── notebooks/
│   └── examples/
└── scripts/
    └── dev_server.py
```

### File Naming

- Python modules: lowercase with underscores
- Test files: prefix with `test_`
- Documentation: lowercase with hyphens

## Best Practices

### Code Quality

1. Keep functions focused:
   ```python
   # Good
   def process_data(data: pd.DataFrame) -> pd.DataFrame:
       """Process input data."""
       return clean_data(validate_data(data))
   
   # Bad
   def process_and_analyze_and_save(data: pd.DataFrame) -> None:
       """Do everything in one function."""
       pass
   ```

2. Use descriptive names:
   ```python
   # Good
   def calculate_average_temperature(readings: List[float]) -> float:
       return sum(readings) / len(readings)
   
   # Bad
   def calc_avg(x: List[float]) -> float:
       return sum(x) / len(x)
   ```

### Testing

1. Test file organization:
   ```python
   # test_data_processor.py
   class TestDataProcessor:
       def setup_method(self):
           self.processor = DataProcessor()
           
       def test_process_data(self):
           assert self.processor.process_data()
           
       def test_invalid_input(self):
           with pytest.raises(ValueError):
               self.processor.process_data(None)
   ```

2. Use fixtures for common setup:
   ```python
   # conftest.py
   @pytest.fixture
   def sample_data():
       return pd.DataFrame({
           'A': [1, 2, 3],
           'B': ['x', 'y', 'z']
       })
   ```

### Error Handling

1. Use specific exceptions:
   ```python
   class DataProcessorError(Exception):
       """Base exception for data processing errors."""
       pass
   
   class InvalidInputError(DataProcessorError):
       """Raised when input data is invalid."""
       pass
   ```

2. Provide context in error messages:
   ```python
   def validate_input(data: pd.DataFrame) -> None:
       if data.empty:
           raise InvalidInputError(
               "Empty DataFrame provided. Expected non-empty data."
           )
   ```

## VS Code Configuration

### Settings

Configure VS Code settings for consistent development:

```json
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "88"
    ],
    "editor.rulers": [88],
    "editor.formatOnSave": true,
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true
}
```

### Extensions

Required extensions for code style:

1. Python
2. Pylance
3. Black Formatter
4. isort
5. flake8

## Git Practices

### Commit Messages

Follow conventional commits:

```bash
# Feature
git commit -m "feat: add data validation function"

# Bug fix
git commit -m "fix: handle empty DataFrame input"

# Documentation
git commit -m "docs: update code style guide"
```

### Pre-commit Hooks

Use pre-commit hooks for consistency:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
```

## Next Steps

- Review [Documentation Guidelines](documentation.md)
- Check [Development Workflow](../user-guide/development-workflow.md)
- Explore [VS Code Integration](../user-guide/vscode-integration.md)
