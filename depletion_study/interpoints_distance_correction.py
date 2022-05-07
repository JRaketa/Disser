# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:48:53 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

import min_inter_eV_distance_calc as min_inter_eV_distance_calc
import invert_calibr_func as invert_calibr_func
inv_calibr_f = invert_calibr_func.invert_calibr_func


def interpoints_distance_correction(eV, corrected_spec, min_eV):

    a = np.shape(corrected_spec)[0]

    new_eV_array = np.arange(min(eV), max(eV), min_eV)
    new_eV_array = new_eV_array[::-1]

    interp_sgnl_array =  np.interp(new_eV_array, eV, corrected_spec,
                                period = 360)
                                  


    return new_eV_array, interp_sgnl_array
    
    