#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:24:42 2022

@author: raketa
"""

import json

path_saving = '/home/raketa/Yandex.Disk/DIser/static plots/Hydrophobic/'





a = {
     'calibr_result': [1.91990228e-08, 1.06160969e+00],
     'harm': 19,
     'acc': 100000,
     'Sample_name': 'Pro, 100 mM.', 
     'date': '',  
     'double_gauss': 0,
     'open_folder': 0,
     'the_same_path': 1,
     'path_solvent': '/home/raketa/Data/18-08-21/' ,
     'path_molec': '/home/motilek/Data/20-03-11/20-15-34_/TOF/',
     'diff_spec_mult_av': 1,
     'diff_spec_mult_count': 1,
     'tof_list_mode': 0,
     'tof_arrays_solvent': [15, 17],
     'tof_arrays_molec': [10, 12],
     'main_plot_limits': [5, 15],
     'count_ylim': [8e-3, 1000],
     'av_ylim': [5e-8, 0.07],
     'diff_plot_lims': [5.0, 10.0],
     'diff_base_line_lims': [5, 9],
     'diff_approx_lims': [5.0, 7.0],
     'diff_ylims': [-10, 70],
     'diff_spec_ylim_av': [-1e-5, 2e-3],
     'diff_spec_ylim_count': [-10, 80],
     'diff_ylim_count': [-1, 75],
     'diff_ylim_av': [-1e-4, 2e-3],
     'diff_spec_xlim': [6, 9],
     'diff_spec_base_line_lims': [0, 5],
     'subplot_ylim_av': [-7e-6, 1e-5],
     'subplot_ylim_count': [-1, 1],
     'subplot_plot_limits': [5.0, 10.0],
     'ylims_diff_spec_analisys': [-1e-2, 5e-2],
     'diff_spec_analisys_mult': 1
         
     }


y = json.dumps(a, indent=4)
file_name = a['Sample_name'].replace(' ', '').replace(',', '_') + 'json'
jsonFile = open(file_name, "w")
jsonFile.write(y)
jsonFile.close()



#with open('Ala_1500.json') as json_file:
#    data = json.load(json_file)
    
#locals().update(a)