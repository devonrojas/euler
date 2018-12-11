#!/usr/bin/env python
"""
Program computes Euler's method algorithm for an
inputted function and graphs the resulting data
along with original function
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x, y = symbols("x y")

__author__ = "Devon Rojas"
__date__ = "December 10, 2018"
__maintainer__ = "Devon Rojas"
__email__ = "devonmrojas@gmail.com"
__status__ = "Prototype"

def euler(x0, y0, h, xn):
    """
    Computes Euler's Method

    Parameters:
    -------------
    x0 : int
        Initial x-value

    y0 : int
        Initial y-value

    h : int
        Interval step size

    xn : int
        Ending x-value

    Returns:
    -------------
    void

    """
    x_arr = []
    y_arr = []
    err_arr = [0]
    ### Euler algorithm
    n = int((xn - x0)/h + 1)
    x_arr.append(x0)
    y_arr.append(y0)
    print('\nX\tY\tError\n-----------')
    for i in range(0,n):
        res = eq.subs([(x, x0), (y, y0)])
        y_temp = y0 + h * res
        x_temp = x0 + h
        print('%.2f\t%.2f\t%.3f' % (x0, y0, res-y0))
        if x_temp <= xn:
            x0 = x_temp
            y0 = y_temp
            x_arr.append(x0)
            y_arr.append(y0)
            err_arr.append(res-y0)
        else:
            break
    ### Graph resulting euler data & original function
    graph(x_arr, y_arr, n, err_arr)

def graph(x, y, n, err):
    """
    Helper function to graph data

    Parameters:
    -------------
    ax : Axes
        The axes to draw

    x : array
        The x data

    y : array
        The y data

    Returns:
    -------------
    ax : list
        List of artists added
    """
    ax = plt.plot(x, y, marker="o", label="Euler")

    ### Plot original function over same interval
    _x = np.linspace(0, xn, 100)
    _y = []
    for i in _x:
        res = eq.subs('x', i)
        _y.append(res)
    ax = plt.plot(_x, _y, label="Original")
    ax = plt.plot(x, err, label="Error")
    plt.legend()
    return ax

### Parse input into function
eq = sympify(input("Enter an equation: "))

x0 = int(input("Enter initial x value: "))
y0 = int(input("Enter initial y value: "))
h = float(input("Enter interval: "))
xn = int(input("Enter ending value: "))

euler(x0, y0, h, xn)

### Display plot graph
plt.grid()
plt.show()
