#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:38:49 2019

@author: carlottaceccacci
"""

with(open('rosalind_tree.txt', 'r')) as f:
    n = int(f.readline())
    tuples = [line.split() for line in f]

print(n - len(tuples) - 1)