# uv.md

## About
**Name:** uv (a play on 'ultraviolet', suggesting something fast, lightweight, and modern for Python package management)

**Created:** uv is a modern Python package manager and virtual environment tool, created by Astral (the maintainers of Ruff) and first released in 2023. Its purpose is to provide a faster, more reliable, and user-friendly alternative to pip and venv for managing Python dependencies and environments.

**Similar Technologies:** pip, pipenv, poetry, conda, hatch, rye

**Plain Language Definition:**
uv is a tool that helps you install Python packages and manage project environments quickly and easily, making Python development smoother.

---

## Project Management

```bash
uv init                      # Initialize new project
uv init --name myproject     # Initialize with specific name
uv add package               # Add dependency
uv add package --dev         # Add development dependency
uv remove package            # Remove dependency
uv sync                      # Install dependencies from lockfile
uv lock                      # Update lockfile
```

## Virtual Environment

```bash
uv venv                      # Create virtual environment
uv venv --python 3.11        # Create with specific Python version
uv run command               # Run command in project environment
uv run python script.py     # Run Python script
uv run --with package cmd    # Run with temporary package
uv shell                     # Activate environment shell
```

## Package Installation

```bash
uv pip install package      # Install package
uv pip install -r requirements.txt  # Install from requirements
uv pip list                  # List installed packages
uv pip freeze               # Show installed packages with versions
uv pip uninstall package    # Uninstall package
uv pip show package         # Show package information
```

## Python Management

```bash
uv python list              # List available Python versions
uv python install 3.11      # Install Python version
uv python find              # Find Python installations
uv python pin 3.11          # Pin Python version for project
```

## Data Science Workflow

```bash
# 1. Initialize ML project
uv init ml-project && cd ml-project

# 2. Add data science dependencies
uv add pandas numpy scikit-learn matplotlib jupyter

# 3. Add development tools
uv add --dev pytest black ruff

# 4. Run Jupyter notebook
uv run jupyter lab

# 5. Run tests
uv run pytest
```