# # Author G. Macario, INAF-Arcetri Astrophysical Observatory
# Sept 08, 2023 - IAU/I-HOW RADIO ASTRONOMY 2023, Kayseri, Turkey
#
# This script produce an error bar plot of the integrated spectrum of the East Relic source in Abell 3365 galaxy cluster, 
# from flux density eastimates derived in step 3) of Continuum project #1, "Multi-frequency view of Abell 3365 (MeerKAT and Gleam X)"
# The flux measurements are already in the S_mJy array; the student will do the measurements following the tutorial and should find the values to those reported here.
#

import numpy as np
import matplotlib.pyplot as plt
import math

# Frequency array in MHz  
nu_MHz = np.array([87.5,118.5,154.5,185.5,215.5,908,952,996,1044,1093,1145,1318,1382,1448,1482,1594,1656])

# Flux measurements array in mJy (step 3) of the tutorial 
S_mJy = np.array([324,323,264,199,178,74,67.5,67.5,61.8,54.9,46.9,37.8,36.3,33.3,30.1,22.2,25.4])


# Assumed uncertainty on all flux measurements is of 15%. This is a basic conservative estimate but it is probably wrong, to simplify the project; 
# A proper estimate of errors is beyond this exercise, as it would require an accurate analysis and previous knowledge in this research field. 
e_S =0.15*S      

# Errorbar plot of the spectrum
fig = plt.figure()
ax = fig.add_subplot(111)

formattedPlot = plt.errorbar(nu_MHz, S_mJy, e_S, fmt = 'ko', markersize = 6,\
    capsize = 5, linewidth = 1.5, markerfacecolor = 'y');

plt.xlabel('Frequency (MHz)', fontsize = 14, fontname = 'Times')
plt.ylabel('Flux density (mJy)', fontsize = 14, fontname = 'Times')
plt.yscale('log')
plt.xscale('log')
plt.axis((70, 2000, 10, 1000));
plt.show()

#Computing spectra indexes in different frequency intervals, assuming power-law spectra 

alpha_87_215 = math.log10(S_mJy[0]/S_mJy[4])/math.log10(nu_MHz[0]/nu_MHz[4])
print('alpha_1 =',alpha_87_215, '; spectral index of a power-law between 87.5 and 215.5 MHz')

alpha_215_908 = math.log10(S_mJy[4]/S_mJy[5])/math.log10(nu_MHz[4]/nu_MHz[5])
print('alpha_2 =',alpha_215_908,  '; spectral index of a power-law between 215.5 and 908 MHz')


alpha_908_1656 = math.log10(S_mJy[5]/S_mJy[16])/math.log10(nu_MHz[5]/nu_MHz[16])
print('alpha_3 =',alpha_908_1656,  '; spectral index of a power-law between 908 and 1656 MHz')

 

