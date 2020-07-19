# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 13:00:43 2020

@author: Amanda Aparicio
@problem_author: Daily Coding Problem

Task:
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first 
and last element of that pair. For example, car(cons(3, 4)) returns 3, 
and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

def cons(a, b):
    """Function defined in the problem. Returns a function whose inputs are
    (a,b)"""
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    """Returns the left value, a, from cons(a,b)"""
    def left_val(a,b):
        return a
    return pair(left_val)

def cdr(pair):
    """Returns the right value, b, from cons(a,b)"""
    def right_val(a,b):
        return b
    return pair(right_val)

    