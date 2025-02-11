# DataProcessor API Reference

## Overview

The `DataProcessor` class provides functionality for loading, cleaning, and analyzing data using pandas DataFrames. It demonstrates various Python features and VS Code integrations.

## Class Documentation

::: src.data_processor.DataProcessor
    handler: python
    options:
      show_root_heading: true
      show_source: true
      members:
        - __init__
        - load_data
        - clean_data
        - calculate_statistics
        - filter_data
        - get_column_types
        - generate_summary

## Methods

### Data Loading and Cleaning

- `__init__(data: Optional[pd.DataFrame] = None)`: Initialize the processor
- `load_data(path: str)`: Load data from a file
- `clean_data()`: Clean and preprocess the data

### Analysis and Processing

- `calculate_statistics(column: str) -> dict[str, float]`: Calculate column statistics
- `filter_data(conditions: list[tuple]) -> pd.DataFrame`: Filter data based on conditions
- `get_column_types() -> dict[str, str]`: Get column data types
- `generate_summary() -> dict`: Generate data summary statistics

## Usage Examples

### Basic Usage

```python
from src.data_processor import DataProcessor

# Initialize processor
processor = DataProcessor()

# Load data from CSV
processor.load_data("data.csv")

# Clean the data
processor.clean_data()

# Get data summary
summary = processor.generate_summary()
print(summary)
```

## Working with Statistics

### Example Usage

```python
# Calculate statistics for a specific column
stats = processor.calculate_statistics("value")
print(f"Mean: {stats['mean']}")
print(f"Median: {stats['median']}")
print(f"Standard Deviation: {stats['std']}")
```

## Filtering Data

### Example Usage

```python
# Define filter conditions
conditions = [
    ("value", "greater_than", 100),
    ("category", "equals", "A")
]

# Apply filters
filtered_data = processor.filter_data(conditions)
print(f"Found {len(filtered_data)} matching records")
```

## Column Type Analysis

### Example Usage

```python
# Get data types for all columns
types = processor.get_column_types()
for column, dtype in types.items():
    print(f"{column}: {dtype}")
```

## Integration with Jupyter

The DataProcessor class works seamlessly in Jupyter notebooks. Here's an example notebook workflow:

```python
# In a Jupyter notebook
import pandas as pd
import numpy as np
from src.data_processor import DataProcessor

# Create sample data
data = pd.DataFrame({
    'id': range(1, 101),
    'value': np.random.normal(100, 15, 100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

# Initialize processor with data
processor = DataProcessor(data)

# Generate and display summary
summary = processor.generate_summary()
display(summary)

# Calculate and plot statistics
import matplotlib.pyplot as plt

stats = processor.calculate_statistics('value')
plt.figure(figsize=(10, 6))
plt.hist(processor.data['value'], bins=20)
plt.title('Value Distribution')
plt.show()
```

## Error Handling

The DataProcessor class includes robust error handling:

```python
try:
    # This will raise an error for non-existent column
    stats = processor.calculate_statistics('invalid_column')
except ValueError as e:
    print(f"Error: {e}")

try:
    # This will raise an error for invalid operator
    conditions = [('value', 'invalid_operator', 100)]
    filtered = processor.filter_data(conditions)
except ValueError as e:
    print(f"Error: {e}")
```

## Best Practices

1. Always clean data after loading:
```python
processor.load_data('data.csv')
processor.clean_data()
```

2. Check data summary before processing:
```python
summary = processor.generate_summary()
print(f"Missing values: {summary['missing_values']}")
```

3. Use type checking for columns:
```python
types = processor.get_column_types()
numeric_columns = [col for col, dtype in types.items() 
                  if np.issubdtype(dtype, np.number)]
```

## See Also

- [User Guide](../user-guide/development-workflow.md)
- [Jupyter Integration](../user-guide/vscode-integration.md#jupyter-notebooks)
- [Best Practices](../best-practices/code-style.md)
