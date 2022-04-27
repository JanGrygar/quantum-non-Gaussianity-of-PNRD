import numpy as np


#open file with data:
out=open("fig4_raw_data.txt","r")

#The first line that contains measurement information:
a=out.readline()

#The second line contains a record of a coincidence for vacuum:
load_vacuum=out.readline()
vacuum=np.fromstring(load_vacuum, dtype=float, sep=',')
vacuum=np.delete(vacuum, -1)
data_vacuum=vacuum.reshape((int(len(vacuum)/17), 17))

#The third line contains a record of a coincidence for thermal state nQ:
load_nq=out.readline()
nq=np.fromstring(load_nq, dtype=float, sep=',')
nq=np.delete(nq, -1)
data_nq=nq.reshape((int(len(nq)/17), 17))


#The Fourth line contains a record of a coincidence for thermal state nS:
load_ns=out.readline()
ns=np.fromstring(load_ns, dtype=float, sep=',')
#ns=np.delete(ns, -1)
data_ns=ns.reshape((int(len(ns)/17), 17))