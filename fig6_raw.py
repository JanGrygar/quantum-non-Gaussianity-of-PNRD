# -*- coding: cp1250 -*-
import numpy as np

# load file fig4_raw.txt
data=np.loadtxt("fig6_raw.txt")



# POVM 1:
povm1_mean_nq=data[0][1]
povm1_mean_ns=data[0][2]
povm1_std_nq=data[1][1]
povm1_std_ns=data[1][2]
povm1_clicks_noise=data[:,0][2:13]
povm1_clicks_nq=data[:,1][2:13]
povm1_clicks_ns=data[:,2][2:13]

# POVM 2:
povm2_mean_nq=data[13][1]
povm2_mean_ns=data[13][2]
povm2_std_nq=data[14][1]
povm2_std_ns=data[14][2]
povm2_clicks_noise=data[:,0][15:26]
povm2_clicks_nq=data[:,1][15:26]
povm2_clicks_ns=data[:,2][15:26]

# POVM 3:
povm3_mean_nq=data[26][1]
povm3_mean_ns=data[36][2]
povm3_std_nq=data[27][1]
povm3_std_ns=data[27][2]
povm3_clicks_noise=data[:,0][28:39]
povm3_clicks_nq=data[:,1][28:39]
povm3_clicks_ns=data[:,2][28:39]

# POVM 4:
povm4_mean_nq=data[39][1]
povm4_mean_ns=data[39][2]
povm4_std_nq=data[40][1]
povm4_std_ns=data[40][2]
povm4_clicks_noise=data[:,0][41:52]
povm4_clicks_nq=data[:,1][41:52]
povm4_clicks_ns=data[:,2][41:52]

# POVM 5:
povm5_mean_nq=data[52][1]
povm5_mean_ns=data[52][2]
povm5_std_nq=data[53][1]
povm5_std_ns=data[53][2]
povm5_clicks_noise=data[:,0][54:65]
povm5_clicks_nq=data[:,1][54:65]
povm5_clicks_ns=data[:,2][54:65]

# POVM 6:
povm6_mean_nq=data[65][1]
povm6_mean_ns=data[65][2]
povm6_std_nq=data[66][1]
povm6_std_ns=data[66][2]
povm6_clicks_noise=data[:,0][67:78]
povm6_clicks_nq=data[:,1][67:78]
povm6_clicks_ns=data[:,2][67:78]

# POVM 7:
povm7_mean_nq=data[78][1]
povm7_mean_ns=data[78][2]
povm7_std_nq=data[79][1]
povm7_std_ns=data[79][2]
povm7_clicks_noise=data[:,0][80:]
povm7_clicks_nq=data[:,1][80:]
povm7_clicks_ns=data[:,2][80:]