# Classes

It is a blueprint or tepmlate for creating objects

To create a class,use the keyword class.

```py
class Car:
    #body
```

## Attributes

1. Class Attributes -Are variables that have same value for all class instance
2. Instance Attribues -Defined within .init() method.Its specific to particular instance of class.

```py

class Shape:
    shape ='Circle'# class attribute

    def __init__(self,radius){
        self.radius=radius # instance attribute
    }
```

## Methods

1. Class Method -Declared eith @Classmethod decorator
2. Instance method-Invoked by instance object
3. Static method-Declared with @staticmethod decorator

```py
class car:

    @classmethod
    function class(){

    }

    function(){

    }

    @staticmethod
    function(){

    }
```

## Modifiers

In Python, you can use different modifiers to control the access level of class attributes and methods. Here are the common modifiers:

1. Public: Accessible from anywhere.
2. Protected: Accessible within the class and its subclasses (conventionally prefixed with a single underscore _).
3. Private: Accessible only within the class (prefixed with double underscores __).

```py
class Shape:
    def __init__(self, value):
        self.value = value  # public attribute

    def public_method(self):
        return self.value  # public method

    def _protected_method(self):
        return self._value  # protected method

    def __private_method(self):
        return self.__value  # private method
```
