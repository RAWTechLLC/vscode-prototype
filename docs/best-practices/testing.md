# Testing Guide

This guide outlines our testing practices and standards for Python development.

## Testing Framework

We use pytest as our testing framework:

```python
# tests/test_example.py
import pytest
from src.example import process_data

def test_process_data():
    """Test basic data processing functionality."""
    input_data = [1, 2, 3]
    result = process_data(input_data)
    assert result == [2, 4, 6]
```

## Test Organization

### Directory Structure

```
project/
├── src/
│   ├── __init__.py
│   └── module.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── unit/
    │   └── test_module.py
    └── integration/
        └── test_integration.py
```

### Test Categories

1. Unit Tests
```python
# tests/unit/test_calculator.py
def test_add():
    """Test addition in isolation."""
    calc = Calculator()
    assert calc.add(2, 2) == 4
```

2. Integration Tests
```python
# tests/integration/test_data_pipeline.py
def test_data_pipeline():
    """Test complete data processing pipeline."""
    processor = DataProcessor()
    loader = DataLoader()
    
    data = loader.load("test_data.csv")
    result = processor.process(data)
    assert result.shape == (100, 10)
```

3. Functional Tests
```python
# tests/functional/test_workflow.py
def test_complete_workflow():
    """Test end-to-end workflow."""
    workflow = Workflow()
    result = workflow.run("input.csv", "output.csv")
    assert result.success
```

## Test Fixtures

### Basic Fixtures

```python
# tests/conftest.py
import pytest
import pandas as pd

@pytest.fixture
def sample_data():
    """Provide sample DataFrame for testing."""
    return pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6]
    })

@pytest.fixture
def processor(sample_data):
    """Provide configured DataProcessor instance."""
    from src.processor import DataProcessor
    return DataProcessor(sample_data)
```

### Fixture Scopes

```python
@pytest.fixture(scope="session")
def database_connection():
    """Create database connection for test session."""
    conn = create_connection()
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def temp_data():
    """Provide temporary data for single test."""
    data = create_temp_data()
    yield data
    cleanup_temp_data(data)
```

## Test Cases

### Parameterized Tests

```python
@pytest.mark.parametrize("input_value,expected", [
    (2, 4),
    (0, 0),
    (-1, -2),
    (1.5, 3.0),
])
def test_double(input_value, expected):
    """Test doubling with various inputs."""
    assert double(input_value) == expected
```

### Exception Testing

```python
def test_invalid_input():
    """Test handling of invalid input."""
    with pytest.raises(ValueError) as exc_info:
        process_data(None)
    assert "Input cannot be None" in str(exc_info.value)
```

### Mock Objects

```python
from unittest.mock import Mock, patch

def test_api_call(mocker):
    """Test external API call."""
    mock_response = Mock()
    mock_response.json.return_value = {"status": "success"}
    
    with patch('requests.get') as mock_get:
        mock_get.return_value = mock_response
        result = call_api("endpoint")
        assert result["status"] == "success"
```

## Testing Patterns

### Arrange-Act-Assert

```python
def test_data_processing():
    """Test data processing using AAA pattern."""
    # Arrange
    processor = DataProcessor()
    input_data = [1, 2, 3]
    
    # Act
    result = processor.process(input_data)
    
    # Assert
    assert len(result) == 3
    assert all(x > 0 for x in result)
```

### Given-When-Then

```python
def test_user_registration():
    """Test user registration using Given-When-Then."""
    # Given
    user_data = {"username": "test", "email": "test@example.com"}
    
    # When
    response = register_user(user_data)
    
    # Then
    assert response.status_code == 201
    assert response.json()["username"] == "test"
```

## Test Coverage

### Coverage Configuration

```ini
# pytest.ini
[pytest]
addopts = 
    --cov=src
    --cov-report=term-missing
    --cov-report=html
```

### Coverage Checking

```python
# tests/test_coverage.py
@pytest.mark.coverage
def test_edge_cases():
    """Test edge cases for coverage."""
    processor = DataProcessor()
    
    # Test empty input
    assert processor.process([]) == []
    
    # Test single item
    assert processor.process([1]) == [1]
    
    # Test large input
    large_input = list(range(1000))
    assert len(processor.process(large_input)) == 1000
```

## Performance Testing

### Timing Tests

```python
import time

def test_performance():
    """Test processing performance."""
    start_time = time.time()
    result = process_large_dataset()
    duration = time.time() - start_time
    
    assert duration < 1.0  # Should complete within 1 second
```

### Load Testing

```python
@pytest.mark.slow
def test_concurrent_processing():
    """Test handling of concurrent requests."""
    import concurrent.futures
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(process_data, i)
            for i in range(100)
        ]
        results = [f.result() for f in futures]
    
    assert len(results) == 100
```

## Best Practices

### Test Naming

```python
# Good
def test_process_valid_input_returns_expected_result():
    pass

def test_process_empty_input_raises_value_error():
    pass

# Bad
def test_1():
    pass

def test_process():
    pass
```

### Test Independence

```python
# Good
def test_stateless_operation():
    """Test without dependencies on other tests."""
    processor = DataProcessor()
    assert processor.process([1, 2, 3]) == [2, 4, 6]

# Bad
global_data = []

def test_dependent():
    """Test depending on global state."""
    global_data.append(1)
    assert len(global_data) == 1
```

### Test Readability

```python
# Good
def test_user_registration_success():
    """Test successful user registration."""
    # Given
    user = create_test_user()
    
    # When
    result = register_user(user)
    
    # Then
    assert result.success
    assert result.user.id is not None
    assert result.user.username == user.username

# Bad
def test_reg():
    """Test reg."""
    assert register_user({"u": "test", "p": "pass"}).s
```

## See Also

- [pytest Documentation](https://docs.pytest.org/)
- [Code Style Guide](code-style.md)
- [Development Workflow](../user-guide/development-workflow.md)
