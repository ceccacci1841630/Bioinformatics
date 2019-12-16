#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:32:39 2019

@author: carlottaceccacci
"""

def lcsq(str1, str2):
    current = [''] * (len(str2) + 1)
    for c in str1:
        last, current = current, ['']
        for i, t in enumerate(str2):
            current.append(last[i] + c if c == t else max(last[i+1], current[-1], key=len))
    return current[-1]

f = open("rosalind_lcsq.txt", "r")

dnas = {}
currentKey = ''
keys = []
for content in f:
    if '>' in content:
        key = content.rstrip().replace('>', '')
        currentKey = key
        keys.append(key)
        dnas[currentKey] = ''
    else:
        dnas[currentKey] += content.rstrip()

a, b = dnas[keys[0]], dnas[keys[1]]
print (lcsq(a, b))