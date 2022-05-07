# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:59:22 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

from PE_spec_formation import PE_spec_formation
from water_gas_peak_shift_calc import water_gas_peak_shift_calc
from eV_shift_correction import eV_shift_correction
from liq_peak_intens_corr_coeff_calc import liq_peak_intens_corr_coeff_calc 
from find_an_index import find_an_index 
from plot_formation_log import plot_formation_log 
from matrix_of_jacob_spec_formation import matrix_of_jacob_spec_formation
from diff_spec_matrix import diff_spec_matrix
from diff_spec_analisys import diff_spec_analisys 
from subplot_formation_log import subplot_formation_log
from diff_spectra_charcterization import diff_spectra_charcterization 
from scientific_not import scientific_not
from gas_peak_norm_coeff import gas_peak_norm_coeff
from liq_peak_diff_analisys import liq_peak_diff_analisys
import os
from PE_spec_formation_with_error import PE_spec_formation_with_error
from st_dev_calc import st_dev_calc
from matrix_shift_compensation import matrix_shift_compensation
from liq_peak_difference_calc import liq_peak_difference_calc
import json




with open('../params/Ile_50mM.json') as json_file:
    data = json.load(json_file)
    
locals().update(data)

count_divide = acc / 1000





print('--- --- --- --- --- --- ---')

print(Sample_name + date + ' H ' + str(harm))
print('--- --- --- --- --- --- ---')

diff_spec_legends = ['Diff spectra',
                     'Diff spec ext', 
                     'Gauss fit']


legends_av_1 = ['Reference','Sample','Diff spec']
legends_count_1 = ['Reference','Sample','Diff spec']
legends_count_2 = ['Reference','Sample','Diff spec']
legends_diff_spec_analisys = ['Reference','Sample','Diff spec', 'Diff spec at 11.31 eV']




title_1 = 'Static PES. Average mode'
title_2 = 'Static PES. Count mode'
title_diff_count = 'Diff spec. Count mode' 
title_diff_av = 'Diff spec. Average mode' 
title_diff_spec_analisys = 'Equal gas peak intensities. Average mode'

title_1 +=  '. ' + ' ' + Sample_name + ' '+ date
title_2 += '. ' + ' ' + Sample_name + ' '+ date
title_diff_count += '. ' + ' ' + Sample_name + ' '+ date
title_diff_av += '. ' + ' ' + Sample_name + ' '+ date
title_diff_spec_analisys += '. ' + ' ' + Sample_name + ' '+ date

if double_gauss == 1:
    diff_spec_legends = np.append(diff_spec_legends, 'gauss 1')
    diff_spec_legends = np.append(diff_spec_legends, 'gauss 2')


if the_same_path == 1:
    path_molec = path_solvent



matrix_rez = PE_spec_formation_with_error(path_solvent,
                                          tof_list_mode,
                                          tof_arrays_solvent,
                                          tof_arrays_molec,
                                          calibr_result,
                                          harm)

BE = matrix_rez[0]

av_solvent_matr = matrix_rez[1]
av_molec_matr  = matrix_rez[3]
count_solvent_matr  = matrix_rez[2] 
count_molec_matr  = matrix_rez[4]

av_solvent = np.mean(av_solvent_matr , axis = 0)
av_molec = np.mean(av_molec_matr , axis = 0)
count_solvent = np.mean(count_solvent_matr , axis = 0)
count_molec = np.mean(count_molec_matr , axis = 0)

count_solvent_matr[:] /= count_divide
count_molec_matr[:] /= count_divide




if diff_spec_mult_av != 1:
    legends_av_1[2] = legends_av_1[2] + ' * ' + str(diff_spec_mult_av)
if diff_spec_mult_count != 1:    
    legends_count_1[2] = legends_count_1[2] + ' * ' + str(diff_spec_mult_count)


dt_solvent = -  water_gas_peak_shift_calc(BE, av_solvent)
dt_molec = - water_gas_peak_shift_calc(BE, av_molec)


av_solvent_shift_corr = eV_shift_correction(BE, av_solvent, dt_solvent)
count_solvent_shift_corr = eV_shift_correction(BE, count_solvent, dt_solvent)

av_molec_shift_corr = eV_shift_correction(BE, av_molec, dt_molec)
count_molec_shift_corr = eV_shift_correction(BE, count_molec, dt_molec)


intens_coeff = liq_peak_intens_corr_coeff_calc(BE,
                                               av_solvent_shift_corr,
                                               av_molec_shift_corr,
                                               12.6)


count_solvent_shift_corr /= count_divide
count_molec_shift_corr /= count_divide



fig1 = plt.figure(1)
fig1.clf()
plot_formation_log(BE, 
                   av_solvent_shift_corr,
                   av_molec_shift_corr,
                   main_plot_limits,
                   av_ylim,
                   diff_plot_lims,
                   diff_spec_mult_av,
                   'linear',
                   legends_av_1,
                   title_1,
                   2)


plt.xlabel('BE, eV', fontsize = 14)
plt.ylabel('Signal, V', fontsize = 14)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
#plt.title(title_1)
scientific_not('y')

plt.text(6.5, 2.5e-02, '(a)', fontsize=20)

fig1.savefig('../figs/fig_1.png', dpi=100)

fig2 = plt.figure(2)
fig2.clf()
liq_peak_difference_calc(BE, av_solvent_shift_corr, 
                         av_molec_shift_corr, 
                         intens_coeff)

plt.xlabel('BE, eV', fontsize = 14)
plt.ylabel('Signal, V', fontsize = 14)
plt.xlim(main_plot_limits[0], main_plot_limits[1])
plt.ylim(av_ylim[0], av_ylim[1])
plt.legend(['Reference' + ' * ' + str(round(intens_coeff, 2)),'Sample','Diff'], 
            fontsize = 12)
plt.grid()
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
scientific_not('y')

plt.text(6.5, 2.5e-02, '(b)', fontsize=20)
fig2.savefig('../figs/fig_2.png', dpi=100)