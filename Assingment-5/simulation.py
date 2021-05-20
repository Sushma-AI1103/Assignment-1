# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xzheCZXERRuNFCVT3Va_n1H8kWOPC3Xu
"""

import matplotlib.pyplot as plt
from scipy.stats import poisson
import numpy as np
f = plt.figure(figsize=(18, 10))
 
def plotHist(nr, N, n_, mean, var0, x0):
    x = np.zeros((N))
    sp = f.add_subplot(4, 1, n_ )
    
    for i in range(N):    
        for j in range(nr):
            x[i] += np.random.poisson(mean) 
        x[i] *= 1/nr
    plt.hist(x, 100, density=True, color='#348ABD', label=" %d RVs"%(nr));
    plt.setp(sp.get_yticklabels(), visible=False)
    
    variance = var0/nr                     
    fac = 1/np.sqrt(2*np.pi*variance)
    dist = fac*np.exp(-(x0-mean)**2/(2*variance))
    plt.plot(x0,dist,color='#A60628',linewidth=3,label='CLT',alpha=0.8)
    plt.xlabel('r')
    plt.xlim([0, 2])
    leg = plt.legend(loc="upper right")
    leg.get_frame().set_alpha(0.1)

    
N = 10000   # number of samples taken
nr = ([32, 64, 128,256])

mean, var0 = 1, 1  # mean and variance 
x0 = np.linspace(0, 2, 256)

for i in range(np.size(nr)):
    plotHist(nr[i], N, i+1, mean, var0, x0)

plt.suptitle("Addition of Poisson distributed RVs converge to a Normal distribution",fontsize=20);

mu = int(1e5)
sum =0 
for i in range(0,mu+1):
  sum = sum + poisson.pmf(i,mu)

print("value coming from addition is approximately equal to standard normal distribution :\n")
print(sum)