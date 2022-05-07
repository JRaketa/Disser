# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:50:52 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt


def base_line_correction(av_mode_spec_mean):
    
    
    ref_point = min(av_mode_spec_mean)
    ref_intens = av_mode_spec_mean[50]
    
    if ref_point < 0:
        av_mode_spec_mean = - av_mode_spec_mean
        
        av_mode_spec_mean += abs(ref_intens)
    
    
    
    return av_mode_spec_mean