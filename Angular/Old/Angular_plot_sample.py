from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import mpl_toolkits.mplot3d.axes3d as p3d
import time as ti

t0 = ti.time()

Hori = np.genfromtxt("/Users/perandersen/Data/DataCosmic/Hori_sub_spher_1.0_0.txt")
Hori = Hori[:,:]

Ra_hori = Hori[:,0]
Dec_hori = Hori[:,1]
Z_hori = Hori[:,2]

print "R: ", np.min(Z_hori), np.max(Z_hori)
map_hori = plt.get_cmap("Reds")
Colors_hori = Z_hori / 1000.0#np.max(Z_hori)

plt.figure()
plt.title("Hori")
plt.xlabel('Ra')
plt.ylabel('Dec')
plt.xlim((0,360))
plt.ylim((-90,90))
plt.scatter(Ra_hori,Dec_hori,c=Colors_hori,cmap=map_hori,edgecolors='none')

plt.figure()
plt.title("Z Hori")
plt.xlim((0,1000))
plt.hist(Z_hori,color='b',range=(0,1000),bins=20)
plt.figure()
plt.title("Ra Hori")
plt.xlim((0,360))
plt.hist(Ra_hori,color='b',range=(0,360),bins=20)
plt.figure()
plt.title("Dec Hori")
plt.xlim((-90,90))
plt.hist(Dec_hori,color='b',range=(-90,90),bins=20)

print "time: ", ti.time() - t0
plt.show()