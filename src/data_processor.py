"""
Example module demonstrating Python development features in VS Code.
"""
from typing import List, Optional
import pandas as pd
import numpy as np


class DataProcessor:
    """A class to demonstrate various Python features and VS Code integrations."""

    def __init__(self, data: Optional[pd.DataFrame] = None):
        """Initialize the DataProcessor with optional data.

        Args:
            data: Optional pandas DataFrame to process
        """
        self.data = data if data is not None else pd.DataFrame()

    def load_data(self, filepath: str) -> None:
        """Load data from a CSV file.

        Args:
            filepath: Path to the CSV file
        """
        self.data = pd.read_csv(filepath)

    def clean_data(self) -> None:
        """Clean the data by removing null values and duplicates."""
        self.data = self.data.dropna()
        self.data = self.data.drop_duplicates()

    def calculate_statistics(self, column: str) -> dict:
        """Calculate basic statistics for a specified column.

        Args:
            column: Name of the column to analyze

        Returns:
            Dictionary containing basic statistics
        """
        if column not in self.data.columns:
            raise ValueError(f"Column {column} not found in data")

        return {
            "mean": self.data[column].mean(),
            "median": self.data[column].median(),
            "std": self.data[column].std(),
            "min": self.data[column].min(),
            "max": self.data[column].max(),
        }

    def filter_data(self, conditions: List[tuple]) -> pd.DataFrame:
        """Filter data based on specified conditions.

        Args:
            conditions: List of tuples (column, operator, value)

        Returns:
            Filtered DataFrame
        """
        filtered_data = self.data.copy()

        for column, operator, value in conditions:
            if operator == "equals":
                filtered_data = filtered_data[filtered_data[column] == value]
            elif operator == "greater_than":
                filtered_data = filtered_data[filtered_data[column] > value]
            elif operator == "less_than":
                filtered_data = filtered_data[filtered_data[column] < value]
            else:
                raise ValueError(f"Unsupported operator: {operator}")

        return filtered_data

    def get_column_types(self) -> dict:
        """Get data types for each column.

        Returns:
            Dictionary mapping column names to their data types
        """
        return self.data.dtypes.to_dict()

    def generate_summary(self) -> dict:
        """Generate a summary of the data.

        Returns:
            Dictionary containing data summary
        """
        return {
            "shape": self.data.shape,
            "columns": list(self.data.columns),
            "missing_values": self.data.isnull().sum().to_dict(),
            "numeric_columns": list(self.data.select_dtypes(include=[np.number]).columns),
        }
