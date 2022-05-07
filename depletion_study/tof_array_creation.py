# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:45:44 2020

@author: motilek
"""
import numpy as np
import matplotlib.pyplot as plt



def tof_array_creation(tof_arrays, tof_list_mode):
    
    
    if len(tof_arrays) > 1:
        if tof_list_mode == 0:
            tof_array = np.arange(tof_arrays[0], tof_arrays[1] + 1, 1)
        if tof_list_mode == 1: 
            tof_array = tof_arrays
    
    if len(tof_arrays) == 1:
        tof_array = tof_arrays
    
    return tof_array
    