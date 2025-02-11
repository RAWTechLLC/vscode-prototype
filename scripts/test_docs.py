#!/usr/bin/env python3
"""Documentation testing and validation script."""

import os
import re
import sys
import json
import urllib.request
from pathlib import Path
from typing import List, Dict, Set, Tuple
import yaml
import markdown
from bs4 import BeautifulSoup
import requests
from rich.console import Console
from rich.table import Table

console = Console()

class DocsValidator:
    """Validate documentation completeness and correctness."""
    
    def __init__(self, docs_dir: str = "docs", mkdocs_file: str = "mkdocs.yml"):
        """Initialize validator with documentation directory.
        
        Args:
            docs_dir: Path to documentation directory
            mkdocs_file: Path to mkdocs.yml configuration
        """
        self.docs_dir = Path(docs_dir)
        self.mkdocs_file = Path(mkdocs_file)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def validate_all(self) -> bool:
        """Run all validation checks.
        
        Returns:
            True if all checks pass, False otherwise
        """
        checks = [
            self.check_files_exist,
            self.validate_internal_links,
            self.validate_code_blocks,
            self.validate_api_docs,
            self.validate_navigation,
            self.check_image_references,
            self.validate_markdown
        ]
        
        success = True
        for check in checks:
            try:
                if not check():
                    success = False
            except Exception as e:
                self.errors.append(f"Error in {check.__name__}: {str(e)}")
                success = False
                
        return success
    
    def check_files_exist(self) -> bool:
        """Verify all files referenced in mkdocs.yml exist.
        
        Returns:
            True if all files exist, False otherwise
        """
        with open(self.mkdocs_file) as f:
            config = yaml.safe_load(f)
            
        def check_nav_items(items: list) -> bool:
            success = True
            for item in items:
                if isinstance(item, dict):
                    for _, path in item.items():
                        if isinstance(path, list):
                            success &= check_nav_items(path)
                        else:
                            file_path = self.docs_dir / path
                            if not file_path.exists():
                                self.errors.append(f"Missing file: {file_path}")
                                success = False
            return success
                                
        return check_nav_items(config.get('nav', []))
    
    def validate_internal_links(self) -> bool:
        """Check all internal markdown links are valid.
        
        Returns:
            True if all internal links are valid, False otherwise
        """
        success = True
        for md_file in self.docs_dir.rglob("*.md"):
            content = md_file.read_text()
            internal_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
            
            for text, link in internal_links:
                if not link.startswith(('http://', 'https://')):
                    # Remove anchor links
                    link = link.split('#')[0]
                    if link:
                        target = (md_file.parent / link).resolve()
                        if not target.exists():
                            self.errors.append(
                                f"Broken internal link in {md_file}: {link}"
                            )
                            success = False
                            
        return success
    
    def validate_external_links(self) -> bool:
        """Check external links are accessible.
        
        Returns:
            True if all external links are accessible, False otherwise
        """
        success = True
        checked_urls: Set[str] = set()
        
        for md_file in self.docs_dir.rglob("*.md"):
            content = md_file.read_text()
            external_links = re.findall(
                r'\[([^\]]+)\]\((https?://[^)]+)\)', 
                content
            )
            
            for text, url in external_links:
                if url not in checked_urls:
                    try:
                        response = requests.head(url, timeout=5)
                        if response.status_code >= 400:
                            self.errors.append(
                                f"Broken external link in {md_file}: {url}"
                            )
                            success = False
                    except requests.RequestException:
                        self.errors.append(
                            f"Failed to access external link in {md_file}: {url}"
                        )
                        success = False
                    checked_urls.add(url)
                    
        return success
    
    def validate_code_blocks(self) -> bool:
        """Validate code blocks have proper syntax.
        
        Returns:
            True if all code blocks are valid, False otherwise
        """
        success = True
        
        for md_file in self.docs_dir.rglob("*.md"):
            content = md_file.read_text()
            code_blocks = re.finditer(
                r'```(\w+)?\n(.*?)\n```', 
                content, 
                re.DOTALL
            )
            
            for match in code_blocks:
                lang, code = match.groups()
                if lang == 'python':
                    try:
                        compile(code, '<string>', 'exec')
                    except SyntaxError as e:
                        self.errors.append(
                            f"Invalid Python syntax in {md_file}: {str(e)}"
                        )
                        success = False
                        
        return success
    
    def validate_api_docs(self) -> bool:
        """Validate API documentation completeness.
        
        Returns:
            True if API docs are complete, False otherwise
        """
        success = True
        api_dir = self.docs_dir / 'api'
        
        if not api_dir.exists():
            self.errors.append("Missing API documentation directory")
            return False
            
        # Check DataProcessor documentation
        processor_doc = api_dir / 'data_processor.md'
        if not processor_doc.exists():
            self.errors.append("Missing DataProcessor API documentation")
            return False
            
        content = processor_doc.read_text()
        
        # Check for required sections
        required_sections = [
            'Class Documentation',
            'Methods',
            'Examples'
        ]
        
        for section in required_sections:
            if section.lower() not in content.lower():
                self.errors.append(
                    f"Missing section in API docs: {section}"
                )
                success = False
                
        return success
    
    def validate_navigation(self) -> bool:
        """Validate navigation structure.
        
        Returns:
            True if navigation is valid, False otherwise
        """
        with open(self.mkdocs_file) as f:
            config = yaml.safe_load(f)
            
        nav = config.get('nav', [])
        
        def validate_nav_item(item: dict) -> bool:
            success = True
            if isinstance(item, dict):
                for title, content in item.items():
                    if not isinstance(title, str):
                        self.errors.append(
                            f"Invalid navigation title: {title}"
                        )
                        success = False
                    if isinstance(content, list):
                        for child in content:
                            success &= validate_nav_item(child)
            return success
            
        return all(validate_nav_item(item) for item in nav)
    
    def check_image_references(self) -> bool:
        """Verify all referenced images exist.
        
        Returns:
            True if all images exist, False otherwise
        """
        success = True
        
        for md_file in self.docs_dir.rglob("*.md"):
            content = md_file.read_text()
            image_refs = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
            
            for alt_text, image_path in image_refs:
                if not image_path.startswith(('http://', 'https://')):
                    image_file = (md_file.parent / image_path).resolve()
                    if not image_file.exists():
                        self.errors.append(
                            f"Missing image in {md_file}: {image_path}"
                        )
                        success = False
                        
        return success
    
    def validate_markdown(self) -> bool:
        """Validate markdown formatting.
        
        Returns:
            True if markdown is valid, False otherwise
        """
        success = True
        
        for md_file in self.docs_dir.rglob("*.md"):
            content = md_file.read_text()
            
            # Check heading hierarchy
            headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
            current_level = 0
            
            for hashes, title in headings:
                level = len(hashes)
                if level - current_level > 1:
                    self.warnings.append(
                        f"Skipped heading level in {md_file}: {title}"
                    )
                current_level = level
                
            # Check for broken HTML
            try:
                html = markdown.markdown(content)
                soup = BeautifulSoup(html, 'html.parser')
            except Exception as e:
                self.errors.append(f"Invalid markdown in {md_file}: {str(e)}")
                success = False
                
        return success
    
    def print_report(self) -> None:
        """Print validation report."""
        console.print("\n=== Documentation Validation Report ===\n")
        
        if self.errors:
            error_table = Table(title="Errors", style="red")
            error_table.add_column("Error Message")
            for error in self.errors:
                error_table.add_row(error)
            console.print(error_table)
            
        if self.warnings:
            warning_table = Table(title="Warnings", style="yellow")
            warning_table.add_column("Warning Message")
            for warning in self.warnings:
                warning_table.add_row(warning)
            console.print(warning_table)
            
        if not self.errors and not self.warnings:
            console.print(
                "\n✅ All documentation checks passed!\n",
                style="green bold"
            )
            
def main():
    """Run documentation validation."""
    validator = DocsValidator()
    success = validator.validate_all()
    validator.print_report()
    sys.exit(0 if success else 1)
    
if __name__ == "__main__":
    main()
