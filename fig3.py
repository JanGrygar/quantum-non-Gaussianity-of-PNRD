import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


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

# Data for \thermal stete ns:
data=np.loadtxt("fig3_ns.txt")
fig = plt.figure(figsize=(10, 6))
#bar of theoretical thermal state ns
plt.bar(data[:,0],data[:,1], color=(44/255., 180/255., 4/255.) ,align="center",width=0.7)
#reconstruct thermal state ns with errorbars:
plt.errorbar(data[:,0],data[:,2], yerr=data[:,3], fmt="o", capsize=12, capthick=3,color=(31/255., 119/255., 180/255.))

plt.yscale("log")
plt.ylabel(r" $p_{n} $")
plt.xlabel(r"n")
plt.xticks(np.arange(0,12,2))
plt.show()


data=np.loadtxt("fig3_nq.txt")
fig = plt.figure(figsize=(10, 6))
#bar of theoretical thermal state nq
plt.bar(data[:,0],data[:,1], color=(44/255., 180/255., 4/255.) ,align="center",width=0.7)
#reconstruct thermal state nq with errorbars:
plt.errorbar(data[:,0],data[:,2], yerr=data[:,3], fmt="o", capsize=12, capthick=3,color=(31/255., 119/255., 180/255.))

plt.yscale("log")
plt.ylabel(r" $p_{n} $")
plt.xlabel(r"n")
plt.xticks(np.arange(0,12,2))
plt.show()
