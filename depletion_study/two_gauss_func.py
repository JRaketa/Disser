# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:05:41 2020

@author: motilek
"""

import numpy as np

def two_gauss_func(t,t_1,a_1, b_1, t_2, a_2, b_2, A):
    return a_1*np.exp(-((t-t_1)**2)/(2*b_1**2))+a_2*np.exp(-((t-t_2)**2)/(2*b_2**2))+A