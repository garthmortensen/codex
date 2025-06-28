# py_basics.md

## Libraries

```python
from sklearn.ensemble import RandomForestClassifier
sklearn  # library
ensemble  # module
RandomForestClassifier  # class
```

## Basic Terminology

### Variables and Naming

In Java, you might use a leading underscore for attributes:
```python
# Java style
def fun1(_data, _val):
    ....
    ....

# Python style
def fun2(data, val):
    ....
    ....
```

A single underscore means the var/method is private, so `_data` should not be used by 3rd party apps. You'd often use this for variables only available within a class.

A double underscore (dunder) variable, `__data` is just an extra level of "don't use this from outside the class".

### Parameters vs Arguments

This is a parameter vs argument. Parameters are in function definitions, arguments are what you feed it:
```python
def myfunction(parameter1, parameter2):
    return parameter1 + parameter2

result = myfunction(argument1, argument2)
```

### Duck Typing

It's evaluated at runtime.
```
1 + 2
a + b
```
Its evaluated line by line, as opposed to the entire module compiled.

### C Python

interpreter = C python = python.exe
```bash
python()  # or python filename.py
quit()
```
Now you've closed the interpreter.

### Comments vs Docstring

`#` comments are by dev, for dev

`"""docstring"""` by dev for user. Available via __doc__ attribute. This is the interface documentation. Should have one for each module, function, class.

### Splats, Asterisk

Star/splat/asterisk (*) = any number of 0...n.
```python
# print(*objects, sep=' ', end='\n', ...)
print("hello", 34, "my name is ", name)
```

### Walrus Expressions

A walrus expression `:=` both assigns and evaluates.

Lore has it that Guido quit python development over walrus expressions.
```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

## Conditionals

Nested if statements with insurance premium predictor:
```python
accident = True
at_fault = False
accident_forgiveness = True
elite_status = True
increase_insurance_premium = True

# Insurance premium will increase. True or False?
# Nested Conditional Statements
if accident:
    if at_fault and accident_forgiveness:
        increase_insurance_premium = False
    elif at_fault and not accident_forgiveness and not elite_status:
        increase_insurance_premium = True
    else:
        increase_insurance_premium = False
elif not accident and elite_status:
    increase_insurance_premium = False
else:
    increase_insurance_premium = True

print(f"Prediction: {increase_insurance_premium}")
```

Ternary operator is a "backwards if":
```python
answer = 'is' if mytrip.is_round_trip() else 'is not'
```

## Loops

### Range Loops

```python
# Loop through a range of numbers (0 through 4)
for x in range(5):
    print(x)

# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
for x in range(2, 7):
    print(x)
```

### While Loops

Loop while input:
```python
# Loop while a condition is being met
run = "y"
while run == "y":
    print("Hi!")
    run = input("To run again. Enter 'y'")
```

Loop with increment:
```python
i = 1
while i < 6:
	print(i)
	i+=1
```

While true stoppable:
```python
uniform = True
while(uniform):
	# Ring up customers
```

Infinite loop:
```python
while True:
    print("hi")
```

While not loop:
```python
while not hash.startswith("00000000"):
    count += 1
    hash = hash_number(count)
```

### Breaks

```python
desired_number = 5
for x in range(10):
    if (x == desired_number):
	    break
    print(x)
```

### Different Looping Techniques

Different looping techniques, [i] and enumerate:
https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

```python
# 1/3 normal technique:
colors = ["red", "green", "blue", "purple"]
for color in colors:
    print(color)

# 2/3 c style loop. this style lets you print the index:
colors = ["red", "green", "blue", "purple"]
for i in range(len(colors)):
    print(colors[i])
    print(f"index: {i}")

# 3/3 enumerate function allows us to loop over a list and retrieve both the index and the value of each item in the list:
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))
```

### Pass

Using `pass` doesn't actually do anything. It just makes things syntactically correct. You could write pass pass pass. Simply, "do nothing".

## Functions

Return output, nicely said:
```python
def something(article):
    return output
result = something(crude_oil_articles)
```

List comprehension:
```python
coding_complete_pdf = [each + ".pdf" for each in coding_complete]
```

Multiline list comprehension:
```python
money_news_ids = [
    doc
    for doc in all_docs_id
    if categories[0] in reuters.categories(doc)
    or categories[1] in reuters.categories(doc)
]
# vs
money_news_ids = [ doc for doc in all_docs_id if categories[0] in reuters.categories(doc) or categories[1] in reuters.categories(doc)]
```

Dictionary comprehension:
```python
metrics = {k: v for k, v in zip(model.metrics_names, scores)}
```

### Docstring

`help(function)`

Some languages, including Python, have the idea of a "docstring." The idea of a docstring is pretty simple: If the first line of the function is a string, then the string is seen as the documentation for that function.

[Python's PEP 257](https://www.python.org/dev/peps/pep-0257/) ("Docstring conventions") suggests that docstrings should always be triple-quoted strings. Also, the closing triple quotes are on a line by themselves. This is considered to be optimal style in Python, in part so that Emacs can format the docstring.

Documentation for a function should indicate three things: (1) What it expects/requires as inputs, (2) what it modifies, and (3) what it returns. If you document all three of these for every function you write, you're way ahead of the game. Providing examples is just icing on the cake.

Docstrings and comments are aimed at completely different audiences. Comments should be written so that someone can debug, maintain, and improve your code. Docstrings are aimed at a much larger audience, and should thus make it easy for someone to understand what your function does, how to run it, and what it returns.

## Packages

6-20 in pdf LearningTree slides.

These are a directory of modules, which contain metadata (version, dependencies). Just a bunch of folders with modules.

The package directory must be within the search path (e.g. c:\course\files)
A common location is `site-packages`. The package directory must contain `__init__.py`.

site-packages dir = c:\python\python310 > Lib > site-packages

In PyCharm > New > Python Package - creates a package.

Each directory in the directory becomes its own namespace, where directory1.nested_directory, the "." becomes a qualified name.

## Scope

LEGB - local enclosing global builtin.
1. Local: within a function
2. Enclosing: within an enclosing function
3. Global: within the module or file
4. Built-in: within the Python builtin module

Python's namespace is a dictionary that it contains. You have a local dictionary, enclosing dictionary, global dictionary, builtin dictionary (LEGB). e.g.:

```python
var = 'global'
def fun1():
	var = 'enclosing'

	def fun2():
		var = 'local'
		print('enclosed var:', var)

	fun2()
	print('enclosing var:', var)

fun1()
print('global var:', var)
```

Output:
```
enclosed var: local
enclosing var: enclosing
global var: global
```

## Namespace and `__main__`

Examine the namespace with dir():
```python
dir()

import math
math.__name__

import this
this.__name__

for k, v in math.__dict__.items():
	print(k, "*****", v)
```

__name__ is equal to __main__ when a module is running as a standalone program. __name__ is equal to the module name when the module is imported. You can test this to conditionally execute module testing code, but only when the script isn't imported.

Create main_script.py:
```python
class Person:
    def __init__(self, name):
        self.name = name

def check_person():
    testname = 'Katrina'
    student = Person(testname)
    if student.name == testname:
        print('Person constructor ok')

if __name__ == '__main__':
    print("I am main, my name is", __name__)
    check_person()
else:
    print("I have been imported", __name__)
```

Output when run directly:
```
I am main, my name is __main__
Person constructor ok
```

main_importer.py:
```python
import main_script
```

Output when imported:
```
I have been imported main_script
```

To print all class attributes:
```python
vars(mycat)
# This is the same thing as:
mycat.__dict__
```

Use case:
```python
import airlineclasses

flight_data = (221, 'HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40', 399.99, 2)
flight_attributes = ('flightnum', 'departcity', 'arrivecity', 'departdaytime', 'arrivedaytime', 'cost', 'code')
data = dict(zip(flight_attributes, flight_data))
this_flight = airlineclasses.Flight(**data)
print("this_flight:", vars(this_flight))
```

Output:
```
this_flight: {'flightnum': 221, 'cost': 399.99, 'code': 2, 'departcity': 'HNL', 'arrivecity': 'HNL', 'departdaytime': '2022-01-03 08:30', 'arrivedaytime': '2022-01-03 15:40'}
```
