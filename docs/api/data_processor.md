# Data Processor API

This document describes the Data Processor API provided by the VS Code Prototype environment.

## Overview

The Data Processor module provides utilities for processing and analyzing data within the VS Code environment.

## Classes

### DataProcessor

Main class for data processing operations.

```python
class DataProcessor:
    """
    A class for processing and analyzing data.
    
    Attributes:
        input_path (str): Path to input data
        output_path (str): Path for processed output
    """
    
    def __init__(self, input_path: str, output_path: str):
        """
        Initialize the DataProcessor.
        
        Args:
            input_path (str): Path to input data
            output_path (str): Path for processed output
        """
        self.input_path = input_path
        self.output_path = output_path
```

## Methods

### process_data

```python
def process_data(self, options: dict = None) -> bool:
    """
    Process the input data according to specified options.
    
    Args:
        options (dict, optional): Processing options. Defaults to None.
            Supported options:
            - format (str): Output format ('csv', 'json')
            - compress (bool): Whether to compress output
            
    Returns:
        bool: True if processing successful, False otherwise
        
    Raises:
        ValueError: If input file not found
        TypeError: If options invalid
    """
    pass
```

### analyze_results

```python
def analyze_results(self) -> dict:
    """
    Analyze the processed data.
    
    Returns:
        dict: Analysis results containing:
            - row_count (int): Number of processed rows
            - error_count (int): Number of errors
            - processing_time (float): Time taken in seconds
    """
    pass
```

## Usage Examples

### Basic Usage

```python
from src.data_processor import DataProcessor

# Initialize processor
processor = DataProcessor('input.csv', 'output.json')

# Process data
options = {
    'format': 'json',
    'compress': True
}
success = processor.process_data(options)

# Analyze results
if success:
    results = processor.analyze_results()
    print(f"Processed {results['row_count']} rows")
```

### Error Handling

```python
try:
    processor = DataProcessor('missing.csv', 'output.json')
    processor.process_data()
except ValueError as e:
    print(f"Error: {e}")
```

## Configuration

### Settings

The DataProcessor can be configured through VS Code settings:

```json
{
    "dataProcessor.defaultFormat": "json",
    "dataProcessor.compression": true,
    "dataProcessor.maxRows": 1000000
}
```

### Environment Variables

Required environment variables:

- `DATA_PROCESSOR_INPUT_DIR`: Default input directory
- `DATA_PROCESSOR_OUTPUT_DIR`: Default output directory

## Testing

Run the test suite:

```bash
pytest tests/test_data_processor.py
```

Example test:

```python
def test_process_data():
    processor = DataProcessor('test_input.csv', 'test_output.json')
    assert processor.process_data() == True
    results = processor.analyze_results()
    assert results['error_count'] == 0
```

## Best Practices

1. Input Validation
   - Always validate input file existence
   - Check file format compatibility
   - Verify data structure

2. Error Handling
   - Use appropriate exception types
   - Provide detailed error messages
   - Log errors for debugging

3. Performance
   - Process large files in chunks
   - Use appropriate data structures
   - Monitor memory usage

## Next Steps

- Review [Code Style](../best-practices/code-style.md)
- Check [Development Workflow](../user-guide/development-workflow.md)
- Explore [VS Code Integration](../user-guide/vscode-integration.md)
