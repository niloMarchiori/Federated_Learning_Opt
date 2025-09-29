import inputs as inp
import constants as ctt
import numpy as np

def get_TN3(N3,alpha,c,D,kappa):
    T_N3=0
    for ue in N3:
        T_N3+=alpha*(c[ue]*D[ue])**3/kappa
    return T_N3**(1/3)

def get_TN2(N2,c,D,fmin):
    if not N2:
        return -1
    times=[]
    for ue in N2:
        times.append(c[ue]*D[ue]/fmin[ue])

    T_N2=max(times)
    return T_N2

def solve_SUB1(kappa,N=ctt.N,alpha=ctt.alpha,D=inp.D,c=inp.c,fmin=inp.fmin,fmax=inp.fmax):
    max_time=c*D/fmin
    UES = np.array(list(enumerate(max_time)))
    ordened_UES=UES[UES[:,1].argsort()]

    min_time=c*D/fmax
    min_time=np.array(list(enumerate(min_time)))
    bottle_neck=max(min_time, key=lambda x: x[1])
    T_N1=bottle_neck[1]

    N1=[]
    N2=[]
    N3=[x for x in range(N)]

    T_N3=get_TN3(N3,alpha,c,D,kappa)

    for i in range(N):
        if not N1:
            if bottle_neck[1]>=T_N3:
                N1.append(int(bottle_neck[0]))
                N3.pop(N3.index(bottle_neck[0]))
                T_N3=get_TN3(N3,alpha,c,D,kappa)
        if ordened_UES[i][1]<=T_N3:
            ue=int(ordened_UES[i][0])
            N2.append(ue)
            N3.pop(N3.index(ue))
            T_N3=get_TN3(N3,alpha,c,D,kappa)
    T_N2=get_TN2(N2,c,D,fmin)
    T_cmp=round(max(T_N3, T_N2, T_N1), 2)
    f=np.zeros(N)
    for ue in N1:
        f[ue]=round(fmax[ue]/10**9  , 2)
    for ue in N2:
        f[ue]=round(fmin[ue]/10**9  , 2)
    for ue in N3:
        f[ue]=round(c[ue]*D[ue]/T_cmp/10**9, 2)

    return T_cmp, f