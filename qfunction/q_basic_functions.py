__author__ = {'name':'Reynan_Bezerra',
              'date':'17/12/2020',
              'hour':'22:44'}
# criação da biblioteca inciada às 22:44 do dia 17 de Dez de 2020
#author Reinan Bezerra

import numpy as np
from mpmath import *

mp.dps = 25; mp.pretty = True

#from sympy import *
#class this:
#	q = .9

#q = this.q

#q-exponencial

def q_exp(t,q):
   #q_ = symbols('q')
   #q_ = q
   equation =lambda q_: (1+(1-q_)*t)**(1/(1-q_))
   #print(q)
   return float(limit(equation,q).real)
'''
def q_exp(t):
    if q==1:
      return np.exp(t)
    A = (1-q)
    #condição de q>1 e espaço limite de t 
    if q > 1.9 and t >= 1/(q-1):
        return np.nan
    return (1+(1-q)*t)**(1/(1-q)) if (1+(1-q)*t) >=0 else 0
'''
#q-rho
def q_rho(t): return q_exp((1-q)*(t**2),q)

#q-phi
def q_phi(t): return (1/(1-q))*np.arctan((1-q)*t)

#q-cosseno
def q_cos(t): return (q_rho(t,q)*cos(q_phi(t,q)))

#q-seno
def q_sen(t,q=.9): return (q_exp(t*1j,q)-q_exp(-t*1j,q))/2j
