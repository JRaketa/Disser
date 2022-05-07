#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:20:42 2020

@author: raketa
"""


import numpy as np
import matplotlib.pyplot as plt


def scientific_not(ax):
    plt.ticklabel_format(axis=ax, style="sci", scilimits=(0,0))
    
    return


# ax: "x" or "y"