import sympy as sp
import numpy as np
from sympy.abc import x

lowerbound = -np.pi
upperbound = np.pi

def intgrt(f, upper, lower):
    
    F = sp.lambdify(x, sp.integrate(f, x), 'numpy')
    
    return F(upper) - F(lower)

def inprod(f, g):
    return intgrt(f * g , upperbound, lowerbound)

def normf(f):
    return np.sqrt(inprod(f, f))