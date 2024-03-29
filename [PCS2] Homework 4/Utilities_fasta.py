#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:58:12 2019

@author: carlottaceccacci
"""

import os

def file_reader(file_name, fasta=False):
    to_split_at = "\n"
    if fasta:
        to_split_at = ">"
    path = os.path.expanduser("~/desktop/" + file_name)
    with open(path, "r") as file:
        s = file.read()
    return s.split(to_split_at)

if __name__ == "__main__":
    l = file_reader("rosalind_prot.txt")
    for el in l:
        print(el)
    print(len(l))
    
    
    
