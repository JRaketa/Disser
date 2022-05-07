# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:35:43 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

import av_spec as av_spec 
import tof_array_creation as tof_array_creation
import base_line_correction as base_line_correction 
import time_array_correction as time_array_correction
import kin_en_calc as kin_en_calc
import jacobian_spec_correction as jacobian_spec_correction 
import interpoints_distance_correction as interpoints_distance_correction
import eV_shift_correction as eV_shift_correction
import water_gas_peak_shift_calc as water_gas_peak_shift_calc


water_gas_peak_shift_calc = water_gas_peak_shift_calc.water_gas_peak_shift_calc
eV_shift_correction = eV_shift_correction.eV_shift_correction
interpoints_distance_correction = interpoints_distance_correction.interpoints_distance_correction
jacobian_spec_correction = jacobian_spec_correction.jacobian_spec_correction
kin_en_calc = kin_en_calc.kin_en_calc
time_array_correction = time_array_correction.time_array_correction
base_line_correction = base_line_correction.base_line_correction
tof_array_creation = tof_array_creation.tof_array_creation
av_spec = av_spec.av_spec




def PE_spec_formation(path, 
                      tof_list_mode,
                      tof_arrays,
                      calibr_result,
                      harm):
    
    full_tof_array = tof_array_creation(tof_arrays, tof_list_mode)    
    harm_energy = harm * 1240 / 795

    av_mode_spec_mean = av_spec(path, 
                            full_tof_array,
                            1)

    count_mode_spec_mean = av_spec(path, 
                            full_tof_array,
                            2)
                                                        

    time_array = np.genfromtxt(path +'TOF_' + str(tof_arrays[0])+'.dat')[:, 0] 

    av_mode_spec_mean_b_l = base_line_correction(av_mode_spec_mean)


    av_time_corrected_spec = time_array_correction(av_mode_spec_mean_b_l,
                                            time_array,
                                            calibr_result[0])

    count_time_corrected_spec = time_array_correction(count_mode_spec_mean,
                                            time_array,
                                            calibr_result[0])       
                                     
    time_array_tc = av_time_corrected_spec[0]
    av_spec_mean_tc = av_time_corrected_spec[1]    
    count_spec_mean_tc = count_time_corrected_spec[1]                                 
                                            
    eV = kin_en_calc(calibr_result, time_array_tc)
    bin_en = harm_energy - eV


    av_jacob =  jacobian_spec_correction(av_spec_mean_tc, 
                                     calibr_result,
                                     time_array_tc)         
                                     
    count_jacob =  jacobian_spec_correction(count_spec_mean_tc, 
                                     calibr_result,
                                     time_array_tc)                                     

    interp_result_av = interpoints_distance_correction(bin_en,
                                                av_jacob,
                                                0.05)
                                                
    interp_result_count = interpoints_distance_correction(bin_en,
                                                count_jacob,
                                                0.05)                                                
                                                
    av_interp_eV = interp_result_av[0]
    av_interp_sgnl = interp_result_av[1]
    count_interp_sgnl = interp_result_count[1]


    
    return av_interp_eV, av_interp_sgnl, count_interp_sgnl
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    