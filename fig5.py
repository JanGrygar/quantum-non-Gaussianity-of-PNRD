# -*- coding: cp1250 -*-
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from lib_function import *


# An analytical description of  threshold, equation (2)
def threshol_parameter_t(t,v): 
    p=((2*np.sqrt(v))/(v+1))*np.exp(-1*(1-v)*(2 -t +t*v)/(2*v*(2*v + t - t*v )))
    q=((2*np.sqrt(v))/np.sqrt((t*v+2-t)*(t+2*v-t*v))) *np.exp(-t*(1-v**2)/(2*v*(2*v -t*v +t)))
    return(p,q)


#paremetrs of figure:
SMALL_SIZE = 26
MEDIUM_SIZE = 30
BIGGER_SIZE = 32
    
plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.rc("errorbar", capsize=2)
plt.rc('lines', markersize = 4)
plt.rc('text.latex', preamble=r'\usepackage{textgreek}')
matplotlib.rcParams['text.usetex'] = True


#load data:
theoretical_lines=np.loadtxt("fig5_theoretical_curve.txt")
data_povm=np.loadtxt("fig5.txt")


# Calculation of the threshold for negausovast:
T=0.5
threshold=np.zeros((300,2))
osa=np.linspace(0.04,1,300)

po=0
for v in osa:
    a=threshol_parameter_t(T,v)
    threshold[po][0]=a[0]
    threshold[po][1]=a[1]
    po=po+1


fig = plt.figure(figsize=(10, 6))

# plot of threshold:
plt.plot(threshold[:,0],threshold[:,1],color="crimson",label="Threshold")

# plot of ttheoretical curve:
for i in [0,1,2]:
    plt.plot(theoretical_lines[:,i],theoretical_lines[:,i+3], linestyle="--", color="lightgrey",label="POVM "+str(i))

# plot data:
for i in range(24):
    if i<8:
        plt.errorbar(data_povm[i][0],data_povm[i][1],xerr=data_povm[i][2],yerr=data_povm[i][3],fmt="s",color=(25/255.,130/255.,196/255.),capsize=6,elinewidth=3,barsabove=3,markersize=6) #label="POVM"+str(i)
    elif 7<i<16:
        plt.errorbar(data_povm[i][0],data_povm[i][1],xerr=data_povm[i][2],yerr=data_povm[i][3],fmt="s",color=(127/255., 0/255., 255/255.),capsize=6,elinewidth=3,barsabove=3,markersize=6) #label="POVM"+str(i)
    else:
        plt.errorbar(data_povm[i][0],data_povm[i][1],xerr=data_povm[i][2],yerr=data_povm[i][3],fmt="s",color=(247/255.,157/255.,101/255.),capsize=6,elinewidth=3,barsabove=3,markersize=6) #label="POVM"+str(i)


plt.xscale("log")
plt.yscale("log")
plt.xlabel(r"$\widetilde{P}_{0}$ ")
plt.ylabel(r"$\widetilde{Q}_{0}$ ")
plt.xlim(1e-9,2)
plt.ylim(8e-3,1)
plt.show()