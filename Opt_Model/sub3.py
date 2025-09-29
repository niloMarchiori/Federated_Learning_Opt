import numpy as np
from scipy.optimize import fsolve
import inputs as inp
import constants as ctt

def get_Ecmp(f, alpha, c, D):
    """
    Calcula a energia de computação (E_cmp) para cada UE.
    Referência: Equação (8) no PDF.
    """
    # Garante que f está em Hz. A saída de solve_SUB1 está em GHz.
    f_hz = f * 1e9
    return (alpha / 2) * c * D * f_hz**2

def get_Ecom(t, s, B, N0, h):
    """
    Calcula a energia de comunicação (E_com) para cada UE.
    Referência: Equações (11) e (12) no PDF.
    """
    # Evita divisão por zero se o tempo 't' for muito pequeno ou zero
    # Adiciona uma pequena constante epsilon ao denominador
    epsilon = 1e-12
    p = (N0 / h) * (np.exp(s / (t * B + epsilon)) - 1)
    return t * p

def get_eta(Ecmp_total, Ecom_total, T_cmp, Tcom, kappa):
    """
    Calcula o valor de eta (η).
    Referência: Equação (39) no PDF.
    """
    numerador = Ecmp_total + kappa * T_cmp
    denominador = Ecmp_total + Ecom_total + kappa * (T_cmp + Tcom)
    # Evita divisão por zero no caso de o denominador ser nulo
    if denominador == 0:
        return 0
    return numerador / denominador

def equation_to_solve_theta(theta, eta):
    """
    Equação que precisa ser resolvida para encontrar theta (θ).
    Rearranjo da Equação (38) no PDF: 1/η = 1/θ + log(θ)
    """
    # Evita log(0) adicionando uma pequena constante se theta for muito pequeno
    epsilon = 1e-12
    return 1/eta - (1/theta + np.log(theta + epsilon))

def solve_SUB3(f, t, T_cmp, Tcom, kappa):
    """
    Resolve o Subproblema 3 para encontrar o valor ótimo de theta.
    """
    # Calcula a energia total de computação e comunicação
    Ecmp_array = get_Ecmp(f, ctt.alpha, inp.c, inp.D)
    Ecom_array = get_Ecom(t, inp.s, inp.B, inp.N0, inp.h)
    
    Ecmp_total = np.sum(Ecmp_array)
    Ecom_total = np.sum(Ecom_array)
    
    # Calcula eta
    eta = get_eta(Ecmp_total, Ecom_total, T_cmp, Tcom, kappa)
    
    # Chute inicial para o solver numérico.
    # O valor de theta deve estar entre 0 e eta.
    initial_guess = eta * 0.5
    
    # Resolve a equação para theta
    theta_solution, = fsolve(equation_to_solve_theta, initial_guess, args=(eta))
    
    return theta_solution, eta