# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:34:58 2020

@author: Amanda Aparicio
@problem_author: Daily Coding Problem

Task:
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear 
time and constant space. In other words, find the lowest positive integer that
 does not exist in the array. The array can contain duplicates and negative 
 numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
 should give 3.

You can modify the input array in-place.
"""

def sortAndshort(num_list):
    """Takes a list of numbers, positive or negative, and returns a version
    of the list that is sorted from least to greatest and only contains
    positive values
    """
    sorted_list = num_list[:]
    sorted_list = set(sorted_list) #gets rid of duplicates
    sorted_list = list(sorted_list)
    sorted_list.sort()
    short_list = []
    for num in sorted_list:
        if num >=0:
            short_list.append(num)
    return short_list

def comparisonList(short_list):
    """Takes the shortened and sorted version of the list and creates a new
    list that starts at the minimum value of the short_list, ends at the max
    value of the short_list, and has an interval of 1. This list will act as
    our comparison to see what's missing.
    """
    min_num =min(short_list)
    max_num = max(short_list)
    compare_list = [*range(min_num, max_num+1)]
    return compare_list

def missingLowestPosInt(num_list):
    """Finds the lowest, positive, missing integer from a list of numbers by
    first sorting and shortening the input num_list, and then comparing the output
    to a comparison list. Outputs the first missing value. If there are no missing values,
    then takes the max of the shortened list as the missing value.
    """
    short_list = sortAndshort(num_list)
    compare_list = comparisonList(short_list)
    for ind, num in enumerate(short_list):
        if short_list[ind] != compare_list[ind]:
            low_int = compare_list[ind]
            return low_int
        else:
            low_int = 0
    if low_int == 0:
        low_int = max(short_list)+1
        return low_int

