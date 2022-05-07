# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:57:27 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt


def find_an_index(val, arr):
    
    t = 0
    
    while arr[t] > val:
        t += 1
  
    
    return t