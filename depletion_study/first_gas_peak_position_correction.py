# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:43:07 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import find_an_index as find_an_index
import gauss as gauss 
import eV_shift_correction as eV_shift_correction

eV_shift_correction = eV_shift_correction.eV_shift_correction
gauss = gauss.gauss
find_an_index = find_an_index.find_an_index

def first_gas_peak_position_correction(eV, spec):
    


    shift_corrected_spec = eV_shift_correction(eV, spec, dt)    
    
    
    return shift_corrected_spec