# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:56:20 2020

@author: Amanda Aparicio
@problem_author: Daily Coding Problem

Task:
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set 
of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings
[dog, deer, deal], return [deer, deal].

Note: There are more efficient ways to do this (such as using a trie data
structure), but for now I'm going to post my original attempt.
"""

def autocomplete(s, query_s):
    """Returns the words in query_s whose prefix is given by s"""
    n = len(s)
    matches = []
    for word in query_s:
        if word[:n] == s:
            matches.append(word)
    return matches