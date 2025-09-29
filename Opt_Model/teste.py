import numpy as np

expo_i=-3
expo_f=3
kappa_i=10**expo_i
kappa_f=10**expo_f
expo=np.linspace(expo_i, expo_f, num=10)

d_kappa=(10*np.ones(10))**expo

print(d_kappa)