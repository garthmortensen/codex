# regex.md

## Basic Patterns

```bash
.                           # Any character except newline
^                           # Start of string
$                           # End of string
*                           # 0 or more of preceding
+                           # 1 or more of preceding
?                           # 0 or 1 of preceding
{n}                         # Exactly n occurrences
{n,m}                       # Between n and m occurrences
```

## Character Classes

```bash
[abc]                       # Any of a, b, or c
[a-z]                       # Any lowercase letter
[A-Z]                       # Any uppercase letter
[0-9]                       # Any digit
[^abc]                      # Not a, b, or c
\d                          # Any digit [0-9]
\w                          # Any word character [a-zA-Z0-9_]
\s                          # Any whitespace
```

## Common Patterns

```bash
# Email validation
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

# Phone number (US format)
^\(\d{3}\) \d{3}-\d{4}$

# IP address
^(\d{1,3}\.){3}\d{1,3}$

# Date (YYYY-MM-DD)
^\d{4}-\d{2}-\d{2}$

# URL
^https?://[^\s/$.?#].[^\s]*$
```

## Python Regex

```python
import re

# Basic operations
re.search(pattern, text)     # Find first match
re.findall(pattern, text)    # Find all matches
re.sub(pattern, repl, text)  # Replace matches

# Compiled patterns
pattern = re.compile(r'\d+')
pattern.findall(text)

# Groups
match = re.search(r'(\d+)-(\d+)', '123-456')
match.group(1)               # First group: '123'
match.groups()               # All groups: ('123', '456')
```

## Data Cleaning Examples

```python
# Extract numbers from text
numbers = re.findall(r'\d+\.?\d*', text)

# Clean phone numbers
clean_phone = re.sub(r'[^\d]', '', phone_number)

# Extract email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Split on multiple delimiters
parts = re.split(r'[,;]', text)
```