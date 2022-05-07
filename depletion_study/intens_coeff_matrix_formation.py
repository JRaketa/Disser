#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 00:03:35 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt


import find_an_index as find_an_index

find_an_index = find_an_index.find_an_index


def intens_coeff_matrix_formation(BE,
                                  matrix_solvent,
                                  matrix_molec):
    
    ind_11_4 = find_an_index(11.31, BE)
    
    a_molec = np.shape(matrix_molec)[0]
    a_solvent = np.shape(matrix_solvent)[0]
    
    coeff_from_av = np.zeros((a_solvent, a_molec))

    for n in range(a_solvent):
        temp_solvent_av = matrix_solvent[n]
        temp_solvent_intens = temp_solvent_av[ind_11_4]

        for m in range(a_molec):
            temp_molec_av = matrix_molec[m]
            temp_molec_intens = temp_molec_av[ind_11_4]
        
            temp_coeff = temp_molec_intens / temp_solvent_intens
            coeff_from_av[n][m] = temp_coeff
    
    
    
    return coeff_from_av