#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This code is supposed to calculate the Fibonnaci sequence
and do some other calculations with it
"""

# FIXME: Refactor the name for this library
import matplotlib.pyplot as matplotlibpyplotlongnameSebiIhopeyoulikeit

def fibonnaci(number_digits: int) -> list:
    """Documentation. Please, implement and comment me!"""
    phi = (1 + 5 ** 0.5) / 2
    return [int((phi ** n - (1 - phi) ** n) / 5 ** 0.5) for n in range(number_digits)]

   
# Plot something 
if __name__ == "__main__":
    # Plot something about the fibonnaci sequence
    pass
