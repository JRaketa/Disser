# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:00:13 2017

@author: motilek
"""

def calibr_func(tt, t0, E0):  
    return 0.5/(1.6e-19)*9.10938356e-31*((0.767)/(tt-t0))**2-E0