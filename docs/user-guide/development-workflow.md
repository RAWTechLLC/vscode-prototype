# Development Workflow

This guide outlines the recommended development workflow for the VS Code Prototype environment.

## Development Cycle

### 1. Feature Branch Creation

Create a new branch for your feature or bugfix:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bugfix-name
```

### 2. Development Environment

1. Activate Virtual Environment:
   ```bash
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/macOS
   ```

2. Start Development Server:
   ```bash
   # For documentation
   mkdocs serve
   
   # For Python development
   python scripts/dev_server.py
   ```

### 3. Interactive Development

#### Jupyter Integration

Use Jupyter notebooks for exploratory development:

1. Create a new notebook:
   - Command Palette (Ctrl+Shift+P)
   - "Create: New Jupyter Notebook"

2. Select kernel:
   - Click "Select Kernel"
   - Choose ".venv/Python 3.x"

3. Interactive features:
   - Variable explorer
   - Data viewer
   - Plot viewer

#### VS Code Features

Utilize VS Code's Python features:

- Interactive window (Ctrl+Shift+Enter)
- Debug console (integrated terminal)
- Breakpoint debugging
- IntelliSense code completion

### 4. Testing

Run tests during development:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_specific.py

# Run tests with coverage
pytest --cov=src tests/
```

### 5. Code Quality

Maintain code quality with automated tools:

```bash
# Format code with Black
black .

# Sort imports
isort .

# Run linter
flake8
```

### 6. Documentation

Update documentation alongside code:

1. Add docstrings to new code:
   ```python
   def new_function(param: str) -> bool:
       """
       Brief description of function.

       Args:
           param (str): Parameter description

       Returns:
           bool: Return value description
       """
       pass
   ```

2. Update relevant documentation files:
   - API reference for new features
   - User guide for workflow changes
   - README for significant updates

### 7. Commit Changes

Follow commit message conventions:

```bash
# Format: <type>(<scope>): <description>
git commit -m "feat(api): add new endpoint for data processing"
git commit -m "fix(ui): resolve button alignment issue"
git commit -m "docs: update installation guide"
```

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code restructuring
- test: Adding tests
- chore: Maintenance

### 8. Pull Request

1. Push changes:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Create Pull Request:
   - Use PR template
   - Link related issues
   - Add descriptive title and description
   - Request reviewers

3. Address Review Comments:
   - Make requested changes
   - Push updates
   - Respond to comments

### 9. Merge and Deploy

After approval:

1. Merge PR:
   - Squash and merge for clean history
   - Delete feature branch

2. Deploy:
   - GitHub Actions handles deployment
   - Verify deployment success
   - Check documentation updates

## Best Practices

- Keep branches focused and short-lived
- Write tests for new features
- Update documentation proactively
- Use meaningful commit messages
- Review your own code before requesting review
- Keep PRs manageable in size

## Troubleshooting

### Common Issues

1. Virtual Environment:
   ```bash
   # Recreate if needed
   rm -rf .venv
   python -m venv .venv
   ```

2. Dependencies:
   ```bash
   # Update all dependencies
   pip install -r requirements.txt --upgrade
   ```

3. Git Issues:
   ```bash
   # Reset local changes
   git reset --hard origin/main
   
   # Clean untracked files
   git clean -fd
   ```

### Getting Help

- Check [Contributing Guidelines](../contributing/guidelines.md)
- Review [GitHub Issues](https://github.com/RAWTechLLC/vscode-prototype/issues)
- Ask in team chat/discussions

## Next Steps

- Learn about [VS Code Integration](vscode-integration.md)
- Explore available [Extensions](extensions.md)
- Review [Code Style](../best-practices/code-style.md)
