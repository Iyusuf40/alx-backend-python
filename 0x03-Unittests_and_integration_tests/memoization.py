#!/bin/python3

from functools import wraps
from typing import Callable
import time

def memoize(fn: Callable) -> Callable:
    @wraps(fn)
    def memoized(self, val):
        """"memoized wraps"""
        attr_name = "_{}".format(fn.__name__ + str(val))
        try:
            getattr(self, attr_name)
        except:
            setattr(self, attr_name, fn(self, val))
        return getattr(self, attr_name)

    return memoized
    
class MyClass:
    @memoize
    def a_method(self, arg):
        print(f"a_method does really complicated stuff with {arg}")
        time.sleep(3)
        return arg
my_object = MyClass()
print(my_object.a_method(32))
print(my_object.a_method(32))
print(my_object.a_method(32))
print(my_object.a_method(32))
print(my_object.a_method(72))

print("\n")

def memoize2(fn: Callable) -> Callable:
    save_self = None
    @wraps(fn)
    def memoized2(self):
        """"memoized wraps"""
        def cpu_intensiv_func(self, val):
            attr_name = "_{}".format(fn.__name__ + str(val))
            try:
                getattr(self, attr_name)
            except:
                print(f"doing really complex stuff with{val}")
                setattr(self, attr_name, val)
                time.sleep(3)
            return getattr(self, attr_name)
        
        try:
            getattr(self, "func")
        except:
            setattr(self, "func", cpu_intensiv_func)
        return getattr(self, "func")
    return property(memoized2)
    
class MyClass2:
    @memoize2
    def a_method(self):
        print(f"a_method does really complicated stuff with {arg}")
        return arg
my_object = MyClass2()
print(my_object.a_method)
print(my_object.a_method(my_object, 32))
print(my_object.a_method(my_object, 32))
print(my_object.a_method(my_object, 32))
print(my_object.a_method(my_object, 32))
print(my_object.a_method(my_object, 72))
