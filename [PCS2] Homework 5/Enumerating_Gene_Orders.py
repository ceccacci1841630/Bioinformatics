#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:03:21 2019

@author: carlottaceccacci
"""

#itertools.permutations()


import math                                         
import itertools                                    
n = 5                                               
print(math.factorial(n))                            
perm = itertools.permutations(list(range(1, n + 1)))
for i, j in enumerate(list(perm)):                  
    permutation = ''                                
    for item in j:                                  
        permutation += str(item) + ' '              
    print(permutation)   
