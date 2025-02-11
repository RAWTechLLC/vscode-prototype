# Git Workflow Guide

This guide outlines our Git workflow and best practices for version control.

## Basic Workflow

### 1. Branch Management

```bash
# Create feature branch
git checkout -b feature/add-data-validation

# Create bugfix branch
git checkout -b fix/memory-leak

# Create release branch
git checkout -b release/v1.0.0
```

Branch naming conventions:
- `feature/*` - New features
- `fix/*` - Bug fixes
- `release/*` - Release preparation
- `hotfix/*` - Production fixes

### 2. Daily Workflow

```bash
# Get latest changes
git fetch origin
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add src/feature.py tests/test_feature.py
git commit -m "Add new feature with tests"

# Push changes
git push origin feature/new-feature
```

## Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

Example:
```
feat(data-processor): add validation for numeric inputs

- Add type checking for numeric columns
- Implement range validation
- Add unit tests for validation

Closes #123
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

## Code Review Process

### 1. Preparing for Review

```bash
# Update branch with main
git fetch origin
git rebase origin/main

# Run tests
pytest tests/

# Run linting
ruff check .
```

### 2. Creating Pull Request

- Clear title describing change
- Detailed description
- Link related issues
- Add tests
- Update documentation

### 3. Reviewing Code

```bash
# Check out PR branch
git fetch origin
git checkout feature/new-feature

# Run tests
pytest tests/

# Make suggestions
git commit -m "review: suggest improvements"
```

### 4. Addressing Feedback

```bash
# Make requested changes
git add src/updated_file.py
git commit -m "fix(review): address feedback"

# Push updates
git push origin feature/new-feature
```

## Git Best Practices

### Commit Organization

```bash
# Good - Logical commits
git add src/validator.py
git commit -m "feat(validation): add input validator"

git add tests/test_validator.py
git commit -m "test(validation): add validator tests"

# Bad - Everything in one commit
git add .
git commit -m "add stuff"
```

### Commit History

```bash
# View history
git log --oneline --graph --decorate

# Clean up before push
git rebase -i HEAD~3  # Squash last 3 commits
```

### Branch Management

```bash
# List branches
git branch --list

# Delete merged branches
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d

# Prune remote branches
git remote prune origin
```

## Git Hooks

### Pre-commit

```bash
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
  
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
  
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.287
    hooks:
      - id: ruff
```

### Pre-push

```bash
#!/bin/sh
# .git/hooks/pre-push

# Run tests before push
python -m pytest tests/

# Check exit code
if [ $? -ne 0 ]; then
    echo "Tests must pass before push!"
    exit 1
fi
```

## Release Process

### 1. Version Bump

```bash
# Update version
echo "1.0.0" > VERSION
git add VERSION
git commit -m "chore(release): bump version to 1.0.0"
```

### 2. Release Branch

```bash
# Create release branch
git checkout -b release/1.0.0

# Update changelog
git add CHANGELOG.md
git commit -m "docs(release): update changelog for 1.0.0"
```

### 3. Release Tag

```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag
git push origin v1.0.0
```

## Troubleshooting

### Common Issues

1. Merge Conflicts
```bash
# Get latest changes
git fetch origin
git rebase origin/main

# Resolve conflicts
git add resolved_file.py
git rebase --continue
```

2. Reset Changes
```bash
# Discard uncommitted changes
git restore src/file.py

# Reset to specific commit
git reset --hard HEAD~1
```

3. Find Issues
```bash
# Find bug introduction
git bisect start
git bisect bad HEAD
git bisect good v1.0.0
```

## VS Code Integration

### Source Control View

1. Open Source Control (`Ctrl+Shift+G`)
2. Stage changes with '+'
3. Enter commit message
4. Click checkmark to commit

### Git Lens Features

- Line blame
- File history
- Branch comparison
- Repository visualization

### Git Commands

Common VS Code Git commands:
- `Git: Clone` - Clone repository
- `Git: Checkout to` - Switch branches
- `Git: Create Branch` - New branch
- `Git: Push` - Push changes
- `Git: Pull` - Pull changes

## See Also

- [Development Workflow](../user-guide/development-workflow.md)
- [Code Style Guide](code-style.md)
- [VS Code Integration](../user-guide/vscode-integration.md)
