#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:44:17 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

import find_an_index as find_an_index
import intens_coeff_matrix_formation as intens_coeff_matrix_formation
import diff_matrix_formation as diff_matrix_formation

diff_matrix_formation = diff_matrix_formation.diff_matrix_formation
intens_coeff_matrix_formation = intens_coeff_matrix_formation.intens_coeff_matrix_formation
find_an_index = find_an_index.find_an_index






def diff_spec_matrix(matrix_solvent, matrix_molec):
    
    BE = matrix_solvent[0]
    av_solvent = matrix_solvent[1]
    count_solvent = matrix_solvent[2]
    av_molec = matrix_molec[1]
    count_molec = matrix_molec[2]   
   
    a_solvent = np.shape(av_solvent)[0]
    a_molec = np.shape(av_molec)[0]    
    coeff_from_av = np.zeros((a_solvent, a_molec))
    ind_11_4 = find_an_index(11.31, BE)

    coeff_av = intens_coeff_matrix_formation(BE, av_solvent, av_molec)

    copy_solvent_av = av_solvent
    copy_molec_av = av_molec
    
    len_BE = len(BE)
    
       
    diff_m_av = diff_matrix_formation(av_solvent,
                                      av_molec,
                                      BE,
                                      coeff_av)
    
    diff_m_count = diff_matrix_formation(count_solvent,
                                      count_molec,
                                      BE,
                                      coeff_av)
    
    





























    
    return diff_m_av, diff_m_count







