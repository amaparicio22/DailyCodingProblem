# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:11:22 2020

@author: Amanda Aparicio
@problem_author: Daily Coding Problem (https://www.dailycodingproblem.com/)

Task:
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index 
i of the new array is the product of all the numbers in the original array 
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would 
be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def multExcept4i(num_list, i):
    """Multiplies all the numbers in a list together except for the number at 
    the ith index (indexing of 0)
    """
    mult_list = num_list[:]
    del mult_list[i]
    res = 1
    for num in mult_list:
        res = res*num
    return res

def multExcept4i_list(num_list):
    """Creates list where each element at index i is the product of all numbers
    in the original index except for the one at i
    """
    res_list = []
    for ind, num in enumerate(num_list):
        res = multExcept4i(num_list, ind)
        res_list.append(res)
    return res_list