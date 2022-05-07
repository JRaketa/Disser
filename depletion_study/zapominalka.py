#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 00:55:55 2018

@author: motilek
"""

array=[[1],[2]]

#subject='times_for_calibration_'

name='Glu_10mM'
sample='_10mM_salt_17_Harm_cc_100000_33-37_eV_Kin'
date='16_10_18'
specification_1='_Refer_eV_full_'
#specification_2='_Spec_diff_cutted'
specification_3='_Spec_full'

#specification_4='_Reference_water_Full'
#specification_5='_Spec_diff_full'
specification_6='_Spec_full'


#name=specification+sample+date
path='/home/motilek/Yandex.Disk/processed_data/dates/16.10.18/Glu/'
                     #here

with open(path+name+sample+date+'.txt', 'w') as hui:
    for i,k,j,m,t in zip(eV, Counts, Aver, err_count_mode, err_aver_mode):
        hui.write('{} {} {} {} {}\n'.format(i,k,j,m,t))
        


        
        
        
        