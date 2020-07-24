# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:46:30 2020

@author: Amanda Aparicio
@problem_author: Daily Coding Problem

Task:
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n,
 and calls f after n milliseconds.
"""
from time import sleep

def job_scheduler(f, n):
    sec = n/1000 #convert from milliseconds to seconds
    sleep(sec)
    return f

### Note: ###
# My solution does not allow for anything else to happen while you wait
#for the function to implement. I've read another solution that is better
#because it allows for you to continue working, so it's a true "scheduler".
#Because this is not my original code, however, I'm leaving up my original
#attempt.