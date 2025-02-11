# Contributing Guidelines

Thank you for your interest in contributing to our project! This guide will help you get started with contributing.

## Code of Conduct

Please read and follow our Code of Conduct to maintain a respectful and inclusive environment for everyone.

## Getting Started

### Prerequisites

1. Python 3.8 or higher
2. VS Code with recommended extensions
3. Git

### Development Setup

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/your-username/vscode-prototype
cd vscode-prototype
```

3. Create virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix/macOS
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Development Process

### 1. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/*` - New features
- `fix/*` - Bug fixes
- `docs/*` - Documentation updates
- `test/*` - Test improvements

### 2. Development Standards

#### Code Style

We use:
- Black for formatting
- Ruff for linting
- Type hints for all functions
- Google-style docstrings

Example:
```python
def process_data(
    data: pd.DataFrame,
    columns: list[str],
    *,
    threshold: float = 0.5,
) -> dict[str, float]:
    """Process data and calculate metrics.
    
    Args:
        data: Input DataFrame
        columns: Columns to process
        threshold: Minimum value threshold
        
    Returns:
        Dictionary of calculated metrics
        
    Raises:
        ValueError: If threshold is negative
    """
```

#### Testing

All code changes must include tests:

```python
def test_process_data():
    """Test data processing functionality."""
    # Arrange
    data = pd.DataFrame({"A": [1, 2, 3]})
    
    # Act
    result = process_data(data, ["A"])
    
    # Assert
    assert "A" in result
    assert result["A"] > 0
```

### 3. Commit Guidelines

Use conventional commits:

```bash
# Format: <type>(<scope>): <description>

# Examples:
git commit -m "feat(processor): add data validation"
git commit -m "fix(tests): handle edge cases"
git commit -m "docs(api): update function documentation"
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `test`: Tests
- `refactor`: Code restructuring
- `style`: Formatting
- `chore`: Maintenance

### 4. Pull Request Process

1. Update Documentation:
   - Add/update docstrings
   - Update README if needed
   - Add to CHANGELOG.md

2. Run Quality Checks:
```bash
# Format code
black src/ tests/

# Run linting
ruff check .

# Run tests
pytest tests/
```

3. Create Pull Request:
   - Clear title describing change
   - Detailed description
   - Link related issues
   - Add tests
   - Update documentation

4. Code Review:
   - Address review comments
   - Keep discussion focused
   - Be respectful

## Documentation

### API Documentation

Document all public APIs:

```python
class DataProcessor:
    """Process and analyze data.
    
    This class provides methods for data processing and analysis,
    with support for various statistical operations.
    
    Attributes:
        data: pandas DataFrame containing the data
        column_types: Dictionary mapping columns to their types
    """
```

### Update Guides

Update relevant documentation:
- API reference
- User guides
- Examples
- Tutorials

## Testing Guidelines

### Test Categories

1. Unit Tests:
   - Test individual components
   - Mock dependencies
   - Fast execution

2. Integration Tests:
   - Test component interaction
   - Real dependencies
   - End-to-end scenarios

### Test Organization

```python
# tests/unit/test_processor.py
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

## Release Process

### Version Numbers

We use semantic versioning:
- MAJOR version for incompatible API changes
- MINOR version for new functionality
- PATCH version for bug fixes

### Release Steps

1. Update Version:
```bash
# Update version
echo "1.0.0" > VERSION
git add VERSION
git commit -m "chore(release): bump version to 1.0.0"
```

2. Update Changelog:
```markdown
# CHANGELOG.md
## [1.0.0] - YYYY-MM-DD
### Added
- New feature X
- Support for Y

### Fixed
- Issue with Z
```

3. Create Release:
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

## Getting Help

### Resources

1. Documentation:
   - Project documentation
   - API reference
   - Tutorials

2. Communication:
   - GitHub Issues
   - Discussions
   - Project chat

### Questions

For questions:
1. Check existing documentation
2. Search closed issues
3. Open discussion thread
4. Create new issue

## See Also

- [Development Setup](development-setup.md)
- [Code Style Guide](../best-practices/code-style.md)
- [Testing Guide](../best-practices/testing.md)
