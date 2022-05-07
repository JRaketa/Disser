#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:55:36 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt

import find_an_index as find_an_index 
import scientific_not as scientific_not

scientific_not = scientific_not.scientific_not
find_an_index = find_an_index.find_an_index

def subplot_formation_log(BE, 
                          spec_solvent,
                          spec_molec,
                          xlim,
                          ylim,
                          diff_spec_lim,
                          diff_spec_mult_coeff,
                          scale):

   
    diff_spec = spec_molec - spec_solvent
    diff_spec [:] *= diff_spec_mult_coeff
    
    diff_spec_lim_left = find_an_index(diff_spec_lim[0], BE)
    diff_spec_lim_right = find_an_index(diff_spec_lim[1], BE)
    
    left_point_of_the_spec = find_an_index(xlim[1], BE)
    right_point_of_the_spec = find_an_index(xlim[0], BE)

    max_int = max(diff_spec[ diff_spec_lim_right : diff_spec_lim_left])

    
    
    plt.plot(BE, spec_solvent, color = 'C0')
    plt.plot(BE, spec_molec, color = 'C1') 
    plt.plot(BE[diff_spec_lim_right : diff_spec_lim_left],
             diff_spec[diff_spec_lim_right : diff_spec_lim_left], '--', 
             color = 'C2') 
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(-0.1 *max_int, max_int + 0.1*max_int)
    plt.yscale(scale)
    plt.grid()

    
    return