# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:46:40 2020

@author: motilek
"""

def invert_calibr_func(Ek, E0, t0):
    return (9.10938356e-31/(2*1.6e-19*(Ek + E0)))**0.5*0.767 + t0