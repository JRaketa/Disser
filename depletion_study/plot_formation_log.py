#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:30:38 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

import find_an_index as find_an_index 

find_an_index = find_an_index.find_an_index

def plot_formation_log(BE, 
                       spec_solvent,
                       spec_molec,
                       xlim,
                       ylim,
                       diff_spec_lim,
                       diff_spec_mult_coeff,
                       scale,
                       leg,
                       title,
                       legend_location):
    
    temp_leg = leg
   
    diff_spec = spec_molec - spec_solvent
    diff_spec [:] *= diff_spec_mult_coeff
    
    diff_spec_lim_left = find_an_index(diff_spec_lim[0], BE)
    diff_spec_lim_right = find_an_index(diff_spec_lim[1], BE)
    
    left_point_of_the_spec = find_an_index(xlim[1], BE)
    right_point_of_the_spec = find_an_index(xlim[0], BE)
    
    max_int_solvent = max(spec_solvent[left_point_of_the_spec : right_point_of_the_spec])
    max_int_molec = max(spec_molec[left_point_of_the_spec : right_point_of_the_spec])    
    
    if max_int_solvent > max_int_molec:
        max_int = max_int_solvent
    else:
        max_int = max_int_molec
    #print(max_int)
    
    plt.plot(BE, spec_solvent)
    plt.plot(BE, spec_molec) 
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    plt.yscale(scale)
    plt.grid()
    plt.legend(temp_leg, fontsize = 12, loc=legend_location)
   # plt.xticks(fontsize = 12)
    #plt.yticks(fontsize = 12)
    #plt.title(title)
    
    return