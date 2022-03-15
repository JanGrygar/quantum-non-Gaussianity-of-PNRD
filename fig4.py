# -*- coding: cp1250 -*-
import numpy as np
from matplotlib import pyplot as plt
import time as tm
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib




#parameters of figure:
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


# An analytical description of  threshold, equation (2)
def threshol_parameter_t(t,v): 
    p=((2*np.sqrt(v))/(v+1))*np.exp(-1*(1-v)*(2 -t +t*v)/(2*v*(2*v + t - t*v )))
    q=((2*np.sqrt(v))/np.sqrt((t*v+2-t)*(t+2*v-t*v))) *np.exp(-t*(1-v**2)/(2*v*(2*v -t*v +t)))
    return(p,q)

osa=np.linspace(0.04,1,300)
threshold=np.zeros((300,2))
T=0.481

# Calculation of the threshold for negausovast:
po=0
for i in osa:
    b=threshol_parameter_t(T,i)
    threshold[po][0]=b[0]
    threshold[po][1]=b[1]
    po=po+1


# load data
data=np.loadtxt("fig4.txt")


fig = plt.figure(figsize=(12, 8))
plt.plot(threshold[:,0],threshold[:,1],color="crimson") # plot Threshold

for x in range(0,9):
    if x>2: # simulation data
        plt.errorbar(data[x][0],data[x][1],xerr=[[data[x][2]], [ data[x][3]]], yerr=[[data[x][4]], [data[x][5]]] ,fmt="o",color="#10eda9",markersize=8,capsize=5,elinewidth=2,capthick=2, )
    else: # measured data 
        plt.errorbar(data[x][0],data[x][1],xerr=[[data[x][2]], [ data[x][3]]], yerr=[[data[x][4]], [data[x][5]]] ,fmt="o",color="#6051A7",markersize=8,capsize=5,elinewidth=2,capthick=2)


plt.xscale("log")
plt.yscale("log")
plt.xlabel(r"$\widetilde{P}_{0}$ ")
plt.ylabel(r"$\widetilde{Q}_{0}$ ")
plt.xlim(1e-15,1)
plt.ylim(1e-4,1)
plt.show()