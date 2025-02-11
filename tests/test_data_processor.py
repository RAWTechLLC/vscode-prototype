"""
Test suite for the DataProcessor class.
"""
import pytest
import pandas as pd
import numpy as np
from src.data_processor import DataProcessor

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        'id': range(1, 6),
        'value': [10, 20, 30, 40, 50],
        'category': ['A', 'B', 'A', 'C', 'B'],
        'nullable': [1, None, 3, None, 5]
    })

@pytest.fixture
def processor(sample_data):
    """Create a DataProcessor instance with sample data."""
    return DataProcessor(sample_data)

def test_init_empty():
    """Test initialization with no data."""
    processor = DataProcessor()
    assert processor.data.empty

def test_init_with_data(sample_data):
    """Test initialization with data."""
    processor = DataProcessor(sample_data)
    assert processor.data.equals(sample_data)

def test_clean_data(processor):
    """Test data cleaning functionality."""
    processor.clean_data()
    assert processor.data.isnull().sum().sum() == 0
    assert len(processor.data) == 3  # After removing rows with null values

def test_calculate_statistics(processor):
    """Test statistics calculation."""
    stats = processor.calculate_statistics('value')
    assert stats['mean'] == 30
    assert stats['median'] == 30
    assert stats['min'] == 10
    assert stats['max'] == 50

def test_calculate_statistics_invalid_column(processor):
    """Test statistics calculation with invalid column."""
    with pytest.raises(ValueError):
        processor.calculate_statistics('invalid_column')

def test_filter_data(processor):
    """Test data filtering."""
    conditions = [('value', 'greater_than', 20)]
    filtered = processor.filter_data(conditions)
    assert len(filtered) == 3
    assert all(filtered['value'] > 20)

def test_filter_data_multiple_conditions(processor):
    """Test filtering with multiple conditions."""
    conditions = [
        ('value', 'greater_than', 20),
        ('category', 'equals', 'A')
    ]
    filtered = processor.filter_data(conditions)
    assert len(filtered) == 1
    assert filtered.iloc[0]['value'] == 30
    assert filtered.iloc[0]['category'] == 'A'

def test_filter_data_invalid_operator(processor):
    """Test filtering with invalid operator."""
    conditions = [('value', 'invalid_operator', 20)]
    with pytest.raises(ValueError):
        processor.filter_data(conditions)

def test_get_column_types(processor):
    """Test getting column types."""
    types = processor.get_column_types()
    assert types['id'] == np.dtype('int64')
    assert types['category'] == np.dtype('O')

def test_generate_summary(processor):
    """Test summary generation."""
    summary = processor.generate_summary()
    assert summary['shape'] == (5, 4)
    assert set(summary['columns']) == {'id', 'value', 'category', 'nullable'}
    assert summary['missing_values']['nullable'] == 2
    assert set(summary['numeric_columns']) == {'id', 'value', 'nullable'}

def test_load_data(tmp_path, processor):
    """Test data loading from CSV."""
    # Create a temporary CSV file
    csv_path = tmp_path / "test.csv"
    processor.data.to_csv(csv_path, index=False)
    
    # Test loading
    new_processor = DataProcessor()
    new_processor.load_data(str(csv_path))
    pd.testing.assert_frame_equal(new_processor.data, processor.data)
