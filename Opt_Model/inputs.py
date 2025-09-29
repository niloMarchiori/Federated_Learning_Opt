import constants as ctt
import numpy as np

np.random.seed(60)
#pos
d=np.random.uniform(*ctt.d_range,size=ctt.N)

#Com
B=ctt.B*1e6  # Convert MHz to Hz
pmin=ctt.p_range[0]*np.ones(ctt.N)
pmax=ctt.p_range[1]*np.ones(ctt.N)
h=ctt.g0*(ctt.d0/d)**4
s=ctt.s*np.ones(ctt.N)*1000  # Convert KB to Bytes
N0=ctt.N0

N0=ctt.sigma  # Use sigma as N0 in Watts
g0_linear = 10**(ctt.g0 / 10)  # Convert dB to linear scale
h=g0_linear*(ctt.d0/d)**4
s=25000*np.ones(ctt.N)  # Convert KB to nats

#Cmp
D=np.random.uniform(*ctt.D_range,size=ctt.N)*10**6  # Convert MB to bits
c=np.random.uniform(*ctt.c_range,size=ctt.N)
fmin=ctt.fmin*np.ones(ctt.N) * 10**9  # GHz to Hz
fmax=np.random.uniform(*ctt.fmax_range,size=ctt.N)*10**9  # GHz to Hz

