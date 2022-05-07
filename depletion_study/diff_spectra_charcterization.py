#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:11:35 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


import find_an_index_posit as find_an_index_posit
import find_an_index as find_an_index 
import lin_func as lin_func 
import gauss as gauss
import two_gauss_func as two_gauss_func
import standart_deviation_calculation as standart_deviation_calculation


standart_deviation_calculation = standart_deviation_calculation.standart_deviation_calculation
two_gauss_func = two_gauss_func.two_gauss_func
gauss = gauss.gauss
lin_func = lin_func.lin_func
find_an_index = find_an_index.find_an_index
find_an_index_posit = find_an_index_posit.find_an_index_posit


def diff_spectra_charcterization(BE, 
                                 spec_solvent,
                                 spec_molec,
                                 b_l_lims,
                                 xlims,
                                 ylims,
                                 print_IP,
                                 double_gauss):
    
    
    len_BE = len(BE)
    base_line_arr = np.zeros(len_BE)
    
    
    func = gauss
    
    if double_gauss == 1:
        func =  two_gauss_func
     
        
    diff_spec = spec_molec - spec_solvent
    
    left_b_l_ind = find_an_index(b_l_lims[1], BE)
    right_b_l_ind = find_an_index(b_l_lims[0], BE)
    
    left_point_of_the_spec = find_an_index(xlims[1], BE)
    right_point_of_the_spec = find_an_index(xlims[0], BE)
    ind_12eV = find_an_index(12, BE)
    
    
    left_border_ind = find_an_index(xlims[1], BE)
    
    max_int = max(diff_spec[left_point_of_the_spec : right_point_of_the_spec])
    

    base_line = np.mean(diff_spec[left_b_l_ind : right_b_l_ind])
    
    base_line_arr[:] = base_line
    
    plt.plot(BE[left_point_of_the_spec - 1 : right_point_of_the_spec ],
             diff_spec[left_point_of_the_spec - 1 : right_point_of_the_spec],
             linewidth = 2, marker='o', alpha = 0.5, linestyle='', fillstyle = 'none')
    
    plt.plot(BE[ind_12eV : left_point_of_the_spec + 1 ],
             diff_spec[ind_12eV : left_point_of_the_spec + 1 ],
             color = 'gray',
             marker='o',
             alpha = 0.5,
             linestyle='',
             fillstyle = 'none')    
    
   # plt.plot(BE, base_line_arr, '--',color = 'k')
    
    plt.xlim(xlims[0], 10.0)
    plt.ylim(-0.1*max_int, max_int + 0.25*max_int)
    
    while diff_spec[left_border_ind] > base_line:
        left_border_ind += 1
    

    
    right_border_eV = BE[left_border_ind] + 1
    right_border_ind = find_an_index(right_border_eV, BE)
    left_border_eV = BE[left_border_ind]
    
    left_extended_ind = left_border_ind + 5
    right_extended_ind = right_border_ind - 5
    

    
    BE_f_fit = BE[right_border_ind : left_border_ind]
    diff_f_fit = diff_spec[right_border_ind : left_border_ind]
    
    BE_f_fit_ext = BE[right_extended_ind : left_extended_ind]
    diff_f_fit_ext = diff_spec[right_extended_ind : left_extended_ind]
    
    popt, pcov = curve_fit(lin_func, 
                              BE[left_border_ind-1 : left_border_ind + 1 ],
                              diff_spec[left_border_ind-1 : left_border_ind + 1])
        
    a = popt[0]
    b = popt[1]
    IP_x = (base_line - b)/a
    text = 'IP th = ' + str(np.round(IP_x, 2))
    
    #plt.plot(IP_x, base_line, 'o')
    
    left_point_of_the_subplot = find_an_index(IP_x + 0.5, BE)
    right_point_of_the_subplot = find_an_index(IP_x - 0.5, BE)
    
    
    min_subplot_spec = min(diff_spec[left_point_of_the_subplot : right_point_of_the_subplot])
    
    
    
    if print_IP == 1:

        plt.text(IP_x, -abs(min_subplot_spec), text)
        plt.xlim(IP_x - 0.5, IP_x + 0.5)
        print(text)
        plt.ylim(base_line - 1.5*abs(min_subplot_spec - base_line),
                 base_line + 1.5*abs(min_subplot_spec - base_line))
        
    
        
    
    ind_of_max = find_an_index_posit(max_int, diff_spec)
    
    init_params = [BE[ind_of_max], diff_spec[ind_of_max], 1]
    bounds_1 = [12, 100, 3, 0.5]
    bounds_2 = [12, 100, 3, 9, 50, 3, 0.5]
    
    bnds = bounds_1
    
    if double_gauss == 1:
        addit_pair_init_par = init_params
        addit_pair_init_par[0] -= 1.5
        addit_pair_init_par[1] /= 3
        init_params = np.append(init_params, addit_pair_init_par)
        bnds = bounds_2
        
    init_params = np.append(init_params, 0)
    
    if print_IP == 0:
        
        popt, pcov = curve_fit(func, BE[left_point_of_the_spec : right_point_of_the_spec],
                               diff_spec[left_point_of_the_spec : right_point_of_the_spec],
                               p0 = init_params, bounds = (-0.01, bnds), maxfev = 100000)
        
        st_dev_error = standart_deviation_calculation(pcov)
        
        BE_range = BE[ind_12eV : right_point_of_the_spec]
       
        plt.plot(BE_range,
                 func(BE_range, *popt), '--', alpha = 1, color = 'green', linewidth = 2)
        
        
        
        
        if double_gauss == 1:
            par_1 =  popt[0: 3]
            par_2 = popt[3: 7]
            par_1 = np.append(par_1, 0)
            par_2 = np.append(par_2, 0)
            

            
            plt.plot(BE_range, 
                     gauss(BE_range,
                           par_1[0], 
                           par_1[1], 
                           par_1[2], 
                           par_1[3]), 
                           '--', color ='skyblue', linewidth = 0.75)
            
            plt.plot(BE_range,
                     gauss(BE_range, 
                           par_2[0],
                           par_2[1], 
                           par_2[2],
                           par_2[3]),
                           '--', color = 'r', linewidth = 0.75)
        #else:    
            
    
        plt.text(popt[0] - 0.25, max_int + 0.1*max_int, 'IP1 = ' + str(np.round(popt[0], 2)))
        
        if double_gauss == 1:
             plt.text(popt[3] - 0.5, popt[4] + 0.05*max_int, 'IP1 = ' + str(np.round(popt[3], 2)))
    
        print("Gauss params")
        
        print('--- ---')
        
        if double_gauss == 0:
            print('IP = ' + str(popt[0]) +  ' \nI = ' + str(popt[1]) + ' \nFWHM =' +
                  str(2.355 * popt[2]))   
            print('errors:')
            print('IP error =', st_dev_error[0],
                  '\nI error =', st_dev_error[1],
                  '\nFWHM error =', st_dev_error[3], sep = ' ')
            
        if double_gauss == 1:
            
            print('IP = ' + str(par_1[0]) + '\nI = ' + str(par_1[1]) + ' \nFWHM =' +
                  str(2.355 * par_1[2]))
            
            print('errors:')
            print('IP error =', st_dev_error[0],
                  '\nI error =', st_dev_error[1],
                  '\nFWHM error =', st_dev_error[3], sep = ' ')
            
            print('---')
            
            print('IP2 = ' + str(par_2[0]) + '\nI2 = ' + str(par_2[1]) + '\nFWHM2 =' +
                  str(2.355 * par_2[2]))
            
            
            print('errors:')
            print('IP2 error =', st_dev_error[3],
                  '\nI2 error =', st_dev_error[4],
                  '\nFWHM2 error =', st_dev_error[5], sep = ' ')
    
            print('--- --- ---')
    
    
    
    
    
    
    
    
    
    
    plt.grid()
    
    return