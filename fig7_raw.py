# -*- coding: cp1250 -*-
import numpy as np

# load file fig7_raw.txt
data=np.loadtxt("fig7_raw.txt")

#mean value of thermal states 
mean_no=data[0][0]
mean_nq=data[0][1]
mean_ns=data[0][2]

#the standard deviation of thermal states 
std_nq=data[1][0]
std_nq=data[1][1]
std_ns=data[1][2]

#measured click statistics:
clicks_no=data[:,0][2:]
clicks_nq=data[:,1][2:]
clicks_ns=data[:,2][2:]

