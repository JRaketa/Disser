#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:36:20 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt


import tof_array_creation as tof_array_creation
import base_line_correction as base_line_correction 
import time_array_correction as time_array_correction
import kin_en_calc as kin_en_calc
import jacobian_spec_correction as jacobian_spec_correction 
import interpoints_distance_correction as interpoints_distance_correction
import eV_shift_correction as eV_shift_correction
import water_gas_peak_shift_calc as water_gas_peak_shift_calc
import spec_matrix as spec_matrix

spec_matrix = spec_matrix.spec_matrix
water_gas_peak_shift_calc = water_gas_peak_shift_calc.water_gas_peak_shift_calc
eV_shift_correction = eV_shift_correction.eV_shift_correction
interpoints_distance_correction = interpoints_distance_correction.interpoints_distance_correction
jacobian_spec_correction = jacobian_spec_correction.jacobian_spec_correction
kin_en_calc = kin_en_calc.kin_en_calc
time_array_correction = time_array_correction.time_array_correction
base_line_correction = base_line_correction.base_line_correction
tof_array_creation = tof_array_creation.tof_array_creation


def matrix_of_jacob_spec_formation(path, 
                                   tof_list_mode,
                                   tof_arrays,
                                   calibr_result,
                                   harm):
    
    full_tof_array = tof_array_creation(tof_arrays, tof_list_mode)    
    harm_energy = harm * 1240 / 795
    
    corrected__time_array = np.array([])
    time_corr_av_spec = np.array([])
    time_corr_count_spec = np.array([])
    av_jacob_spec = np.array([])
    count_jacob_spec = np.array([])
    interp_av = np.array([])
    interp_count = np.array([])
    interp_BE = np.array([])
    len_spec_interp = 0
    
    len_tof_array = len(full_tof_array)
    
    time_array = np.genfromtxt(path +'TOF_' + str(tof_arrays[0])+'.dat')[:, 0] 
    
    av_spec_matrix = spec_matrix(path,
                                 full_tof_array,
                                 1)

    count_spec_matrix = spec_matrix(path,
                                 full_tof_array,
                                 2)    
    
    for n in range(len_tof_array):
        av_spec_matrix[n] = base_line_correction(av_spec_matrix[n])
        count_spec_matrix[n] = base_line_correction(count_spec_matrix[n])
    
    av_bl_correction = av_spec_matrix
    count_bl_correction = count_spec_matrix
   

    for n in range(len_tof_array):
        temp_array = time_array_correction(av_bl_correction[n],
                                            time_array,
                                            calibr_result[0])[1]
        
        time_corr_av_spec = np.append(time_corr_av_spec, temp_array)
        
        corrected__time_array = time_array_correction(av_bl_correction[n],
                                            time_array,
                                            calibr_result[0])[0]
    
    for n in range(len_tof_array):
         
        temp_array = time_array_correction(count_bl_correction[n],
                                            time_array,
                                            calibr_result[0])[1]
        
        time_corr_count_spec = np.append(time_corr_count_spec, temp_array)
    
    new_spec_len = len(corrected__time_array)    
    
    time_corr_av_spec = np.reshape(time_corr_av_spec, (len_tof_array,
                                                       new_spec_len)) 
    time_corr_count_spec = np.reshape(time_corr_count_spec, (len_tof_array,
                                                       new_spec_len)) 
    
    
    
    eV = kin_en_calc(calibr_result, corrected__time_array)
    BE = harm_energy - eV
    
    for n in range(len_tof_array):
        temp_av = jacobian_spec_correction(time_corr_av_spec[n],
                                           calibr_result,
                                           corrected__time_array)
        
        temp_count = jacobian_spec_correction(time_corr_count_spec[ n],
                                           calibr_result,
                                           corrected__time_array)
        
        av_jacob_spec = np.append(av_jacob_spec, temp_av)
        count_jacob_spec = np.append(count_jacob_spec, temp_count)
    
    av_jacob_spec = np.reshape(av_jacob_spec, (len_tof_array,
                                                       new_spec_len))
    count_jacob_spec = np.reshape(count_jacob_spec, (len_tof_array,
                                                       new_spec_len))
   
    for n in range(len_tof_array):
        temp_av = interpoints_distance_correction(BE,
                                                av_jacob_spec[n],
                                                0.05)
        temp_count = interpoints_distance_correction(BE,
                                                     count_jacob_spec[n],
                                                     0.05)
        interp_BE = temp_av[0]
        temp_interp_av = temp_av[1]
        temp_interp_count = temp_count[1]
        
        interp_av = np.append(interp_av, temp_interp_av)
        interp_count = np.append(interp_count, temp_interp_count)
        
        len_spec_interp = len(temp_interp_av)
        
    interp_av_matrix = np.reshape(interp_av, (len_tof_array,
                                              len_spec_interp))
    
    interp_count_matrix = np.reshape(interp_count, (len_tof_array,
                                              len_spec_interp))
    

    
    
    return interp_BE, interp_av_matrix, interp_count_matrix