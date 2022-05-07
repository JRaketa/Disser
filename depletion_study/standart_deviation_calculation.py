# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:09:32 2020

@author: motilek
"""

import numpy as np

def standart_deviation_calculation(pcov):                                       # pcov - Input
    standart_deviation = np.sqrt(np.diag(pcov))


    return standart_deviation