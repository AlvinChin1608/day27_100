# day27_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

-------------------------

# Advanced Python Arguments: *args and **kwargs
In Python, functions are highly versatile and allow for flexible parameter passing. Two powerful features that enable this flexibility are __*args__ and __**kwargs__. These constructs allow functions to accept an arbitrary number of positional and keyword arguments, respectively.

__*args__
The *args syntax allows a function to accept any number of positional arguments. The arguments are passed into the function as a tuple.
```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```
In this example, the __sum_all__ function can accept any number of positional arguments and sum them up. The __*args__ collects the arguments into a tuple, allowing the function to iterate over them.

__**kwargs__
The __**kwargs__ syntax allows a function to accept any number of keyword arguments. The arguments are passed into the function as a dictionary.
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, job="Engineer")
```
Output
```python
name: Alice
age: 30
job: Engineer
```
In this example, the __print_info__ function can accept any number of keyword arguments. The __**kwargs__ collects the arguments into a dictionary, allowing the function to iterate over the key-value pairs.

Combining __*args__ and __**kwargs__
You can use both __*args__ and __**kwargs__ in the same function definition to accept both positional and keyword arguments.

Example:
```python
def mixed_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mixed_args(1, 2, 3, name="Alice", age=30)
```
Output
```python
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 30}
```
In this example, the __mixed_args__ function accepts both positional and keyword arguments. The __*args__ collects positional arguments into a tuple, and the __**kwargs__ collects keyword arguments into a dictionary.

__Practical Use Cases__
__1. Wrapper Functions:__
When creating decorators, __*args__ and __**kwargs__ are commonly used to ensure that the wrapper function can accept any arguments that the decorated function might receive.
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@decorator
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
```
__2. Flexible APIs:__
Functions that need to handle a variable number of inputs or provide a flexible API can leverage __*args__ and __**kwargs__.
```python
def flexible_function(required_arg, *args, **kwargs):
    print(f"Required argument: {required_arg}")
    if args:
        print("Additional positional arguments:", args)
    if kwargs:
        print("Additional keyword arguments:", kwargs)

flexible_function("Mandatory", 1, 2, 3, key1="value1", key2="value2")
```







