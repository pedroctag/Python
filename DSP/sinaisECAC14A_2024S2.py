import numpy as np
import random

def sinalAtv12(numMat):
    random.seed(numMat)
    f1 = random.randrange(10,40)*10
    f2 = random.randrange(51,90)*10
    f3 = random.randrange(101,140)*10
    f4 = random.randrange(161,200)*10
    A1 = random.randrange(10,50,2)/10
    A2 = random.randrange(10,50,4)/10
    A3 = random.randrange(10,50,5)/10
    A4 = random.randrange(10,50,5)/10
    Ts = 1/10e3
    t = np.arange(0,2,Ts)
    s = A1*np.cos(2*np.pi*f1*t) + A2*np.cos(2*np.pi*f2*t) + A3*np.cos(2*np.pi*f3*t) + A4*np.cos(2*np.pi*f4*t)
    ampRuido = 10
    ruido = np.zeros(len(s))
    for k in range(0,len(ruido)):
        ruido[k] = random.gauss(0,ampRuido)
    s = s + ruido

    with open('sinalAtv12.npy','wb') as arq:
        np.save(arq,Ts)
        np.save(arq,s)
