#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 01:34:23 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import find_an_index as find_an_index 
import lin_func as lin_func

lin_func = lin_func.lin_func
find_an_index = find_an_index.find_an_index



def diff_spec_analisys(BE,
                       diff_spec,
                       base_line_lims,
                       approx_lims,
                       plot_xlims,
                       plot_ylims):
    
    a = np.shape(diff_spec)[0]
    b = np.shape(diff_spec)[1]
    
    left_approx_point = find_an_index(approx_lims[1], BE)
    right_approx_point = find_an_index(approx_lims[0], BE)
    
    left_base_line = find_an_index(base_line_lims[1], BE)
    right_bas_line = find_an_index(base_line_lims[0], BE)
    
    bl = np.zeros(b)
    IP = np.array([])
    normal_deviation = 0
    
    for n in range(a):
        plt.plot(BE, diff_spec[n])
        x_approx = BE[left_approx_point : right_approx_point]
        y_approx =  diff_spec[n][left_approx_point : right_approx_point]
        popt, pcov = curve_fit(lin_func, x_approx, y_approx) 
        plt.plot(x_approx, lin_func(x_approx, *popt), color = 'b')
        
        bl_val = np.mean(diff_spec[n][left_base_line : right_bas_line], axis = 0)
        bl[:] = bl_val
        plt.plot(BE, bl, '--', color = 'k', linewidth = 0.5)
        intersection = (bl_val - popt[1]) / popt[0]
        IP = np.append(IP, intersection)
        
    mean_IP = np.mean(IP, axis = 0)    
        
    len_IP = len(IP)
    
    mean_sq_sum = 0
    
    for n in range(len_IP):
        mean_sq_sum = (mean_IP - IP[n])**2
    
    normal_deviation = ( 1 / (len_IP) * mean_sq_sum)**0.5
        
    print(mean_IP, normal_deviation)    
        
    plt.xlim(plot_xlims[0], plot_xlims[1])
    plt.ylim(plot_ylims[0], plot_ylims[1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return