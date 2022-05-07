#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:44:58 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt


import find_an_index as find_an_index 


find_an_index = find_an_index.find_an_index




def liq_peak_diff_analisys(BE,
                           solvent,
                           molec,
                           xlim,
                           scale,
                           ylims,
                           leg,
                           mult,
                           title):
    
    Water_IP = np.genfromtxt('/home/raketa/Yandex.Disk/PythonLib/param_foles/Water_IP.txt')    
    liq_peak_IP = Water_IP[0]
    liq_peak_ind = find_an_index(liq_peak_IP, BE)
    
    
    left_point_of_the_spec = find_an_index(xlim[1], BE)
    right_point_of_the_spec = find_an_index(xlim[0], BE)
    
    max_int = max(solvent[left_point_of_the_spec : right_point_of_the_spec])
    
    diff_spec = molec - solvent
    diff_spec *= mult

    min_solv = min(solvent[left_point_of_the_spec : right_point_of_the_spec])
    min_molec = min(molec[left_point_of_the_spec : right_point_of_the_spec])
    min_diff = min(diff_spec[left_point_of_the_spec : right_point_of_the_spec])
    
    min_arr = np.array([min_solv, min_molec, min_diff])
    min_min = min(min_arr)

    
    plt.plot(BE, solvent)
    plt.plot(BE, molec)
    plt.plot(BE, diff_spec, '--')
    plt.plot(BE[liq_peak_ind], diff_spec[liq_peak_ind], 'o')
    plt.yscale(scale)
    plt.ylim(-1.5 * abs(min_min), max_int + 0.1 * max_int)
    plt.grid()
    plt.legend(leg)
    plt.title(title)



    
    plt.xlim(xlim[0], xlim[1])
    
    
    print('Intensity of liq peak of the solvent and the sample at 11.31 eV')
    print('---')
    print('Solvent: ' + str(solvent[liq_peak_ind]) + ' \nMolecule: '+ str(molec[liq_peak_ind]))
    print('---')
    print('Intensity diffefence at 11.31 eV')
    print('---')
    print(diff_spec[liq_peak_ind] / mult)

    plt.text(7, max_int/2, 'Diff spec at 11.31 eV = ' + str(np.round(diff_spec[liq_peak_ind], 6)))
    
    return





















