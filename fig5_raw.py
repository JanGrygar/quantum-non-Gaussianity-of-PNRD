# -*- coding: cp1250 -*-
import numpy as np

# load file fig5_raw.txt,
data=np.loadtxt("fig5_raw.txt")


# point 1:
point1_mean_ns=data[0][1]
point1_mean_nq=data[0][2]
point1_std_ns=data[1][1]
point1_std_nq=data[1][2]
point1_clicks_noise=data[:,0][2:13]
point1_clicks_ns=data[:,1][2:13]
point1_clicks_nq=data[:,2][2:13]

# point 2:
point2_mean_ns=data[13][1]
point2_mean_nq=data[13][2]
point2_std_ns=data[14][1]
point2_std_nq=data[14][2]
point2_clicks_noise=data[:,0][15:26]
point2_clicks_ns=data[:,1][15:26]
point2_clicks_nq=data[:,2][15:26]

# point 3:
point3_mean_ns=data[26][1]
point3_mean_nq=data[36][2]
point3_std_ns=data[27][1]
point3_std_nq=data[27][2]
point3_clicks_noise=data[:,0][28:39]
point3_clicks_ns=data[:,1][28:39]
point3_clicks_nq=data[:,2][28:39]

# point 4:
point4_mean_ns=data[39][1]
point4_mean_nq=data[39][2]
point4_std_ns=data[40][1]
point4_std_nq=data[40][2]
point4_clicks_noise=data[:,0][41:52]
point4_clicks_ns=data[:,1][41:52]
point4_clicks_nq=data[:,2][41:52]

# point 5:
point5_mean_ns=data[52][1]
point5_mean_nq=data[52][2]
point5_std_ns=data[53][1]
point5_std_nq=data[53][2]
point5_clicks_noise=data[:,0][54:65]
point5_clicks_ns=data[:,1][54:65]
point5_clicks_nq=data[:,2][54:65]

# point 6:
point6_mean_ns=data[65][1]
point6_mean_nq=data[65][2]
point6_std_ns=data[66][1]
point6_std_nq=data[66][2]
point6_clicks_noise=data[:,0][67:78]
point6_clicks_ns=data[:,1][67:78]
point6_clicks_nq=data[:,2][67:78]

# point 7:
point7_mean_ns=data[78][1]
point7_mean_nq=data[78][2]
point7_std_ns=data[79][1]
point7_std_nq=data[79][2]
point7_clicks_noise=data[:,0][80:91]
point7_clicks_ns=data[:,1][80:91]
point7_clicks_nq=data[:,2][80:91]

# point 8:
point8_mean_ns=data[91][1]
point8_mean_nq=data[91][2]
point8_std_ns=data[92][1]
point8_std_nq=data[92][2]
point8_clicks_noise=data[:,0][93:104]
point8_clicks_ns=data[:,1][93:104]
point8_clicks_nq=data[:,2][93:104]

# point 9:
point9_mean_ns=data[104][1]
point9_mean_nq=data[104][2]
point9_std_ns=data[105][1]
point9_std_nq=data[105][2]
point9_clicks_noise=data[:,0][106:117]
point9_clicks_ns=data[:,1][106:117]
point9_clicks_nq=data[:,2][106:117]

# point 10:
point10_mean_ns=data[117][1]
point10_mean_nq=data[117][2]
point10_std_ns=data[118][1]
point10_std_nq=data[118][2]
point10_clicks_noise=data[:,0][119:]
point10_clicks_ns=data[:,1][119:]
point10_clicks_nq=data[:,2][119:]


