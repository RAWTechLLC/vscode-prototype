# GitHub Pages Setup Guide

This guide explains how to enable GitHub Pages and perform the initial documentation deployment.

## Repository Settings

1. Go to the repository settings:
   ```
   https://github.com/RAWTechLLC/vscode-prototype/settings
   ```

2. Navigate to "Pages" in the sidebar

3. Configure GitHub Pages:
   - Source: Deploy from a branch
   - Branch: gh-pages
   - Folder: / (root)
   - Click "Save"

## Initial Deployment

1. Ensure you have the latest changes:
   ```bash
   git pull origin main
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize versioning:
   ```bash
   mike list  # Check current versions
   mike deploy --push main latest  # Deploy main as latest version
   ```

4. Verify deployment:
   - Wait for GitHub Actions workflow to complete
   - Visit https://rawtechllc.github.io/vscode-prototype
   - Check that all pages load correctly
   - Verify navigation and search functionality

## Troubleshooting

### Common Issues

1. 404 Page Not Found
   - Verify gh-pages branch exists
   - Check repository settings
   - Ensure workflow completed successfully

2. Missing Content
   - Check mkdocs.yml navigation structure
   - Verify all referenced files exist
   - Rebuild locally to check for errors

3. Styling Issues
   - Clear browser cache
   - Check theme configuration
   - Verify asset paths

### Local Testing

Before pushing changes:

```bash
# Build documentation locally
mkdocs build

# Serve documentation
mkdocs serve

# Check for errors
mkdocs build --strict
```

## Maintaining Documentation

### Version Management

Create new documentation versions:
```bash
# Deploy new version
mike deploy --push 1.0.0

# Set default version
mike set-default --push 1.0.0

# List all versions
mike list
```

### Branch Protection

Configure branch protection rules:
1. Go to repository settings
2. Navigate to "Branches"
3. Add rule for `gh-pages`:
   - Require pull request reviews
   - Require status checks to pass
   - Include administrators
   - Allow force pushes (for documentation updates)

## PR Review Process

When reviewing documentation changes:

1. Check the PR preview:
   - Download the documentation-preview artifact
   - Open site/index.html locally
   - Verify all changes render correctly

2. Review versioning:
   - Check version tags
   - Verify correct version is updated
   - Ensure version links work

3. Validate links:
   - Internal navigation
   - External resources
   - API references

## See Also

- [Contributing Guidelines](guidelines.md)
- [Development Setup](development-setup.md)
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
