import inputs as inp
import constants as ctt
import numpy as np
import pandas as pd
from sub1 import solve_SUB1
from sub2 import solve_SUB2
from sub3 import solve_SUB3
from analisys import plot_sub1, plot_sub2, plot_sub3

expo_i=-3
expo_f=3
kappa_i=10**expo_i
kappa_f=10**expo_f
expo=np.linspace(expo_i, expo_f, num=10000)

d_kappa=(10*np.ones(10000))**expo

sub1={'F': [], 'Tcmp': [], 'kappa': []}
sub2={'Tcom': [], 't': [], 'p':[],'kappa': []}
sub3={'theta': [], 'eta': [], 'kappa': []}

for k in d_kappa:
    T_cmp, f = solve_SUB1(kappa=k)
    sub1['F'].append(f)
    sub1['Tcmp'].append(T_cmp)
    sub1['kappa'].append(k)

    Tcom, t,p = solve_SUB2(ctt.N, kappa=k, s=inp.s, B=inp.B, N0=inp.N0, h=inp.h, pmin=inp.pmin, pmax=inp.pmax)
    sub2['Tcom'].append(Tcom)
    sub2['t'].append(t)
    sub2['p'].append(p)
    sub2['kappa'].append(k)

    thteta, eta = solve_SUB3(f, t, T_cmp, Tcom, k)
    sub3['theta'].append(thteta)
    sub3['eta'].append(eta)
    sub3['kappa'].append(k)

#Convert to DataFrame
df_sub1 = pd.DataFrame(sub1)
df_sub2 = pd.DataFrame(sub2)
df_sub3 = pd.DataFrame(sub3)
print(df_sub1)
print(df_sub2)

#Plot the results
plot_sub1(df_sub1)
plot_sub2(df_sub2)
plot_sub3(df_sub3)
df_sub1.to_csv('sub1_results.csv', index=False)
df_sub2.to_csv('sub2_results.csv', index=False)
df_sub3.to_csv('sub3_results.csv', index=False)