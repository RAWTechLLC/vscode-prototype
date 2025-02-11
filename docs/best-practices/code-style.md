# Code Style Guide

This guide outlines our Python coding standards and best practices.

## Python Style Rules

### Code Formatting

We use Black for automatic code formatting:

```python
# Good - Black formatted
def calculate_statistics(
    data: pd.DataFrame,
    columns: list[str],
    include_nulls: bool = False,
) -> dict[str, float]:
    """Calculate statistics for specified columns."""
    return {
        column: data[column].mean()
        for column in columns
        if include_nulls or not data[column].isnull().any()
    }

# Bad - Inconsistent formatting
def calculate_statistics(data:pd.DataFrame,columns:list[str],include_nulls:bool=False)->dict[str,float]:
    return {column:data[column].mean() 
        for column in columns if include_nulls or not data[column].isnull().any()}
```

## Code Organization

### Imports

Organize imports in three sections:

```python
# 1. Standard library
import os
from typing import Optional, List

# 2. Third-party libraries
import numpy as np
import pandas as pd
from scipy import stats

# 3. Local modules
from .utils import calculate_metrics
from .constants import DEFAULT_THRESHOLD
```

### Variable Types

#### Type Hints

Use type hints consistently:

```python
# Good
def process_data(
    items: list[str],
    threshold: float = 0.5,
    labels: Optional[list[str]] = None,
) -> dict[str, float]:
    """Process items with optional labels."""
    
# Bad
def process_data(items, threshold=0.5, labels=None):
    """Process items with optional labels."""
```

## Documentation

### Docstrings

Use Google-style docstrings:

```python
def calculate_metrics(
    data: pd.DataFrame,
    columns: list[str],
    *,
    aggregation: str = "mean",
) -> dict[str, float]:
    """Calculate statistical metrics for specified columns.
    
    Args:
        data: Input DataFrame containing numeric data
        columns: List of column names to analyze
        aggregation: Statistical operation to perform
            Options: "mean", "median", "std"
            
    Returns:
        Dictionary mapping column names to their metrics
        
    Raises:
        ValueError: If aggregation is not supported
        KeyError: If any column is not found in data
        
    Example:
        >>> df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        >>> calculate_metrics(df, ["A", "B"])
        {"A": 2.0, "B": 5.0}
    """
```

### Comments

Use comments sparingly and meaningfully:

```python
# Good - Explains complex logic
# Apply Kalman filter to smooth noisy data
smoothed_data = apply_kalman_filter(raw_data, noise_variance)

# Bad - States the obvious
# Get the mean
mean_value = values.mean()
```

## Code Organization

### Class Structure

```python
class DataProcessor:
    """Process and analyze data with various methods."""
    
    def __init__(self, data: pd.DataFrame):
        """Initialize with input data."""
        self.data = data
        self._validate_data()
    
    def _validate_data(self) -> None:
        """Validate input data format and content."""
        if not isinstance(self.data, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")
    
    def process(self) -> pd.DataFrame:
        """Process the data and return results."""
        return self._apply_transformations()
    
    def _apply_transformations(self) -> pd.DataFrame:
        """Apply series of transformations to data."""
        # Implementation
```

### Module Structure

```python
"""Module docstring describing purpose and usage."""

# Standard library imports
import json
from typing import Optional

# Third-party imports
import numpy as np
import pandas as pd

# Constants
DEFAULT_THRESHOLD = 0.5
VALID_METRICS = ["mean", "median", "std"]

# Helper functions
def _validate_input(data: pd.DataFrame) -> None:
    """Validate input data."""
    pass

# Main functionality
class MainClass:
    """Main class docstring."""
    pass

def main_function():
    """Main function docstring."""
    pass

# Optional: Main execution
if __name__ == "__main__":
    main_function()
```

## Naming Conventions

### Variables and Functions

```python
# Good
max_iterations = 100
user_preferences = get_user_preferences()
calculate_mean_value(data_points)

# Bad
maxiter = 100
userprefs = getUserPrefs()
calc_mean(points)
```

#### Classes

```python
# Good
class DataProcessor:
    pass

class HTMLParser:
    pass

# Bad
class dataProcessor:
    pass

class Html_Parser:
    pass
```

#### Constants

```python
# Good
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT_MS = 1000
VALID_STATUS_CODES = frozenset([200, 201, 204])

# Bad
MaxConnections = 100
timeout = 1000
valid_codes = [200, 201, 204]
```

## Best Practices

### Error Handling

```python
# Good
try:
    value = process_data(input_data)
except ValueError as e:
    logger.error("Invalid data format: %s", e)
    raise
except KeyError as e:
    logger.error("Missing required field: %s", e)
    raise DataProcessingError("Missing field") from e

# Bad
try:
    value = process_data(input_data)
except:  # Too broad
    print("Error occurred")
```

#### Context Managers

```python
# Good
with open("data.txt") as f:
    content = f.read()

# Bad
f = open("data.txt")
content = f.read()
f.close()
```

#### List Comprehensions

```python
# Good - Simple, readable
squares = [x * x for x in numbers if x > 0]

# Bad - Too complex
squares = [x * x if x > 0 else 0 for x in numbers if x != None and isinstance(x, int)]
```

## Testing Style

### Test Functions

```python
# Good
def test_process_valid_data():
    """Test processing of valid input data."""
    input_data = pd.DataFrame({"A": [1, 2, 3]})
    result = process_data(input_data)
    assert result["A"].mean() == 2.0

# Bad
def test_1():
    """Test something."""
    assert process_data(pd.DataFrame({"A": [1, 2, 3]}))["A"].mean() == 2.0
```

## Test Structure

### Test Organization

```python
class TestDataProcessor:
    """Test suite for DataProcessor class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.processor = DataProcessor()
    
    def test_valid_input(self):
        """Test processing of valid input."""
        pass
    
    def test_invalid_input(self):
        """Test handling of invalid input."""
        pass
```

## See Also

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Development Workflow](../user-guide/development-workflow.md)
