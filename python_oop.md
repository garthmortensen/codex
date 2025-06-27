# python_oop.md

## OOP Concepts

OOP is about combining data and functionality. Manage it all in one place. You build tools (classes). Libraries contain classes. Classes contain methods and data.

Inheritance = is-a
Composition = has-a

### Objects

object = instance of data. no declarations. objects have "identifiers". We can derive 365 in diff ways, but not all point to the same object. If nothing points to the object, garbage collector removes it.
```python
365
id(365)  # returns identifier

365 - 1  # not the same id
```

An object is a type. Built-in types accessible via `type()`. You pass an argument to a function. It returns a value. **Type constrains operations!** 
```python
type(365)  # <class 'Int'>
365 + 2  # creates new object, 367
```
If type constrains operations, you get TypeError.

A variable is a named reference to an object. It's the name tag that references the object. Variables don't contain things. They reference things! All variables are identifiers. Variables can vary. You can point to "cat" then "dog" using the same variable.
```python
count = 365
```
Because is referenced, garbage collection won't destroy it. No reference? Garbage.

Immutable datatypes are read-only! Why make a copy of something is immutable? Save memory. 
```python
count = 365
num = count
num is count  # true
num = 2
num is count  # false
```

### Wrapper

A wrapper is a function with functions inside. That's it!
```python
def logdata():
	def print_header():
		print(Beginning status')
	def print_footer():
	print('Ending status')

	print_header()
	print(Processing...')
	print_footer()

logdata()
```

@ decorators are just pre-written (built-in?) wrappers.

## Classes

``` python
function()
type(df) # is a function

class.method()  # a function which belongs to a class
df.corr() # is a method, bc its attached to the df class. using dot = method

class.attribute  # a property of that class
df.shape # is a attribute, attached to a class  # a class can store multiple variables, known as attributes
```

see all methods
``` python
listy = [1, 3]
dir(listy)
stringy = "hi"
dir(stringy)
```

make a class diagram from terminal
``` bash
pyreverse -o png -p pythony ./proof_of_work.py
```

### @dataclass

dataclasses create structured classes for storing data.
they hold certain properties and functions to deal with data
like a solidity struct

``` python
@dataclass
class Counter:  # # this will record a count for us
    count: int = 0
    # # classes can have functions, aka "methods". They perform actions

    def update_count(self): # # self? gives the method access to all the class' variables (attributes)
        self.count = self.count + 1  # # accessing count
```

Another example:

Base functionality:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
```

`__init__` to initialize the point, `__repr__` to provide a human-readable representation of the point, and `__eq__` to allow comparison of two points.

Now the same, with `@dataclass`:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

Decorator automatically adds `__init__`, `__repr__`, `__eq__` based on the class attributes (`x`, `y`). 

Usage:

```python
# create a new point
p1 = Point(1, 2)
print(p1)  # outputs: Point(x=1, y=2)

# create another point
p2 = Point(1, 2)
print(p1 == p2)  # outputs: True, bc x and y are the same in p1 and p2
```

In summary, `@dataclass` simplifies code, without losing functionality.

class with method
18-Blockchain\3\Activities\03-Evr_Proof_of_Work\Solved\proof_of_work.py

``` python
@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4  # # new

    def proof_of_work(self, block):
        calculated_hash = block.hash_block()  # Block method

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):
            block.nonce += 1
            calculated_hash = block.hash_block()  # Block method

        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

set a class attribute
difficulty = 4
pychain.difficulty = difficulty  # # connect slider input back to PyChain class
```

class with attributes, with starting values
create dataclass
``` python
from dataclasses import dataclass
from datetime import datetime
from typing import Any
@dataclass  ## @decorator = modifier to add functionality to the Block object. @dataclass is used to make structured classes specialized for storing data. decorators tell python about whats to come nextclass Block:  ## the Uppercased class name is Block. looks like def function!
    ## define the data names and types to be stored in this container
    ## attribute: type
    data: Any  ## allow string, lists, dicts, or other data classes
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")  ## universal timing for truely relative time compare
```

You can get the name of an object's class as a string:
``` python
class MyClass: pass
obj = MyClass()
obj.__class__.__name__
'MyClass'
Functions have a
similar feature:
def myfunc(): pass
myfunc.__name__
'myfunc'
```

To print all class attributes, 
`vars(mycat)`
This is the same thing as:
`mycat.__dict__`
Use case:
```python
import airlineclasses

flight_data = (221, 'HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40', 399.99, 2)
flight_attributes = ('flightnum', 'departcity', 'arrivecity', 'departdaytime', 'arrivedaytime', 'cost', 'code')
data = dict(zip(flight_attributes, flight_data))
this_flight = airlineclasses.Flight(**data)
print("this_flight:", vars(this_flight))
```
> this_flight: {'flightnum': 221, 'cost': 399.99, 'code': 2, 'departcity': 'HNL', 'arrivecity': 'HNL', 'departdaytime': '2022-01-03 08:30', 'arrivedaytime': '2022-01-03 15:40'}

## OOP LearningTree

### Encapsulation

Has-A. Class 'cruise' has a ship, a cabin, a cost. Attributes. Also, dine(), dance(), swim(). Methods.

Class templates are all about reusability. If you were to only use it once, no point to create classes. But reuse code? Class it.

When you instantiate a class, it calls the constructor.
```python
myvacation = Cruise(ship='Voyager', cabin=101)
# python translates the above into this:
myvacation = Cruise.__init__(myvacation, ship='Voyage", cabin=101)
```
Attributes are self.ship, self.cost, self.cabin. Parameters are what you pass to them. self.ship = ship. Typically, you name the parameters the same as the attributes. This makes position and keyword assignment easier.

Encapsulation should imply that all changes should be done through the class. So you'd need getters and setters/readers and writers. Python allows it either way. For large projects, it's better to do getters and setters. But Guido's design decision was to not require them, making it easier for the consumer. Easier access. E.g. you can just directly assign via `myvacation.ship = "USS Pony"`. Python is a cooperative atmosphere, trust based.

Methods can be categorized:
- static methods
- class methods
- abstract methods
- instance methods - self
Methods are stored within class memory, not instance memory. myvacation.cost(), yourvacation.cost(), they all use the same cost(). Attributes, not so.

Class attributes. These go before __init__.
```python
class Cruise:

	# class attributes
	premiumcabins = (101, 102, 105, 106, 109, 110)

	def __init__(self, ship=None, cost=0.0, cabin=0):
		self.ship = ship
		self.cost = cost
		self.cabin = cabin
		self.charge_upgrade()

	def charge_upgrade(self):
		if self.cabin in Cruise.premiumcabins:
		self.cost += 50.0

myvacation = Cruise(ship='Voyager', cabin=101)
print(myvacation.cost)
```

### Inheritance
Is-A

A convertible is a specialized sedan, which is a specialized car, which is a specialized vehicle.

Inheritance helps us achieve DRY. Converible inherits from sedan, which inherits from cars, which inherits from vehicle. This forms a pine tree shape taxonomy.

super().whatevs

### Polymorphism

A method tied to a specific type. You override inherited methods. AKA overloading.

### How to get from functional to OOP?
Write down as an English paragraph what your script does.
pull out the nouns and verbs
some classes are entity class. something that you store.
some classes are regular classes.
there are control classes. Traffic cop, calls all classes in between.

Good to have a conversation about it with someone else
extraction() - what does this json object do? it contains things, points to things.

UML is language agnostic. 

Start with English.

### Summary

class == type
instance == object of type
method = method within a type
constructor = builds attributes

## [Rueven Object-oriented Python](https://store.lerner.co.il/view/courses/object-oriented-python)

What is an **object**?

1. It has a type ( = "class")
2. It has attributes (data + functions)

Nearly everything in Python is an object. 

What is a **type**? e.g. `str` or `dict`

1. A type is a factory for objects with predefined attributes
2. Attribute names are shared across all instances of that type
3. Attribute values, of course, can be different
4. Each instance can have custom attribute name-value pairs, as well

`type('abc')`  = 'str'. This returns the class, which you can use to create other similar types.

You can use a class 

`str(123)` = '123', creating a string. A string factory to create a string. Str is the maker. Int is a class, a maker, a factory. They create objects of that type. In python, classes are actually objects that can be passed around, used as arguments to functions, and do other things.

The type of every class is type. `type(list)` = type. `type(str)` = type. Type is a factory maker. It makes classes. 

**type is the factory's factory**. Every class's type is type. `type(type)` = type. Everything has a type.

Everything also has attributes.

```py
a  # identifier = name = variable or function...some sort of object
# python searches LEGB, first local, then look enclosing in function, then look global then look built-in.
a.b  # now we look for object a, but we search for the name/attribute 'b' inside the object a.
```

Now think of `a` as a namespace, a collection.

All objects in python, without exception have attributes. and attributes have attributes, etc.

```py
y = [10, 20, 30]
y.append(40)
# y is an attribute, that happens to be a method
```

`dir('abc')` to see what attributes exist, and also what data exists.

### Methods

A method is "bound to an object." You access it via the dot operator. `stringy.upper()` ~LearningTree

Many of the attributes are **methods**! 

```py
a = 'abc'
a.upper()
```

Here, we're asking, do you have an attribute named upper? Yes. It turns out to be a method. We use parens to invoke/call the method, and we get back a new string. Methods are a particular type of attribute! Any time you see a dot in python, it means 'I'm looking for an attribute under the name on the right-side, in the object on the left-side.

Conversely...

```py
listy = [1, 2, 3, 4, 5]
sum(listy)  # = 15
```

This is a function. 

```py
f(x)  # f of x
```

The function exists as a variable. It's not an attribute - there's no `.something`. No dot before it's name. `f` is searched through LEGB through python's various namespaces, and if it finds it, we get the function back. So why can't we write `listy.sum()`?

```py
listy.pop()
# 5
listy  # = [1, 2, 3, 4]

# methods use syntax o.m(x) = object.method(x)
# or o.m()
```

We can invoke a function, and also can invoke a method. So when should we be using which? 

Why isn't everything in python a method? Especially so given `len(x)`? 

Some historical, some aesthetic, some design decisions. They are baked in forever. Almost everything is a method though. `o.m(x)`. 

**Some things cut across data types**, like `len()` and `sum()`. Rather than implement the same method on all the various datatypes, they decided to write a single function to apply to various objects. It seems to work. How to know whether to try a function or a method? Always try the method first. 

`dir(listy)` will return both data and methods, but also private stuff. Try less technical. `help(list)` returns docstring on list. 

**It's like verbs and irregular verbs**. Just gotta get used to them.

### Get/Set attributes

```py
import os
os.sep  # = '\\ bc Windows'
os.sep = 'hahaha'
os.sep  # = 'hahaha'
```

We go into the module and access an attribute. You can change almost any object's attribute. It doesn't change it on disk, but it changes it in memory. Reload the memory to reset. What if the attribute doesn't exist? `os.mybutt = 'hurts'`. It works. We can set and get almost any attribute we want. Remember that every object is a type and every object has attributes. Knowing how to set/get attributes will make life easier.  

### Simple class

When you're talking about python, `type` and `class` are interchangeable. But not so when actually coding.

If we want to create a new type of data, we use `class` keyword. 

```py
class Foo(object):  # in python3, object is optional. you dont need it.
    pass  # "i have nothing more to say here"

# the type of all classes, the type of all factories is type
type(Foo)  # = type

# create new integar object
int('123')

# create string object
str(123)

# create Foo object
Foo()

# capture the newly create object
a = Foo()
type(f)  # = __main__.Foo  # what type of object is this? Foo.

# see what attributes there are
dir(Foo)
# ...
# ...
# ...
# many built in attributes that were inherited
dir(f)
# returns mostly the same things
```

`Foo` is a class, and `f` is an instance of Foo. Both objects have types and both have attributes.

Let's add some attributes.

```py
f = Foo()
vars()  # returns globals() = list of global vars
def bars():
    vars()  # returns locals() = list of local vars

vars(f)  # returns list of attributes we've added to f, that is, not inherited
```

So let's edit this.

```py
f.x = 100
f.y = [1, 2, 3]

dir(f)  # returns many attributes, inluding x and y!
vars(f)  # returns ONLY x and y!
```

So you've created an instance of Foo. Don't do this though, it is bad form.

```py
g = Foo()
g.a = 'cat'
g.x = 'dog'
```

You've just created something of the same class, but different attributes. Gross.

### Constructor

A special function that's invoked when the object is created. In python, this is `__init__`.

Attributes are something that exists on an object. 

```py
class Foo(object):
    def __init__(self);  # self is required
    	self.x = 100
        self.y = [10, 20, 30]

f = Foo()
vars(f)  # x = 100, y = [10. 20, 30]
g = Foo()
vars(g)  # x = 100, y = [10. 20, 30]
```

Above, the behavior is consistent. 

What is `__init__` ? It's from Smalltalk programming language. In smalltalk, you created objects in 2 stages by creating the object with a method called `new`, then you add attributes to the object with something called `initialize`. Python does the same. `__new__` is actually called whenever we create a new object. 

So, after we create a new object of type Foo, it then looks for `__init__` and if it exists, it says "hey, init, please go and add attributes to the object." And if there is no init? Then no attributes need to be added. 

`__ini__` gets one arguement, `self`. Many other languages (C++) use the keyword `this`. It means "this is the current object", then you do things with that current object. Roughly, this is `self`, which comes from Smalltalk. In python though, `self` is convention. You could call it whatever you want, like `this`, but 99.99% people use `self`. IDEs color it automatically. `self` is the instance of Foo. 

```py
f = Foo()
# when you run that line, here are the steps:
# 1
# Foo() calls foo, calls the class
# 2
# this invokes the new method, __new__, which creates the new object
# 3
# __new__ calls __init__. 
# __new__: "Hey init, this is your chance to add attributes to the object"
# __init__: what object?
# This is why you include param self. it points init to it
# 4
# init runs 
# self.x = 100
# self.y = [10, 20, 30]
```

### Init and parameters

The arguments x and y have nothing to do with self.x and self.y. Here, x and y are local variables. self.x and self.y are attributes on self. Take the local variable x and put it on the object as attribute x.

```py
class Foo(object):
    def __init__(self, x, y);
    	self.x = x
        self.y = y

f = Foo(10, 20)  # ok
```

If we go to use it like this:

```py
f = Foo()  # NOT ok
# error missing positional arguments
```

So we can handle it this way:

```py
class Foo(object):
    def __init__(self, x=10, y=99);
    	self.x = x
        self.y = y

f = Foo()  # ok
```

Let's look at *args.

```py
class Foo(object):
    def __init__(self, x, *args);
    	self.x = x
        self.args = args

f = Foo(10, 20, 30, 40)  # ok
vars(f)
# x = 10, args = [20. 30, 40]
```

Interesting. He calls * a "splat". Like a fly splatted on wall. Googling shows that "**splat args**" are from Ruby. where you take many arguments and convert to an array.

### Thinking in OOP way

So let's do something perfectly fine. Let's define all of our computers.

```py
computers = [
    		{'brand': 'HP', 'year': 2021},
    		{'brand': 'MS', 'year': 2019},
    		{'brand': 'HP', 'year': 2015},
			]
```

We can do some operations here, such as a loop.

```python
for computer in computers:
    if computer['year'] = 2019:
        print(f"the computer is brand {brand} and year {year}.")
```

But here we're thinking at a low level. We're thinking about dictionaries. Let's think at a higher level.

```python
class Computer(object):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c1 = Computer('HP', 2021)
c2 = Computer('MS', 2019)
c3 = Computer('HP', 2015)

computers = [c1, c2, c3]  # ez

for computer in computers
    if computer.year = 2019:  # referencing attribute. No need to look up dict syntax
        print(f"the computer is brand {computer.brand} and year {computer.year}.")
```

Technically, these are the same. Semantically, it's an improvement. You don't have to think in terms of dictionaries. You want to think about computers, at a higher level. You can always add whatever attributes you need.

### Polymorphism

https://www.stechies.com/polymorphism-inheritance-python/
```python
a = 1
b = 2
print(a + b)  # 3

a = 1.1  # float
b = "hi"
print(a + b)  # TypeError
```
So, it's a function (and/or method?) which behaves differently depending on the argument's object type. Seems like you could say "type checking" here. But it's also about classes. Many different classes, which can use the same methods? Or is that inheritance???

### Constructor

The name of the method is the same as the object. if i initialize this object, here are the values i set when we start

It's an optional function declared with the constructor keyword which is executed upon contract creation, and where you can run contract initialization code. Quickly customize code with your own initial values.
...quickly customize code with your own initial values
...using the constructor simplifies the process of creating custom versions of the ERC20Detailed contract
...we pass initial values to the contract