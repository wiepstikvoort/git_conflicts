#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This code is supposed to calculate the Fibonnaci sequence
and do some other calculations with it
"""

import matplotlib.pyplot as plt

def fibonnaci(number_digits: int) -> list:
    """
    This function outputs number_digits numbers from
    the fibonnaci series.
    
    Parameters
    ----------
    number_digits: int
        the number of numbers we wanna output from the
        fibonnaci sequence.
    
    Returns
    ----------
    list: list containint number_digits numbers from the fibonnaci series
    """

    return_list = []
    for num in range(number_digits):
        if num < 2:
            # Define F0 and F1 as 0 and 1
            return_list.append(num)
        else:
            value = return_list[-1] + return_list[-2]
            return_list.append(value)
    
    return return_list

# If script executed as main, make a nice plot
#   having the number in the x axis and the value
#   of the sequence in the Y axis
# TODO: Rephrase this description
if __name__ == "__main__":
    # Create figure and axes
    fig, ax = plt.subplots(1,1,1)
    num_digits = 15 # FIXME: Can we do this with arguments??
    lin = ax.plot([i for i in range(num_digits)], fibonnaci(num_digits))
    plt.setp(
        ax,
        xlabel="Sequence digit",
        ylabel="Sequence digit value",
        title="Fibonnaci sequence"
    )
    plt.show()
