# py_misc.md

## Documentation Tools

### MkDocs

https://www.mkdocs.org/getting-started/

```bash
pip install -r requirements.txt  # ?
pip install mkdocs
```

```bash
mkdocs new my-project
cd my-project
mkdocs serve  # ?
```

## System Integration

### SSH Key Generation

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# If you are using a legacy system that doesn't support the Ed25519 algorithm, use:
ssh-keygen –t rsa –b 4096 –C "YOURGITHUBEMAIL@PLACEHOLDER.NET"
```

### Git Branch Operations

Create and checkout branch (-b = create the new branch and immediately switch to it):
```bash
git checkout -b add-new-python-script
```

Create a new branch which doesn't exist, switch to it (-c = create new branch):
```bash
git switch -c new-branch
```

### Legacy System Access

Log into the SAS server in Putty, then type:
```bash
/usr/bin/python3.6
```
then write your hello world program

### Windows Tools

```cmd
cd c:\program files\gnuwin32\bin
wget -m -A txt http://aleph.gutenberg.org/
```

## Package Management

### Requirements Generation

Determine requirements with pipreqs:
```cmd
PS C:\lab_new\edge_raider> pipreqs
INFO: Successfully saved requirements file in C:\lab_new\edge_raider\requirements.txt
```

Also using pip freeze:
```bash
pip freeze
```

## Python Decorators and Wrappers

### Wrapper Functions

A wrapper is a function with functions inside. That's it!
```python
def logdata():
	def print_header():
		print('Beginning status')
	def print_footer():
		print('Ending status')

	print_header()
	print('Processing...')
	print_footer()

logdata()
```

@ decorators are just pre-written (built-in?) wrappers.

## Class Utilities

### Class Name Access

You can get the name of an object's class as a string:
```python
class MyClass: pass
obj = MyClass()
obj.__class__.__name__
# 'MyClass'

# Functions have a similar feature:
def myfunc(): pass
myfunc.__name__
# 'myfunc'
```

### Class Diagram Generation

Make a class diagram from terminal:
```bash
pyreverse -o png -p pythony ./proof_of_work.py
```

## Miscellaneous Notes

- fintech. contains lines from before unit 5.1, and some lines from 11.3+
- Philosophical quote: "Before I had studied Chan for thirty years, I saw mountains as mountains, and rivers as rivers. When I arrived at a more intimate knowledge, I came to the point where I saw that mountains are not mountains, and rivers are not rivers. But now that I have got its very substance I am at rest. For it's just that I see mountains once again as mountains, and rivers once again as rivers."