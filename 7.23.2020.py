# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:02:27 2020

@author: Amanda Aparicio
@problem_author: Daily Coding Challenge

Task:
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum 
of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
 [5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""

def create_skipcombos(num_list, n_skip):
    """Creates all possible combinations of a list with n_skips. For example,
    if n_skip = 1, then creates a list of lists where each individual list
    is the original list with 1 element skipped"""
    skip_combos = []
    for skip in range(n_skip+1):
        combos = []
        skip_list = num_list[skip:]
        n_tot = len(skip_list)
        i = 0
        while i < n_tot:
            combos.append(skip_list[i])
            i = i+1+n_skip
        if len(combos) > 1: #if there's only one element in the resulting list, skip it
            skip_combos.append(combos)
    return skip_combos

def add_combos(num_list):
    """Adds up each element in the list for a maximum output (i.e. won't add negative
    values to the total)"""
    tot = 0
    for num in num_list:
        if tot+num > tot:
            tot = tot+num
    return tot

def create_allcombos(num_list):
    """Given a list of numbers, creates a list of lists with all combinations
    of non-adjacent values with a constant skip value of 1, 2, 3, ... len(num_list) - 2."""
    all_combos =[]
    n = len(num_list)
    max_nskips = n-2
    for skip_num in range(1, max_nskips+1):
        combo = create_skipcombos(num_list, skip_num)
        for ele in combo:
            all_combos.append(ele)
    return all_combos

def max_value(num_list):
    """Finds the largest sum of non-adjacent values from a given list"""
    all_combos = create_allcombos(num_list)
    tots = []
    for ele in all_combos:
        tot =add_combos(ele)
        tots.append(tot)
    return max(tots)