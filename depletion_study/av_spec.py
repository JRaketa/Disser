# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:13:51 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt





def av_spec(path,
            tof_arrays,
            column):

    
    file = np.genfromtxt(path +'TOF_' + str(tof_arrays[0])+'.dat')            
    time_array =  file[:, 0]         
    
    av_array = np.zeros(len(time_array))  
    
    for n in tof_arrays:
        temp_file = np.genfromtxt(path +'TOF_' + str(n)+'.dat') 
        temp_sgnl = temp_file[:, column]
        av_array += temp_sgnl
        
    av_array[:] /= len(tof_arrays)    
               
          
    return av_array           