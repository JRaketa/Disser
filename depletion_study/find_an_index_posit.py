# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:36:44 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt


def find_an_index_posit(val, arr):
    
    t = len(arr) - 1
    
    
    while arr[t] != val:
        t -= 1
  
    
    return t