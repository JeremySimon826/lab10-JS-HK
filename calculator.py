"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): 
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if a!=0:
        return b/a
    else:
        raise ZeroDivisionError

def logarithm(a, b):
    if a>0 and b>0 and a!=1:
        return math.log(b,a)
    else:
        raise ValueError

def exponent(a,b):
    return a**b

git add ./calculator.py
git commit -m "modified calculator p1"
git push




