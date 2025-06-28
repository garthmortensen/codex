# uv_pyproject.md

## Basic Structure

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-project"
version = "0.1.0"
description = "A sample project"
authors = [{name = "Your Name", email = "you@example.com"}]
readme = "README.md"
requires-python = ">=3.8"
```

## Dependencies

```toml
[project.dependencies]
pandas = ">=1.5.0"
numpy = "^1.24.0"
scikit-learn = ">=1.3.0"
matplotlib = ">=3.6.0"

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]
docs = [
    "sphinx>=5.0.0",
    "sphinx-rtd-theme>=1.0.0",
]
```

## UV Configuration

```toml
[tool.uv]
dev-dependencies = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]

[tool.uv.sources]
# Use local development version
my-package = { path = "../my-package", editable = true }

# Use specific git branch
experimental-lib = { git = "https://github.com/user/repo.git", branch = "main" }
```

## Tool Configuration

```toml
[tool.black]
line-length = 88
target-version = ['py38']

[tool.ruff]
line-length = 88
target-version = "py38"
select = ["E", "F", "W", "C90"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v --tb=short"
```

## Project Scripts

```toml
[project.scripts]
my-cli = "my_project.cli:main"
data-processor = "my_project.scripts.process:run"

[project.entry-points."console_scripts"]
my-tool = "my_project.tools:main_cli"
```

## Data Science Project Example

```toml
[project]
name = "ml-pipeline"
version = "0.1.0"
description = "Machine learning pipeline"
dependencies = [
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    "scikit-learn>=1.3.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
    "jupyter>=1.0.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
]
```