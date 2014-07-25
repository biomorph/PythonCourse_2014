__author__ = 'ravi'

import numpy as np

import matplotlib.pyplot as plt
'''
x = np.arange(0,100)
y = 0.5 * x + 5 + 10*np.random.uniform(0,3,len(x))
plt.plot(x,y,'bo',label="Blue Circles")
#plt.show()

from scipy import stats

r_slope, r_int, r_rval, r_pval, r_stderr = stats.linregress(x, y)
plt.plot(x, x * r_slope + r_int, 'g-.', label='Dash-dotted Line')
plt.legend(["Noisy data", "Linear regression"], loc='lower right', numpoints=1,fancybox=True, shadow=True)

plt.savefig('plot.pdf',format='pdf')
'''

import pandas
import sys

cuffNorm = pandas.read_table('E_coli_genes.count_table.txt')

condition_pairs = [('control_20min_0','control_60min_0'),('control_20min_0','20bicyclomycin_20min_0'),('control_20min_0','100bicyclomycin_20min_0'),('20bicyclomycin_20min_0','100bicyclomycin_20min_0')]




FPKM_sample1 = list(cuffNorm[sys.argv[1]])
FPKM_sample2 = list(cuffNorm[sys.argv[2]])
'''
plt.scatter(FPKM_sample1,FPKM_sample2)

frame = plt.gca()
frame.axes.set_yscale('log')
frame.axes.set_xscale('log')

plt.xlim(1,1000000)
plt.ylim(1,1000000)
'''
plt.hist(FPKM_sample1,bins=range(0,1050,50),range=(0,1000),alpha=0.5)
frame = plt.gca()
frame.axes.get_xaxis().set_ticks(range(0,1050,50))
plt.show()
