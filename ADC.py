# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

"""Part A : Plotting sine wave of frequency 5Hz"""
f=5
tmin=0
tmax=1 
t1= np.linspace(tmin,tmax,1000)
analog_sin= np.sin(2*np.pi*f*t1)
plt.figure
plt.xlabel("Time(s)")
plt.ylabel("sin(2pi*5t) (volts)")
plt.plot(t1,analog_sin, 'C9')


"""Part E : 12 bit ADC """

sampling_f= 40.0
bits=12
levels= 2**bits
LSB = 2.0/levels
T1 = 1/sampling_f
nmin = np.ceil(tmin / T1)
nmax = np.floor(tmax / T1)
n = np.arange(nmin,nmax);
sampled_sin= np.sin(2*np.pi*f*n*T1)
quantized_sin=LSB * np.round((sampled_sin/LSB))
t3= np.linspace(0,1,40)
plt.plot(n*T1, quantized_sin,'bo')
plt.savefig('sinWave.png')

""" Part C: Quantization Error Signal """
error_signal= sampled_sin-quantized_sin
avg= sum(error_signal) / 40.0
value= error_signal-avg
value = value**2
var= sum(value)/39.0
rms= np.sqrt(var)
print("Average is: ")
print(avg)
print(" Standard Deviation is:")
print(rms)


