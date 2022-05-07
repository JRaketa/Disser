# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:14:11 2019

@author: motilek
"""
import numpy as np 
import calibr_func as c_f
import matplotlib.pyplot as plt

calibr_func=c_f.calibr_func


def jacobian_spec_correction(spec, calibr_par, time_array):
    t0=calibr_par[0] 
    
    jacobian_processed_spec_array = spec * ((1e-9 * time_array - t0))**3/(1.6e-19)

    
    return jacobian_processed_spec_array  
        