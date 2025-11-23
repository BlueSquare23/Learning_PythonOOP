# Learning Object Oriented Python3

## Overview

I've hit a wall with what I can achieve using standard python procedural
programming patterns. I need to evolve and I need a refresher on Python OOP
stuff.

I'm at the point where I need to start using factories and constructors and
learn more about design patterns. But still a bit handicapped by basic python
oop stuff. So need to practice.

Based on [this FreeCodeCamp video](https://www.youtube.com/watch?v=Ej_02ICOIgs)

Using bpython as the shell for following along with examples.

## Getting Started with Classes

Basic class

```python3

class Item:
    pass

item1 = Item()
item2 = Item()
```

Classes can have attributes.

```python3
class Item:
    pass

item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 4

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
```

Classes also have methods. You probably also know about some builtin methods in
python like string methods.

```python3
mystr = "aaaaaaa"
print(mystr.upper())
```

When we build a class, we can make our own custom methods.

Methods are just functions that live inside of a class.

Methods always take the object it`self` as first argument.

```python3
class Item:

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 4
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
print(item1.calculate_total_price(item2.price, item2.quantity))

```

As you can see methods take parameters and return results.

### Constructor Method `__init__`

The code above was for demonstration purposes but it sucks.

In reality what we should do when creating a class is define our constructor
method. In python this method is named `__init__` and its responsible for the
initial bit of code that get's run when first creating our object.

```python3
class Item:

    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

iphone_order = Item('iPhone', 100, 4)
print(iphone_order.calculate_total_price())

macbook_order = Item('macbook', 1000, 3)
print(macbook_order.calculate_total_price())
```

> Note: In general in python these sorts of special builtin methods are called
> "dunder" (double underscore) or "magic methods." And we can define lots of
> them to control very interesting object/class behaviors.

You can see with the `__init__` method we're able to refactor our code quite a bit.

Now we can set the object's attributes right when we create it and we can then
also use those attributes in our method without having to pass them in
directly.

We can also see we've set default quantity to zero in the `__init__` method
because we want it that way.

### Typing

Python is a dynamically typed language, meaning a variable's type is checked at
runtime (not compile time). This means we don't have to set a variable type in
python when initializing. That type will be set "implicitly" and determined by
the type of data the variable holds.

However, python does have optional typing that can be applied to function and
method definitions. This serves more as a programmers aid, helping fellow
coders know what type of data to pass to your function / method.

This falls under "best practices" so let's apply some typing to our Item class.

```python3
class Item:

    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

# iphone_order = Item('iPhone', 100, "4")  # Throws error because expects type int for quantity.

iphone_order = Item('iPhone', 100, 4)
print(iphone_order.calculate_total_price())

macbook_order = Item('macbook', 1000, 3)
print(macbook_order.calculate_total_price())
```

### Assert Validation

We can add some assert statements before our assignments to use as validation.

These assert statements will throw an exception and display our custom message
in the event either the price or quantity is passed in as a negative number.

```python3
class Item:

    def __init__(self, name: str, price: float, quantity=0):
        # Validate args
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # Assign args
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

#iphone_order = Item('iPhone', 100, -4)  # Throws and AssertionError and displays our message

iphone_order = Item('iPhone', 100, 4)
print(iphone_order.calculate_total_price())

macbook_order = Item('macbook', 1000, 3)
print(macbook_order.calculate_total_price())
```

### Class Attributes

These are shared attributes that are the same across all instances of the
class. These attributes belong to the class itself (hence the name), but they
can also be accessed by any individual instance / object.

In our case here we're going to apply a 20% discount to all Items in the store.

```python3
class Item:
    discount = .2

    def __init__(self, name: str, price: float, quantity=0):
        # Validate args
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # Assign args
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return (self.price * self.quantity) * (1 - Item.discount)

iphone_order = Item('iPhone', 100, 4)
print(iphone_order.calculate_total_price())

macbook_order = Item('macbook', 1000, 3)
print(macbook_order.calculate_total_price())

# Further listing class vs instance level attirbutes.
print(Item.__dict__)
print(iphone_order.__dict__)
```

As you can see we set our discount to .2 (aka 20%). Then at price cacl time we
apply the discounted rate using the class attribute. This will ensure no matter
what the item quantity or price is, we will have the same discount across them
all.

In the case of the discount, we do not export that and don't allow callers of
our method to use set that discount rate, because we want the class itself to
enforce what that rate is globally.

#### Exploring Class Vs Instance Attributes Using `__dict__`

When it comes to exploring class level attributes vs instance level attributes,
we can print the `__dict__` method for each to get a better understanding. The
`__dict__` method will automatically convert all the data in our class or
object into a dictionary for easier viewing of the whole thing.

Here we can see our `discount` class level attribute when printing the Classes dict:

```
>>> print(Item.__dict__)
{'__module__': '__main__', 'discount': 0.2, '__init__': <function Item.__init__ at 0x7f3f2ea3eb00>, 'calculate_total_price': <function Item.calculate_total_price at 0x7f3f2ea3ee60>, '__dict__': <attribute '__dict_
_' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
```

And then here we can see the instance specific vars when printing our `iphone_order` object's dict.

```
>>> print(iphone_order.__dict__)
{'name': 'iPhone', 'price': 100, 'quantity': 4}
```

### Getting All Instances

Now that we know about class level variables, let's use one to store a list of
all Item object we create. This will come in handy later on.

```python3
class Item:
    discount = .2
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validate args
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # Assign args
        self.name = name
        self.price = price
        self.quantity = quantity

        # Do needful...
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.calculate_total_price() * (1 - Item.discount)


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
```

As you can see we just make a class level list named `all` and then we go ahead
and append newly instanced item objects to the class level list. Then at the
end after creating some items, we can go ahead and print the class level all
var to get our list.

### Defining A `__repr__` Method

The `__repr__` allows us to print a string representation of our data. The
`__repr__` prints debug / development related information. Much more detailed.
There's a similar magic method called `__str__` which also is meant to print a
string representation of the objects data, however `__str__` is meant to be
user facing, whereas `__repr__` is more for developers.

```python3
class Item:
    discount = .2
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validate args
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # Assign args
        self.name = name
        self.price = price
        self.quantity = quantity

        # Do needful...
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.calculate_total_price() * (1 - Item.discount)

    # Best practice is for repr to print items in same format as they're instantiated.
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
```

Now with our `__repr__` method defined we get a much nicer looking list when we
go to print things out.

```
>>> print(Item.all)
[Item('Phone', '100', '1'), Item('Laptop', '1000', '3'), Item('Cable', '10', '5'), Item('Mouse', '50', '5'), Item('Keyboard', '75', '5')]
```

### Class Methods

Moving forward we're going to store our data in a csv file for ease of use.

* `items.csv`

```csv
name,price,quantity
"Phone",100,1
"Laptop",1000,3
"Cable",10,5
"Mouse",50,5
"Keyboard",75,5
```

With a class level method, (like a class level attribute) we don't have a given
object to use to call the method through. Instead by exporting that method to
the class level, when we call it we just use the class name directly.

We can use the special `@classmethod` decorator to make our method a class
method. Likewise with class methods, instead of passing `self` we pass `cls`
because with a class method, its the class itself that is passed as first
argument to our class method.

```python3
import csv

class Item:
    discount = .2
    all = []

    # Class level methods
    # Creates objects from csv data
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )

    def __init__(self, name: str, price: float, quantity=0):
        # Validate args
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # Assign args
        self.name = name
        self.price = price
        self.quantity = quantity

        # Do needful...
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.calculate_total_price() * (1 - Item.discount)

    # Best practice is for repr to print items in same format as they're instantiated.
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


Item.instantiate_from_csv()

print(Item.all)

```

When we call the class method we can see it prints all our items as
dictionaries. We then stuff all those item dictionaries into and instantiate
them as Item objects.

From bpython shell:

```
{'name': 'Phone', 'price': '100', 'quantity': '1'}
{'name': 'Laptop', 'price': '1000', 'quantity': '3'}
{'name': 'Cable', 'price': '10', 'quantity': '5'}
{'name': 'Mouse', 'price': '50', 'quantity': '5'}
{'name': 'Keyboard', 'price': '75', 'quantity': '5'}
[Item('Phone', '100.0', '1.0'), Item('Laptop', '1000.0', '3.0'), Item('Cable', '10.0', '5.0'), Item('Mouse', '50.0', '5.0'), Item('Keyboard', '75.0', '5.0')]

```

### Static Methods

Static methods are similar to class methods in a few ways. One being that we
use a decorator `@staticmethod` to denote its a static method. Another being it
is scoped to the entire class not the individual instances/objects.

The main difference is that a static method does not take its own class as an
argument. Instead it is just like a function outside of the class where there
is no default first parameter passed to the static method. 

```python3
import csv

class Item:
    discount = .2
    all = []

    # Class level methods
    # Creates objects from csv data
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # Counts 1.0 as int, 1.1 as not int.
        if isinstance(num, float):
            # builtin .is_integer returns True if the float has no fractional part (e.g., 5.0, 10.0).
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __init__(self, name: str, price: float, quantity=0):
        # Validate args
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # Assign args
        self.name = name
        self.price = price
        self.quantity = quantity

        # Do needful...
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.calculate_total_price() * (1 - Item.discount)

    # Best practice is for repr to print items in same format as they're instantiated.
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


Item.instantiate_from_csv()

print(Item.is_integer('fart'))
print(Item.is_integer(1.0))
print(Item.is_integer(15.0))
print(Item.is_integer(15.7))
```

Returns 
```
False
True
True
False
```

### Inheritance

Say we want to have multiple types of items in our fake store. Some of them are
Phones, some of them are Laptops, etc.

Rather than create three very similar classes with lots of duplicate code, what
we can do instead is create a base class for Item and then extend it with
different more specific type of items class that inherits attributes and
methods from the base class.

In python they use the terms "Parent" and "Child" to refer to the relationship
between classes that related via inheritance.

```python3
import csv

class Item:
    discount = .2
    all = []

    # Class level methods
    # Creates objects from csv data
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # Counts 1.0 as int, 1.1 as not int.
        if isinstance(num, float):
            # builtin .is_integer returns True if the float has no fractional part (e.g., 5.0, 10.0).
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __init__(self, name: str, price: float, quantity=0):
        # Validate args
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # Assign args
        self.name = name
        self.price = price
        self.quantity = quantity

        # Do needful...
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.calculate_total_price() * (1 - Item.discount)

    # Best practice is for repr to print items in same format as they're instantiated.
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )

        # Validate args
        assert broken_phones >= 0, f"Broken Phones {broken_phones} cannot be negative"

        # Assign args
        self.broken_phones = broken_phones


item1 = Item("Laptop", 1000, 2)
phone1 = Phone("iPhone10", 500, 5, 1)
print(phone1.apply_discount())
phone2 = Phone("iPhone13", 700, 5, 1)

print(Item.all)
print(Phone.all)
```





