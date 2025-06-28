# pytest.md

## Basic Usage

```bash
pytest                       # Run all tests
pytest test_file.py          # Run specific test file
pytest -v                    # Verbose output
pytest -s                    # Show print statements
pytest -x                    # Stop on first failure
pytest --tb=short            # Short traceback format
pytest -k "test_name"        # Run tests matching pattern
```

## Test Discovery

```bash
pytest --collect-only        # Show which tests would run
pytest test/                 # Run tests in directory
pytest test_*.py             # Run files matching pattern
pytest -m "slow"             # Run tests with specific marker
pytest --lf                  # Run last failed tests
pytest --ff                  # Run failed tests first
```

## Test Writing

```python
import pytest

def test_function():
    assert 1 + 1 == 2

def test_with_fixture(tmp_path):
    # tmp_path is a built-in fixture
    file = tmp_path / "test.txt"
    file.write_text("content")
    assert file.read_text() == "content"

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
])
def test_increment(input, expected):
    assert input + 1 == expected
```

## Fixtures

```python
@pytest.fixture
def sample_data():
    return {"name": "test", "value": 42}

@pytest.fixture(scope="session")
def database():
    # Setup
    db = create_test_database()
    yield db
    # Teardown
    db.close()

def test_with_data(sample_data):
    assert sample_data["value"] == 42
```

## Data Science Testing

```python
import pandas as pd
import numpy as np

def test_dataframe_shape():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    assert df.shape == (3, 2)

def test_model_accuracy():
    # Test ML model performance
    accuracy = train_and_evaluate_model()
    assert accuracy > 0.8

@pytest.fixture
def sample_dataset():
    return pd.read_csv("test_data.csv")
```