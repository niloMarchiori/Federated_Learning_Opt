import inputs as inp
import constants as ctt
import numpy as np
from scipy.special import lambertw

def get_tmax(s,B,h,N0,pmin):
    return s/(B * np.log(1 + (pmin * h) / N0))

def get_tmin(s,B,h,pmax,N0):
    return s/(B * np.log(1 + (pmax * h) / N0))

def g(kappa,s,B,N0,h):
    num=s/B
    x= ((kappa*h)/N0-1)/np.e
    W= lambertw(x).real
    return num/(1+ W)

def g_inverse(t,s,B,N0,h):
    y= (s/(B*t))-1
    # k=(N0/h)*(1+(y-1)*np.e**y)
    k = (N0/h)*(1 + y*np.exp(y+1))
    return k

def solve_SUB2(N,kappa,s,B,N0,h,pmin,pmax):
    t=np.zeros(N)
    tmax = get_tmax(s,B,h,N0,pmin)
    tmin = get_tmin(s,B,h,pmax,N0)

    g_value = g(kappa,s,B,N0,h)

    price_tmax=g_inverse(tmax,s,B,N0,h)
    price_tmin=g_inverse(tmin,s,B,N0,h)
    
    mask_a= kappa <= price_tmax
    mask_b= (price_tmax < kappa) & (kappa < price_tmin)
    mask_c= kappa >= price_tmin

    t[mask_a]=tmax[mask_a]
    t[mask_b]=g_value[mask_b]
    t[mask_c]=tmin[mask_c]

    p=N0/h * (np.exp(s/(B*t)) - 1)

    Tcom=np.sum(t)
    return Tcom,t,p

if __name__ == "__main__":
    N=ctt.N
    kappa=ctt.kappa
    s=inp.s
    B=inp.B
    N0=ctt.N0
    h=inp.h
    pmin=inp.pmin
    pmax=inp.pmax
    Tcom,t=solve_SUB2(N,kappa,s,B,N0,h,pmin,pmax)
    print("Tcom:",Tcom)
    print("t:",t)