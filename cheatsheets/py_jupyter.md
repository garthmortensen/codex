# py_jupyter.md

## Jupyter Labs / Notebooks

### Cell Operations

In cell, to split single cell into another cell, place cursor at split and push `control-shift-minus`.

Jupyter notebook merge current cell with next:
`shift-m`

### Display and Formatting

Create red text in notebook:
```python
<font color='red'>@@@</font> <font color='red'>@@@</font>
```

Setting these options will allow for reviewing more of the DataFrames:
```python
pd.set_option("display.max_rows", 2000)
pd.set_option("display.max_columns", 2000)
pd.set_option("display.width", 1000)
```

### Magic Functions

Setting the %matplotlib inline feature is necessary for displaying the plots in the notebook:
```python
%matplotlib inline
```

Get magic functions programmatically (like %matplotlib inline):
```python
get_ipython().run_line_magic("matplotlib", "inline")
```

### Tab Completion

Tab complete in jupyter:
```python
pd.options.<TAB>
```

### File Operations

Print current file directory:
```python
import os
print(os.path.dirname(os.getcwd()).split('\\')[-1])
```

Get current working directory:
```python
import os
os.path.realpath(__file__)
# Reference: http://www.faqs.org/docs/diveintopython/regression_path.html
```

## Best Practices

1. **Use markdown cells** for documentation and explanations
2. **Keep cells focused** - one concept per cell
3. **Use meaningful variable names** especially in shared notebooks
4. **Clear output before committing** to version control
5. **Use magic functions** to enhance functionality (%time, %debug, etc.)