"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/JeremySimon826/lab10-JS-HK.git

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a+b

def subtract(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if a!=0:
        return b/a
    else:
        raise ZeroDivisionError

def logarithm(a, b):
    if a>0 and b>0 and a!=1:
        return math.log(b,a)
    else:
        raise ValueError

def exp(a,b):
    return a**b

