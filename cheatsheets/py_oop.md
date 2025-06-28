# py_oop.md

## Core OOP Concepts

### Objects and Types

Object = instance of data. No declarations. Objects have "identifiers". We can derive 365 in different ways, but not all point to the same object. If nothing points to the object, garbage collector removes it.

```python
365
id(365)  # returns identifier

365 - 1  # not the same id
```

An object is a type. Built-in types accessible via `type()`. You pass an argument to a function. It returns a value. **Type constrains operations!**

```python
type(365)  # <class 'int'>
365 + 2  # creates new object, 367
```

If type constrains operations, you get TypeError.

A variable is a named reference to an object. It's the name tag that references the object. Variables don't contain things. They reference things! All variables are identifiers. Variables can vary. You can point to "cat" then "dog" using the same variable.

```python
count = 365
```

Because it's referenced, garbage collection won't destroy it. No reference? Garbage.

Immutable datatypes are read-only! Why make a copy of something that's immutable? Save memory.

```python
count = 365
num = count
num is count  # True
num = 2
num is count  # False
```

### OOP Fundamentals

OOP is about combining data and functionality. Manage it all in one place. You build tools (classes). Libraries contain classes. Classes contain methods and data.

**Inheritance** = is-a
**Composition** = has-a

### Encapsulation

Has-A. Class 'cruise' has a ship, a cabin, a cost. Attributes. Also, dine(), dance(), swim(). Methods.

Class templates are all about reusability. If you were to only use it once, no point to create classes. But reuse code? Class it.

When you instantiate a class, it calls the constructor:

```python
myvacation = Cruise(ship='Voyager', cabin=101)
# python translates the above into this:
myvacation = Cruise.__init__(myvacation, ship='Voyager', cabin=101)
```

Attributes are self.ship, self.cost, self.cabin. Parameters are what you pass to them. self.ship = ship. Typically, you name the parameters the same as the attributes. This makes position and keyword assignment easier.

Encapsulation should imply that all changes should be done through the class. So you'd need getters and setters/readers and writers. Python allows it either way. For large projects, it's better to do getters and setters. But Guido's design decision was to not require them, making it easier for the consumer. Easier access. E.g. you can just directly assign via `myvacation.ship = "USS Pony"`. Python is a cooperative atmosphere, trust based.

Methods can be categorized:
- static methods
- class methods  
- abstract methods
- instance methods - self

Methods are stored within class memory, not instance memory. myvacation.cost(), yourvacation.cost(), they all use the same cost(). Attributes, not so.

### Class Attributes

Class attributes go before __init__:

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

Class attribute vs instance (regular) attribute. Are we putting it on an instance, where each one has its own value? Or are we putting it on a class, where it's on the class.

How are class attributes used?
- If you have a value you'll be using throughout your class, and don't want to hardcode it, then use a class attribute and refer to it all the time.
- If you have a resource that's shared among instances. Take person.population...you don't want that outside the class as a variable (especially not a global variable), so you put it inside a class.

### Population Counter Example

```python
class Person(object):
    # class attributes
    population = 0  

    def __init__(self, name):
        Person.population += 1
        self.name = name
        
print(f"pop = {Person.population}")
p1 = Person("Mike")
p2 = Person("Like")
```

### Inheritance (Is-a)

If you can just add onto it using an existing class, *except for something*.

```python
class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

p1 = Person("Guido")
p1.greet()

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)  # gives me back object on which i can run init. self is automatically passed
        self.employee_id = employee_id

e1 = Employee("Guido", 13132)
e1.greet()
```

Inheritance helps us achieve DRY. Convertible inherits from sedan, which inherits from car, which inherits from vehicle. This forms a pine tree shape taxonomy.

### Polymorphism

A method tied to a specific type. You override inherited methods. AKA overloading.

```python
class VerbosePerson(Person):
    def greet(self):
        return f"Hello there {self.name}, how are you doing? That is great!"

v1 = VerbosePerson("Pony")
```

Example:
```python
a = 1
b = 2
print(a + b)  # 3

a = 1.1  # float
b = "hi"
print(a + b)  # TypeError
```

So, it's a function (and/or method?) which behaves differently depending on the argument's object type.

### Getting from Functional to OOP

Write down as an English paragraph what your script does.
- Pull out the nouns and verbs
- Some classes are entity classes - something that you store
- Some classes are regular classes
- There are control classes - Traffic cop, calls all classes in between

Good to have a conversation about it with someone else. UML is language agnostic. Start with English.

#### Summary

- class == type
- instance == object of type
- method = method within a type
- constructor = builds attributes

## Advanced OOP Concepts

### Reuven Object-oriented Python

What is an **object**?
1. It has a type (= "class")
2. It has attributes (data + functions)

Nearly everything in Python is an object.

What is a **type**? e.g. `str` or `dict`
1. A type is a factory for objects with predefined attributes
2. Attribute names are shared across all instances of that type
3. Attribute values, of course, can be different
4. Each instance can have custom attribute name-value pairs, as well

`type('abc')` = 'str'. This returns the class, which you can use to create other similar types.

`str(123)` = '123', creating a string. A string factory to create a string. Str is the maker. Int is a class, a maker, a factory. They create objects of that type. In python, classes are actually objects that can be passed around, used as arguments to functions, and do other things.

The type of every class is type. `type(Foo)` = type

**type is the factory's factory**. Every class's type is type. `type(type)` = type. Everything has a type.

Everything also has attributes.

```python
a  # identifier = name = variable or function...some sort of object
# python searches LEGB, first local, then look enclosing in function, then look global then look built-in.
a.b  # now we look for object a, but we search for the name/attribute 'b' inside the object a.
```

Now think of `a` as a namespace, a collection.

All objects in python, without exception have attributes. And attributes have attributes, etc.

```python
y = [10, 20, 30]
y.append(40)
# y is an attribute, that happens to be a method
```

`dir('abc')` to see what attributes exist, and also what data exists.

### Methods vs Functions

A method is "bound to an object." You access it via the dot operator. `stringy.upper()`

Many of the attributes are **methods**!

```python
a = 'abc'
a.upper()
```

Here, we're asking, do you have an attribute named upper? Yes. It turns out to be a method. We use parens to invoke/call the method, and we get back a new string. Methods are a particular type of attribute! Any time you see a dot in python, it means 'I'm looking for an attribute under the name on the right-side, in the object on the left-side.

Conversely...

```python
listy = [1, 2, 3, 4, 5]
sum(listy)  # = 15
```

This is a function.

The function exists as a variable. It's not an attribute - there's no `.something`. No dot before its name. `f` is searched through LEGB through python's various namespaces, and if it finds it, we get the function back.

**Some things cut across data types**, like `len()` and `sum()`. Rather than implement the same method on all the various datatypes, they decided to write a single function to apply to various objects.

### Get/Set Attributes

```python
import os
os.sep  # = '\\' bc Windows
os.sep = 'hahaha'
os.sep  # = 'hahaha'
```

We go into the module and access an attribute. You can change almost any object's attribute. It doesn't change it on disk, but it changes it in memory. What if the attribute doesn't exist? `os.mybutt = 'hurts'`. It works. We can set and get almost any attribute we want.

### Simple Class Creation

When you're talking about python, `type` and `class` are interchangeable. But not so when actually coding.

If we want to create a new type of data, we use `class` keyword.

```python
class Foo(object):  # in python3, object is optional. you don't need it.
    pass  # "i have nothing more to say here"

# the type of all classes, the type of all factories is type
type(Foo)  # = type

# create new integer object
int('123')

# create string object
str(123)

# create Foo object
Foo()

# capture the newly created object
a = Foo()
type(a)  # = __main__.Foo

# see what attributes there are
dir(Foo)
dir(a)
```

`Foo` is a class, and `a` is an instance of Foo. Both objects have types and both have attributes.

```python
vars(a)  # returns list of attributes we've added to a, that is, not inherited
```

### Constructor (__init__)

A special function that's invoked when the object is created. In python, this is `__init__`.

```python
class Foo(object):
    def __init__(self):  # self is required
        self.x = 100
        self.y = [10, 20, 30]

f = Foo()
vars(f)  # x = 100, y = [10, 20, 30]
g = Foo()
vars(g)  # x = 100, y = [10, 20, 30]
```

What is `__init__`? It's from Smalltalk programming language. In smalltalk, you created objects in 2 stages by creating the object with a method called `new`, then you add attributes to the object with something called `initialize`. Python does the same. `__new__` is actually called whenever we create a new object.

### Init with Parameters

The arguments x and y have nothing to do with self.x and self.y. Here, x and y are local variables. self.x and self.y are attributes on self. Take the local variable x and put it on the object as attribute x.

```python
class Foo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

f = Foo(10, 20)  # ok
```

If we go to use it like this:
```python
f = Foo()  # NOT ok - error missing positional arguments
```

So we can handle it this way:
```python
class Foo(object):
    def __init__(self, x=10, y=99):
        self.x = x
        self.y = y

f = Foo()  # ok
```

### Practical Examples

#### Computer Example

```python
# Old way - thinking at low level about dictionaries
computers = [
    {'brand': 'HP', 'year': 2021},
    {'brand': 'MS', 'year': 2019},
    {'brand': 'HP', 'year': 2015},
]

# New way - thinking at higher level about computers
class Computer(object):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c1 = Computer('HP', 2021)
c2 = Computer('MS', 2019)
c3 = Computer('HP', 2015)

computers = [c1, c2, c3]

for computer in computers:
    if computer.year == 2019:  # referencing attribute. No need to look up dict syntax
        print(f"the computer is brand {computer.brand} and year {computer.year}.")
```

#### Scoop and Bowl Example

```python
class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl(object):
    max_scoops = 3  # class attribute
    
    def __init__(self):
        self.scoops = []
    
    def add_scoops(self, *new_scoops):
        self.scoops += new_scoops[:Bowl.max_scoops - len(self.scoops)]
    
    def flavors(self):
        return ', '.join([one_scoop.flavor for one_scoop in self.scoops])
```

#### Bank Account Example

```python
class BankAccount(object):
    def __init__(self):
        self.transactions = []

class Person(object):
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, new_account):
        self.accounts.append(new_account)

    def balances(self):
        return [each_account.balance for each_account in self.accounts]
        
    def current_total_balance(self):
        return sum(sum([each_account.transactions for each_account in self.accounts]))
    
    def average_transaction_amount(self):
        all_transactions = [one_transaction
                           for one_account in self.accounts
                           for one_transaction in one_account.transactions]
        return sum(all_transactions) / len(all_transactions)
```

## @dataclass Decorator

Dataclasses create structured classes for storing data. They hold certain properties and functions to deal with data like a solidity struct.

```python
@dataclass
class Counter:
    count: int = 0

    def update_count(self):  # self gives the method access to all the class' variables (attributes)
        self.count = self.count + 1
```

Base functionality without @dataclass:

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

Same with @dataclass:

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

### Complex Dataclass Example

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List

@dataclass
class Block:
    data: Any  # allow string, lists, dicts, or other data classes
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):
        calculated_hash = block.hash_block()
        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):
            block.nonce += 1
            calculated_hash = block.hash_block()

        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]
```

## Utility Functions

You can get the name of an object's class as a string:

```python
class MyClass: 
    pass

obj = MyClass()
obj.__class__.__name__  # 'MyClass'

# Functions have a similar feature:
def myfunc(): 
    pass

myfunc.__name__  # 'myfunc'
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

## See All Methods

```python
listy = [1, 3]
dir(listy)

stringy = "hi"
dir(stringy)
```

## Class Diagram Generation

Make a class diagram from terminal:

```bash
pyreverse -o png -p pythony ./proof_of_work.py
```