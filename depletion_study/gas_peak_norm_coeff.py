#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:30:15 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt

import find_an_index as find_an_index 


find_an_index = find_an_index.find_an_index





def gas_peak_norm_coeff(BE, 
                        solvent,
                        molec):
    
    
    Water_IP = np.genfromtxt('/home/raketa/Yandex.Disk/PythonLib/param_foles/Water_IP.txt')    
    
    gas_peak_IP = Water_IP[1]
    gas_peak_ind = find_an_index(gas_peak_IP, BE)
    
    solvent_coeff = solvent[gas_peak_ind]
    molec_coeff = molec[gas_peak_ind]

    norm_coeff = molec_coeff / solvent_coeff
    
    return norm_coeff