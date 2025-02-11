# Documentation Guidelines

This guide outlines the documentation standards and best practices for the VS Code Prototype environment.

## Documentation Structure

### Project Documentation

```
docs/
├── index.md                  # Project overview
├── getting-started/          # Getting started guides
│   ├── installation.md
│   ├── configuration.md
│   └── first-steps.md
├── user-guide/              # User documentation
│   ├── development-workflow.md
│   ├── vscode-integration.md
│   └── extensions.md
├── api/                     # API documentation
│   └── data_processor.md
├── best-practices/          # Best practices guides
│   ├── code-style.md
│   ├── documentation.md
│   └── testing.md
└── contributing/            # Contributing guides
    ├── guidelines.md
    └── development-setup.md
```

## Writing Style

### General Guidelines

1. Use clear, concise language
2. Write in present tense
3. Use active voice
4. Include code examples
5. Provide context and explanations

### Formatting

Use Markdown formatting consistently:

```markdown
# Main Heading

## Section Heading

### Subsection

#### Details

- List item 1
- List item 2
  - Subitem 2.1
  - Subitem 2.2

1. Ordered item 1
2. Ordered item 2

> Important note or quote

`inline code`

```python
# Code block
def example():
    pass
```
```

## Code Documentation

### Python Docstrings

Use Google-style docstrings:

```python
def process_data(
    input_data: pd.DataFrame,
    options: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Process input data with specified options.
    
    Args:
        input_data: Input DataFrame to process
        options: Optional configuration dictionary
            - format (str): Output format
            - validate (bool): Whether to validate
            
    Returns:
        Dictionary containing:
            - status (str): Processing status
            - results (pd.DataFrame): Processed data
            
    Raises:
        ValueError: If input_data is empty
        TypeError: If options contains invalid values
        
    Example:
        >>> processor = DataProcessor()
        >>> result = processor.process_data(df, {'format': 'json'})
        >>> print(result['status'])
        'success'
    """
    pass
```

### Module Documentation

Include module-level docstrings:

```python
"""
Data Processing Module

This module provides utilities for processing and analyzing data
within the VS Code Prototype environment.

Classes:
    DataProcessor: Main class for data processing operations
    DataValidator: Validation utilities
    
Functions:
    load_config: Load configuration from file
    validate_schema: Validate data schema
"""

from typing import Dict, Optional

import pandas as pd

# Rest of the module code...
```

## API Documentation

### Structure

1. Overview
2. Installation/Setup
3. Basic Usage
4. API Reference
5. Examples
6. Troubleshooting

### Example

```markdown
# Data Processor API

## Overview

The Data Processor API provides utilities for processing and
analyzing data within the VS Code environment.

## Installation

```bash
pip install vscode-prototype
```

## Basic Usage

```python
from vscode_prototype import DataProcessor

processor = DataProcessor()
result = processor.process_data(input_data)
```

## API Reference

### DataProcessor

Main class for data processing operations.

#### Methods

- `process_data(input_data, options=None)`
- `analyze_results()`
```

## MkDocs Configuration

### Site Structure

Configure navigation in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Configuration: getting-started/configuration.md
    - First Steps: getting-started/first-steps.md
  - User Guide:
    - Development Workflow: user-guide/development-workflow.md
    - VS Code Integration: user-guide/vscode-integration.md
    - Extensions: user-guide/extensions.md
```

### Extensions

Enable Markdown extensions:

```yaml
markdown_extensions:
  - admonition
  - codehilite
  - toc:
      permalink: true
  - pymdownx.superfences
  - pymdownx.tabbed
```

## Contributing to Documentation

### Pull Request Process

1. Create feature branch
2. Update documentation
3. Build locally with `mkdocs serve`
4. Submit PR with description
5. Address review comments
6. Merge after approval

### Documentation Checklist

- [ ] Correct spelling and grammar
- [ ] Code examples are tested
- [ ] Links are valid
- [ ] Images have alt text
- [ ] Navigation is updated
- [ ] Mobile-friendly formatting

## Best Practices

### Content Organization

1. Progressive Disclosure:
   - Start with overview
   - Provide basic usage
   - Add advanced topics
   - Include reference material

2. Cross-Referencing:
   - Link related topics
   - Use relative links
   - Maintain link hierarchy

3. Examples:
   - Start simple
   - Show common use cases
   - Include error handling
   - Provide complete context

### Maintenance

1. Regular Updates:
   - Review for accuracy
   - Update screenshots
   - Check external links
   - Verify code examples

2. Version Control:
   - Document changes
   - Tag documentation versions
   - Maintain changelog
   - Archive old versions

## Next Steps

- Review [Code Style Guide](code-style.md)
- Check [Development Workflow](../user-guide/development-workflow.md)
- Explore [Contributing Guidelines](../contributing/guidelines.md)
