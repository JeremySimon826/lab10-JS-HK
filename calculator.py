"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a!=0:
        return b / a
    raise ZeroDivisionError

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a*b

git add .	     # staging all files to be saved
git commit -m "modified calculator p1" # saving changes w/ message
git push		# sending changes to the remote repository (GitHub)



