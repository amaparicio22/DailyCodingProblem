# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:59:38 2020

@author: Amanda Aparicio
@problem_author: edabit (edabit.com)

Task:
In this challenge, establish if a given integer num is a Curzon number.
 If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied
 by num, then num is a Curzon number.

Given a non-negative integer num, implement a function that returns 
True if num is a Curzon number, or False otherwise.

My added task: Can we find a pattern of Curzon numbers?
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def is_Curzon(n):
    """Checks to see if a value, n, is a Curzon number or not. """
    if n <0 or type(n) != int:
        return print("Please provide a non-negatieve integer")
    else:
        numerator = 1+2**n
        denominator = 1+2*n
        remainder = numerator%denominator
        if remainder == 0:
            return True
        else:
            return False

def find_Curzon(num_list):
    """Returns a list of 1's and 0's. 1 means the number is a 
    Curzon number, 0 means the number is not"""
    list_Curzon = []
    for num in num_list:
        list_Curzon.append(int(is_Curzon(num)))
    return list_Curzon


def plot_Curzon(grid_size):
    """Plots a grid_size by grid_size figure where dark blue
    squares are the location of Curzon numbers"""
    n = grid_size*grid_size
    list_Curzon = find_Curzon(range(0,n))
    array_Curzon = np.array(list_Curzon)
    grid_Curzon = np.reshape(array_Curzon, (grid_size, grid_size))
        
    plt.figure(figsize=(15, 15))
    sns.heatmap(grid_Curzon, linecolor='white', 
                cmap = "Blues", cbar = False, square = True)
    plt.show()