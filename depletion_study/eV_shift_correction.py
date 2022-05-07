# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:57:56 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

import min_inter_eV_distance_calc as min_inter_eV_distance_calc
import invert_calibr_func as invert_calibr_func
inv_calibr_f = invert_calibr_func.invert_calibr_func


def eV_shift_correction(eV, spec, shift):


    interp_sgnl_array =  np.interp(eV + shift, eV, spec,
                                period = 360)
                                  

    return interp_sgnl_array
    
    