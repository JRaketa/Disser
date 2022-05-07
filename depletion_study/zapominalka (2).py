#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 00:55:55 2018

@author: motilek
"""

array=[[1],[2]]

#subject='times_for_calibration_'

name='Water_eV_'
sample='_10mM_salt_17_Harm_counts_100000_88-95_'
date='19_06_18'
specification_1='_Refer_eV_fixed_intensities'
specification_2='_Spec_diff_cutted'
specification_3='_Spec_cutted'

specification_4='_Reference_water_Full'
specification_5='_Spec_diff_full'
specification_6='_Spec_full'


#name=specification+sample+date
path='/home/motilek/Yandex.Disk/processed_data/dates/19.06.18/'
#name+'.txt'
#the_first_row=cutted_time
#the_second_row=cutted_spec                       #here

with open(path+name+sample+date+specification_6+'.txt', 'w') as hui:
    for i,k in zip(eV, Counts):
        hui.write('{} {} \n'.format(i,k))
        
#with open(path+name+sample+date+specification_2+'.txt', 'w') as hui:
#    for i,k in zip(cutted_time, spec_diff):
#        hui.write('{} {} \n'.format(i,k))
        
#with open(path+name+sample+date+specification_3+'.txt', 'w') as hui:
#    for i,k in zip(cutted_time, cutted_spec):
#        hui.write('{} {} \n'.format(i,k))        


#with open(path+name+sample+date+specification_6+'.txt', 'w') as hui:
#    for i,k in zip(ttime, full_spec):
#        hui.write('{} {} \n'.format(i,k))
        
#with open(path+name+sample+date+specification_4+'.txt', 'w') as hui:
#    for i,k in zip(ttime, ref_full):
#        hui.write('{} {} \n'.format(i,k))
        
#with open(path+name+sample+date+specification_5+'.txt', 'w') as hui:
#    for i,k in zip(ttime, spec_diff_full):
#        hui.write('{} {} \n'.format(i,k))       
        
        
        
        
        
        
        