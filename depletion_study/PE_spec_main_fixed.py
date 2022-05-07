# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:59:22 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

import PE_spec_formation as PE_spec_formation
import water_gas_peak_shift_calc as water_gas_peak_shift_calc
import eV_shift_correction as eV_shift_correction
import liq_peak_intens_corr_coeff_calc as liq_peak_intens_corr_coeff_calc 
import find_an_index as find_an_index 
import plot_formation_log as plot_formation_log 
import matrix_of_jacob_spec_formation as matrix_of_jacob_spec_formation
import diff_spec_matrix as diff_spec_matrix
import diff_spec_analisys as diff_spec_analisys 
import subplot_formation_log as subplot_formation_log
import diff_spectra_charcterization_fixed as diff_spectra_charcterization_fixed 
import scientific_not as scientific_not
import gas_peak_norm_coeff as gas_peak_norm_coeff
import liq_peak_diff_analisys as liq_peak_diff_analisys
import os
import PE_spec_formation_with_error as PE_spec_formation_with_error
import st_dev_calc as st_dev_calc
import matrix_shift_compensation as matrix_shift_compensation
import liq_peak_difference_calc as liq_peak_difference_calc


liq_peak_difference_calc = liq_peak_difference_calc.liq_peak_difference_calc
matrix_shift_compensation = matrix_shift_compensation.matrix_shift_compensation
st_dev_calc = st_dev_calc.st_dev_calc
PE_spec_formation_with_error = PE_spec_formation_with_error.PE_spec_formation_with_error
liq_peak_diff_analisys = liq_peak_diff_analisys.liq_peak_diff_analisys
gas_peak_norm_coeff = gas_peak_norm_coeff.gas_peak_norm_coeff
scientific_not = scientific_not.scientific_not
diff_spectra_charcterization_fixed = diff_spectra_charcterization_fixed.diff_spectra_charcterization
subplot_formation_log = subplot_formation_log.subplot_formation_log
diff_spec_analisys = diff_spec_analisys.diff_spec_analisys
diff_spec_matrix = diff_spec_matrix.diff_spec_matrix
matrix_of_jacob_spec_formation = matrix_of_jacob_spec_formation.matrix_of_jacob_spec_formation
plot_formation_log = plot_formation_log.plot_formation_log
find_an_index = find_an_index.find_an_index
liq_peak_intens_corr_coeff_calc = liq_peak_intens_corr_coeff_calc.liq_peak_intens_corr_coeff_calc
eV_shift_correction = eV_shift_correction.eV_shift_correction
water_gas_peak_shift_calc = water_gas_peak_shift_calc.water_gas_peak_shift_calc
PE_spec_formation = PE_spec_formation.PE_spec_formation



#                   1.91990228e-08, 5.14155482e-01
#                   open_folder = 0








make_new_input = 0
make_new_output = 0



path_saving = '/home/raketa/Yandex.Disk/DIser/static plots/Hydrophobic/'






acalibr_result = [1.91990228e-08, 5.14155482e-01]
harm = 17
acc = 10000
Sample_name = 'Ala, 1500 mM.'
date = ''

double_gauss = 0

open_folder = 0

the_same_path = 1
path_solvent = '/home/raketa/Data/18-03-20/'                               
path_molec = '/home/motilek/Data/20-03-11/20-15-34_/TOF/'        

#path_saving = '/home/raketa/Yandex.Disk/processed_data/Static_data/plots/Gly 800, 20.03.18/'


path_saving = path_saving + Sample_name + date

diff_spec_mult_av = 1
diff_spec_mult_count = 1

tof_list_mode = 0
tof_arrays_solvent = [2]                                               
tof_arrays_molec = [25, 29] 

main_plot_limits = [5, 15]
count_ylim = [1e-1, 1000]
av_ylim = [5e-7, 0.07]

diff_plot_lims = [5.0, 10.0]

diff_base_line_lims = [0, 4]
diff_approx_lims = [5.0, 7.0]
diff_ylims = [-10, 70]

diff_spec_ylim_av = [-1e-5, 2e-3] #
diff_spec_ylim_count = [-10, 80] #

###############  its subplots ################

diff_ylim_count = [-1, 75]
diff_ylim_av = [-1e-4, 2e-3]

############  difff specs subplots ###########

diff_spec_xlim = [5, 9.5]
diff_spec_base_line_lims = [0, 5]


subplot_ylim_av = [-7e-6, 1e-5]
subplot_ylim_count = [-1, 1]

subplot_plot_limits = [7.0, 10.5]


############### diff spec analisys ################


ylims_diff_spec_analisys = [-1e-2, 5e-2]
diff_spec_analisys_mult = 1


#plt.bar(2, height = 5, width = 5, bottom = 6, alpha = 0.15, color = 'C0')





















































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

#solvent_rez = PE_spec_formation(path_solvent,
#                                tof_list_mode,
#                                tof_arrays_solvent,
#                                calibr_result,
#                                harm)

#molec_rez = PE_spec_formation(path_molec,
#                              tof_list_mode,
#                              tof_arrays_molec,
#                              calibr_result,
#                              harm)

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
#spec_matrix_solvent = matrix_of_jacob_spec_formation(path_solvent,
##                                                     tof_list_mode,
#                                                    tof_arrays_solvent,
#                                                     calibr_result,
#                                                     harm)

#spec_matrix_molec = matrix_of_jacob_spec_formation(path_solvent,
#                                                   tof_list_mode,
#                                                   tof_arrays_molec,
##                                                   calibr_result,
 #                                                  harm)

#BE = spec_matrix_solvent[0]

#av_solvent = spec_matrix_solvent[1]
#count_solvent = spec_matrix_solvent[2]

#av_mol = spec_matrix_molec[1]
#count_mol = spec_matrix_molec[2]



#diff_matrix_rez = diff_spec_matrix(spec_matrix_solvent,
#                           spec_matrix_molec)                                   #matrix of diff spectra

#av_diff_matrix = diff_matrix_rez[0]
#count_diff_matrix = diff_matrix_rez[1]


#mean_av_solvent = np.mean(av_solvent , axis = 0)
#mean_count_solvent = np.mean(count_solvent , axis = 0)

#mean_av_molec = np.mean(av_mol , axis = 0)
#mean_count_molec = np.mean(count_mol , axis = 0)

#mean_diff_av = np.mean(av_diff_matrix , axis = 0)
#mean_diff_count = np.mean(count_diff_matrix , axis = 0)

#ind_11_31 = find_an_index(11.31, BE)
#solv_intens = mean_av_solvent [ind_11_31]
#molec_intens = mean_av_molec [ind_11_31]
#norm_coeff =  solv_intens / molec_intens

#mean_av_solvent /= norm_coeff
#mean_count_solvent /= norm_coeff



if diff_spec_mult_av != 1:
    legends_av_1[2] = legends_av_1[2] + ' * ' + str(diff_spec_mult_av)
if diff_spec_mult_count != 1:    
    legends_count_1[2] = legends_count_1[2] + ' * ' + str(diff_spec_mult_count)







dt_solvent = -  water_gas_peak_shift_calc(BE, av_solvent)
dt_molec = - water_gas_peak_shift_calc(BE, av_molec)

av_shift_comp_matr_solvent = matrix_shift_compensation(dt_solvent, BE, av_solvent_matr)
count_shift_comp_matr_solvent = matrix_shift_compensation(dt_solvent, BE, count_solvent_matr)

av_shift_comp_matr_molec = matrix_shift_compensation(dt_molec, BE, av_molec_matr)
count_shift_comp_matr_molec = matrix_shift_compensation(dt_molec, BE, count_molec_matr)

#solvent_count_error /= count_divide
#molec_count_error /= count_divide

##solvent_av_error = st_dev_calc(av_shift_comp_matr_solvent)
##solvent_count_error = st_dev_calc(count_shift_comp_matr_solvent)
##molec_av_error = st_dev_calc(av_shift_comp_matr_molec)
##molec_count_error = st_dev_calc(count_shift_comp_matr_molec)


    

av_solvent_shift_corr = eV_shift_correction(BE, av_solvent, dt_solvent)
count_solvent_shift_corr = eV_shift_correction(BE, count_solvent, dt_solvent)

av_molec_shift_corr = eV_shift_correction(BE, av_molec, dt_molec)
count_molec_shift_corr = eV_shift_correction(BE, count_molec, dt_molec)

intens_coeff = liq_peak_intens_corr_coeff_calc(BE,
                                               av_solvent_shift_corr,
                                               av_molec_shift_corr,
                                               11.31)


count_solvent_shift_corr /= count_divide
count_molec_shift_corr /= count_divide



legends_av_1[0] = legends_av_1[0] + ' * ' + str(np.round(intens_coeff, 2))
legends_count_1[0] = legends_count_1[0] + ' * ' + str(np.round(intens_coeff, 2))

#intens_coeff_count = liq_peak_intens_corr_coeff_calc(BE,
#                                                     count_solvent_shift_corr,
#                                                     count_molec_shift_corr,
#                                                     11.31)                                               

av_solvent_intens_corr = av_solvent_shift_corr * intens_coeff
count_solvent_intens_corr = count_solvent_shift_corr * intens_coeff 

#solvent_av_error[:] *= intens_coeff
#solvent_count_error[:] *=intens_coeff

##plt.figure(7)
##plt.clf()
##a = np.shape(count_shift_comp_matr_molec)[0]
##plt.plot(BE,count_solvent_intens_corr )
##plt.plot(BE, )

#for n in range(a):
#    plt.plot(BE, count_shift_comp_matr_molec[n])
#plt.errorbar(BE,
#             count_solvent_intens_corr,
#             yerr = solvent_count_error)
#plt.errorbar(BE,
#             count_molec_shift_corr,
#             yerr = molec_count_error)
plt.xlim(5, 15)
plt.ylim(-5, 50)





diff_plot_ind = [find_an_index(diff_plot_lims[0], BE),
                               find_an_index(diff_plot_lims[1], BE)]


fig1 = plt.figure(1)
fig1.clf()
plot_formation_log(BE, 
                   av_solvent_intens_corr,
                   av_molec_shift_corr,
                   main_plot_limits,
                   av_ylim,
                   [5, 9.5],
                   diff_spec_mult_av,
                   'log',
                   legends_av_1,
                   title_1)

plt.xlabel('BE, eV', fontsize = 12)
plt.ylabel('Signal, V', fontsize = 12)


plt.text(5.15, 2e-4, "(a)", fontsize=20)


plt.ylabel('Signal, Counts / sec')


#######################################################

fig4 = plt.figure(4)
plt.clf()
#plt.title(title_diff_count)
print('Count mode')
diff_spectra_charcterization_fixed(BE, 
                             count_solvent_intens_corr,
                             count_molec_shift_corr,
                             diff_spec_base_line_lims,
                             diff_spec_xlim,
                             diff_spec_ylim_count,
                             0,
                             double_gauss)

plt.xlim(6, 10)
plt.xlabel('BE, eV',fontsize = 12)
plt.ylabel('Signal, Counts / sec', fontsize = 12)

plt.legend(diff_spec_legends, loc = 2, fontsize = 12)


plt.text(6.06, 25, "(b)", fontsize=20)

            
            
            
            
            
            
            
            
            
            
            
            
            