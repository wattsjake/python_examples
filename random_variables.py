#from scipy import signal
import scipy
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

points = 5000
frequency = 1000

period = frequency**-1
#number of cycles
n = 1

def print_graph(x,y,x_label,y_label,title):
    plt.title(title) 
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # plt.xlim([0,1])
    # plt.ylim([0,15])
    plt.plot(x,y)


def exponential(lambda_, x):
    f = lambda_*np.exp(-lambda_*x)
    return f

def gaussian(mean,sigma,x):
    f = (1/sigma*np.sqrt(2*np.pi))*np.exp(-(x-mean)**2/(2*sigma**2))
    return f

#A is the amplitue
#w is the angular frequency 
def sine(A,w,phase,off_set):
    f = A*np.sin(w*t + phase) + off_set
    return f

t = np.linspace(0,0.001,points)
f1 = sine(1,(2*np.pi)/period,0,0)
f2 = sine(1,(2*np.pi)/5e-4,0,0)
f3 = sine(1,(2*np.pi)/1e-4,0,0)
f = sine(1,(2*np.pi)/period,0,0) + sine(1,(2*np.pi)/5e-4,0,0) + sine(1,(2*np.pi)/3.33e-4,0,0)

print_graph(t,f,'time','amplitude','sine')
plt.show()
print_graph(t,f1,'time','amplitude','sine')
print_graph(t,f2,'time','amplitude','sine')
print_graph(t,f3,'time','amplitude','sine')
plt.show()









