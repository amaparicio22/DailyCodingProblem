# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:59:58 2020

@author: Amanda Aparicio
""" 
def make_combos_add(num_list):
    """Takes a list of objects and outputs a list of all possible addition combinations
        of those objects. 
        input:
            num_list: a list of numbers (int or float, positive or negative)
        output:
            additions: list of numbers (int or float, positive or negative)"""
    additions = []
    n = len(num_list)
    i = 0
    while i < n:
        m = num_list[i]
        add_list = num_list[i+1:]
        for ele in add_list:
            additions.append(m+ele)
        i = i+1
    return additions
    
def compare_additions(num_list, k):
    """ Returns True if k is equal to the addition of two elements in num_list. Otherwise
    returns False.
    inputs:
        num_list: list of numbers (int or float, positive or negative)
        k: number (int or float, positive or negative)
    output:
        True or False (boolean)
    """
    try:
        float(k) #make sure that the inputs are numbers
        for ele in num_list: 
            float(ele)
        all_add_combos = make_combos_add(num_list)
        if (k in all_add_combos):
            return True
        else:
            return False
    except:
        print("ERROR: Invalid input.")
