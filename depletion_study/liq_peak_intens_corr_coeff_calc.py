# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:15:08 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

import find_an_index as find_an_index

find_an_index = find_an_index.find_an_index

def liq_peak_intens_corr_coeff_calc(eV,
                                    solvent_sgnl,
                                    molec_sgnl,
                                    eV_corr_point):
    
    
    liq_peak_pos = find_an_index(eV_corr_point, eV)
    
    liq_peak_intens_solvent = solvent_sgnl[liq_peak_pos]
    liq_peak_intens_molec = molec_sgnl[liq_peak_pos]

    coeff = liq_peak_intens_molec / liq_peak_intens_solvent
    
    return coeff