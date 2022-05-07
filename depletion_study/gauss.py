# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:33:04 2017

@author: motilek
"""



import numpy as np

def gauss(t, tm, A, delta, C):
        return A*np.exp(-((t-tm)**2)/(2*delta**2)) + C