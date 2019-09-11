from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
"""Передаточная функция"""
def func(num,den,num2, den2):
    W=tf(num, den)
    W2=tf(num2, den2)
 
    y,x=step(W)
    ya,xa=step(W2)
    plt.figure()
    plt.subplot(2,2,1)
    plt.plot(x,y,"r",xa,ya,"g")
    #lines=[W,W2]
    #lines[0],lines[1]=plt.plot(y,"r",ya,"g")
    #plt.legend(lines,['W' ,'W2']) 
    #plt.plot(x,y,"r")
    plt.title('Переходная функция') 
    plt.ylabel('Amplitude')
    plt.xlabel('Time')
    plt.grid(True)
    print (W)
    
    y1,x1=impulse(W)
    y1a,x1a=impulse(W2)
    plt.subplot(2,2,2)
    plt.plot(x,y,"r",xa,ya,"g")
    #lines=[W,W2]
    #lines[0],lines[1]=plt.plot(y1,"r",y1a,"g")
    #plt.legend(lines,['W' ,'W2']) 
    plt.title('Импульсная функция') 
    plt.ylabel('Amplitude')
    plt.xlabel('Time')
    plt.grid(True)

    plt.figure()
    mag, phase, omega=bode(W, dB=False)
    mag, phase, omega=bode(W2, dB=False)
    plt.plot() 
    plt.title('АЧХ ФЧХ')
    
    plt.show()
    return W
    return W2
"""k=3
w=tf([k],[0.0000001,1])
y,x=step(w)
plt.plot(x,y,"r")
plt.show()"""
f=func([3],[0.0000001,1],[6],[0.0000001,1])

#a=func([5.],[5.,1],[10.],[10.,1])
#b=func([1.],[1.,0],[2.],[1.,0])
#c=func([2.,0],[10e-10,1],[4.,0],[10e-10,1])
#d=func([2.,0.],[1.,1],[4.,0.],[2.,1])
"""print('безынерционное звено ', f)
print('апериодическое звено ', a)
print('интегрирующее звено ', b)
print('идеальное дифференцирующее звено ', c)
print('реальное дифференцирующее звено ', d)"""


