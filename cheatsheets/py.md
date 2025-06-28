# Python Cheatsheets - Main Index

> Before I had studied Chan for thirty years, I saw mountains as mountains, and rivers as rivers. When I arrived at a more intimate knowledge, I came to the point where I saw that mountains are not mountains, and rivers are not rivers. But now that I have got its very substance I am at rest. For it's just that I see mountains once again as mountains, and rivers once again as rivers.

This directory contains specialized Python cheatsheets organized by topic. For specific functionality, refer to the appropriate specialized file:

## Specialized Cheatsheets

- **[py_basics.md](py_basics.md)** - Python fundamentals, terminology, conditionals, loops, functions, scope
- **[py_data_structures.md](py_data_structures.md)** - Lists, dictionaries, tuples, sets and operations
- **[py_pandas.md](py_pandas.md)** - DataFrame operations, data cleaning, grouping, iloc/loc
- **[py_oop.md](py_oop.md)** - Object-oriented programming, classes, inheritance, polymorphism
- **[py_file_operations.md](py_file_operations.md)** - File I/O, CSV, JSON, path operations
- **[py_apis_web.md](py_apis_web.md)** - FastAPI, requests, web scraping, HTTP operations
- **[py_db.md](py_db.md)** - Database connections, SQL operations, PostgreSQL, Oracle
- **[py_jupyter.md](py_jupyter.md)** - Jupyter notebook operations, magic functions, display settings
- **[py_ml_ai.md](py_ml_ai.md)** - Machine learning, data preprocessing, scikit-learn, TensorFlow
- **[py_environment_setup.md](py_environment_setup.md)** - Conda, virtual environments, package management
- **[py_misc.md](py_misc.md)** - Miscellaneous utilities, decorators, SSH, Git integration

## Quick Reference

### Library Imports
```python
from sklearn.ensemble import RandomForestClassifier
sklearn  # library
ensemble  # module
RandomForestClassifier  # class
```

### Common Patterns
```python
# List comprehension
result = [item.upper() for item in my_list if condition]

# Dictionary comprehension  
metrics = {k: v for k, v in zip(keys, values)}

# Function with docstring
def my_function(param1, param2):
    """
    Brief description of function.
    
    Args:
        param1: Description
        param2: Description
        
    Returns:
        Description of return value
    """
    return result
```

### Best Practices

1. **Use virtual environments** for project isolation
2. **Follow PEP 8** style guidelines
3. **Write docstrings** for functions and classes
4. **Handle exceptions** appropriately
5. **Use type hints** for better code documentation
6. **Keep functions small** and focused on single responsibility

## Navigation

For detailed examples and comprehensive coverage of specific topics, navigate to the appropriate specialized cheatsheet file listed above.
