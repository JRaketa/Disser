#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:18:11 2020

@author: raketa
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
import spec_matrix as spec_matrix
import st_dev_calc as st_dev_calc


st_dev_calc = st_dev_calc.st_dev_calc
spec_matrix = spec_matrix.spec_matrix
water_gas_peak_shift_calc = water_gas_peak_shift_calc.water_gas_peak_shift_calc
eV_shift_correction = eV_shift_correction.eV_shift_correction
interpoints_distance_correction = interpoints_distance_correction.interpoints_distance_correction
jacobian_spec_correction = jacobian_spec_correction.jacobian_spec_correction
kin_en_calc = kin_en_calc.kin_en_calc
time_array_correction = time_array_correction.time_array_correction
base_line_correction = base_line_correction.base_line_correction
tof_array_creation = tof_array_creation.tof_array_creation







def PE_spec_formation_with_error(path, 
                                 tof_list_mode,
                                 tof_arrays_solvent,
                                 tof_arrays_molec,
                                 calibr_result,
                                 harm):
    
    solvent_av = np.array([])
    solvent_count = np.array([])
    molec_av = np.array([])
    molec_count = np.array([])
    
    solvent_av_jacob = np.array([])
    solvent_count_jacob = np.array([])
    molec_av_jacob = np.array([])
    molec_count_jacob = np.array([])
    
    solvent_av_jacob_interp = np.array([])
    solvent_count_jacob_interp = np.array([])
    molec_av_jacob_interp = np.array([])
    molec_count_jacob_interp = np.array([])
    new_eV = np.array([])
    
    
    len_spec = 0
    corrected_time_array = np.array([])
    
    full_tof_array_solvent = tof_array_creation(tof_arrays_solvent, tof_list_mode)    
    full_tof_array_molec = tof_array_creation(tof_arrays_molec, tof_list_mode)    
    
    len_solv_tof = len(full_tof_array_solvent)
    len_molec_tof = len(full_tof_array_molec)
    
    harm_energy = harm * 1240 / 795
    

    av_spec_matrix_solvent = spec_matrix(path,
                                         full_tof_array_solvent,
                                         1)

    count_spec_matrix_solvent = spec_matrix(path,
                                            full_tof_array_solvent,
                                            2)  
    
    av_spec_matrix_molec = spec_matrix(path,
                                       full_tof_array_molec,
                                       1)

    count_spec_matrix_molec = spec_matrix(path,
                                          full_tof_array_molec,
                                          2)  
        
    
    for n in range(len_solv_tof):
        av_spec_matrix_solvent[n] = base_line_correction(av_spec_matrix_solvent[n])
     #   count_spec_matrix_solvent[n] = base_line_correction(count_spec_matrix_solvent[n])
    
    for n in range(len_molec_tof):
        av_spec_matrix_molec[n] = base_line_correction(av_spec_matrix_molec[n])
      #  count_spec_matrix_molec[n] = base_line_correction(count_spec_matrix_molec[n])    
    
    
    time_array = np.genfromtxt(path +'TOF_' + str(tof_arrays_solvent[0])+'.dat')[:, 0] 
    
    
    for n in range(len_solv_tof):
        
        temp_av = time_array_correction(av_spec_matrix_solvent[n],
                                        time_array,
                                        calibr_result[0])
        
        len_spec = len(temp_av)
        corrected_time_array = temp_av[0]
        
        temp_count = time_array_correction(count_spec_matrix_solvent[n],
                                           time_array,
                                           calibr_result[0])
    
        solvent_av = np.append(solvent_av, temp_av[1])
        solvent_count = np.append(solvent_count, temp_count[1])

    for n in range(len_molec_tof):
        
        temp_av = time_array_correction(av_spec_matrix_molec[n],
                                        time_array,
                                        calibr_result[0])
        
        temp_count = time_array_correction(count_spec_matrix_molec[n],
                                           time_array,
                                           calibr_result[0])
    
        molec_av = np.append(molec_av, temp_av[1])
        molec_count = np.append(molec_count, temp_count[1])    
        
    
    b_solvent = int (len(solvent_av) / len_solv_tof)
    b_molec = int (len(molec_av) / len_molec_tof)
    
    
    solvent_av = np.reshape(solvent_av, (len_solv_tof, b_solvent))
    solvent_count = np.reshape(solvent_count, (len_solv_tof, b_solvent))
    
    molec_av = np.reshape(molec_av, (len_molec_tof, b_molec))
    molec_count = np.reshape(molec_count, (len_molec_tof, b_molec))
    
    
    eV = kin_en_calc(calibr_result, corrected_time_array)
    bin_en = harm_energy - eV
    
    
    
    for n in range(len_solv_tof):
        temp_av_jacob = jacobian_spec_correction(solvent_av[n], 
                                                 calibr_result,
                                                 corrected_time_array) 
        
        temp_count_jacob = jacobian_spec_correction(solvent_count[n], 
                                                    calibr_result,
                                                    corrected_time_array) 
        
        solvent_av_jacob =  np.append(solvent_av_jacob, temp_av_jacob)
        solvent_count_jacob = np.append(solvent_count_jacob, temp_count_jacob)
        
        
    for n in range(len_molec_tof):
        temp_av_jacob = jacobian_spec_correction(molec_av[n], 
                                                 calibr_result,
                                                 corrected_time_array) 
        
        temp_count_jacob = jacobian_spec_correction(molec_count[n], 
                                                    calibr_result,
                                                    corrected_time_array) 
        
        molec_av_jacob =  np.append(molec_av_jacob, temp_av_jacob)
        molec_count_jacob = np.append(molec_count_jacob, temp_count_jacob)        
    
    
    
    
    solvent_av_jacob = np.reshape( solvent_av_jacob, 
                                  (len_solv_tof, b_solvent))
    
    solvent_count_jacob = np.reshape( solvent_count_jacob,
                                     (len_solv_tof, b_solvent))
    
    molec_av_jacob = np.reshape( molec_av_jacob, 
                                (len_molec_tof, b_molec))
    
    molec_count_jacob = np.reshape( molec_count_jacob,
                                   (len_molec_tof, b_molec))


    for n in range(len_solv_tof):
        temp_av = interpoints_distance_correction(bin_en,
                                                  solvent_av_jacob[n],
                                                  0.05)
        
        temp_count = interpoints_distance_correction(bin_en,
                                                     solvent_count_jacob[n],
                                                     0.05)
        
        new_eV = temp_av[0]
        solvent_av_jacob_interp = np.append(solvent_av_jacob_interp , temp_av[1])
        solvent_count_jacob_interp = np.append(solvent_count_jacob_interp , temp_count[1])
        
        
        
    for n in range(len_molec_tof):
        temp_av = interpoints_distance_correction(bin_en,
                                                  molec_av_jacob[n],
                                                  0.05)
        
        temp_count = interpoints_distance_correction(bin_en,
                                                     molec_count_jacob[n],
                                                     0.05)    
        
        molec_av_jacob_interp = np.append(molec_av_jacob_interp , temp_av[1])
        molec_count_jacob_interp = np.append(molec_count_jacob_interp , temp_count[1])
        

        
    len_new_eV = len(new_eV)    
        
        
        
    solvent_av_jacob_interp = np.reshape(solvent_av_jacob_interp , (len_solv_tof, len_new_eV))
    solvent_count_jacob_interp = np.reshape(solvent_count_jacob_interp , (len_solv_tof, len_new_eV))
    molec_av_jacob_interp = np.reshape(molec_av_jacob_interp , (len_molec_tof, len_new_eV))
    molec_count_jacob_interp = np.reshape(molec_count_jacob_interp , (len_molec_tof, len_new_eV))
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  #  plt.clf()
  #  plt.figure(7)
    #plt.plot(new_eV, solvent_av_error)
    #plt.plot(new_eV, solvent_count_mean)
  #  plt.errorbar(new_eV, solvent_av_mean, yerr = solvent_av_error,  fmt=' ', color='k')
  #  plt.xlim(5, 15)
   # plt.yscale('log')
    
            
        
        
        
    

    

    
    
    
    
    
    return new_eV, solvent_av_jacob_interp, solvent_count_jacob_interp, molec_av_jacob_interp, molec_count_jacob_interp