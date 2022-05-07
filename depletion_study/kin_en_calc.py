# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:51:12 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

import calibr_func as calibr_func
calibr_func = calibr_func.calibr_func

def kin_en_calc(calibr_par, time_array):
    eV = calibr_func(1e-9 * time_array, *calibr_par)    
    
    
    return eV