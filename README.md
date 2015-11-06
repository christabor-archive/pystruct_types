# python-structural-types
Structural type checking for Python.

## What is structural typing?
From [https://en.wikipedia.org/wiki/Structural_type_system](https://en.wikipedia.org/wiki/Structural_type_system):
"A structural type system (or property-based type system) is a major class of type system, in which type compatibility and equivalence are determined by the type's actual structure or definition, and not by other characteristics such as its name or place of declaration. Structural systems are used to determine if types are equivalent and whether a type is a subtype of another. It contrasts with nominative systems, where comparisons are based on the names of the types or explicit declarations, and duck typing, in which only the part of the structure accessed at runtime is checked for compatibility."

In typical python type checking, subclases are determined by name (nominal). This means they are referenced as subclasses by specifying the inheritence.
"""python
class FooParent:
    def bar():
        pass

class FooChild(FooParent):
    def foo():
        pass

p = FooParent()
c = FooChild()
assert isssubclass(p, c)  # True
"""

But this is not the case with a structural type system. The inheritence no longer applies. Instead, structure must match.

"""python
class FooParent(StructuralType):
    def bar():
        pass

class FooChild:
    def bar():
        pass

p = FooParent()
c = FooChild()
assert isssubclass(p, c)  # True
"""

## How is this achieved?
Using the magic of Python's overloading magic methods, a bit of abstract base classes, and the inspect module, I've devised a way to analyze the contents of any class and then compare it's properties and methods to another class, to determine if the structure is in fact identical.

## How to use
1. Import the module.
2. Register your class to it, like you would any Abstract Base Class. [Take a look at ABC's in Python](https://docs.python.org/2/library/abc.html) for some background.

"""python
struct.StructuralType.register(YourClass)
your_class_instance = YourClass()
"""

3. Use **issubclass** operator to check if things are structurally equivalent!
