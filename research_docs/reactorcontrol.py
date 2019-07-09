import matplotlib.pyplot as plt
import numpy as np

kp=0.1
ki=0.1
kd=0.0

integral=0
derivative=0

error=0
correction=0

setp=18
pv=15

dt=0.05
final=10
t=0
y=[setp-pv]
counter=0;

while t<final:
    error = setp-pv
    integral = integral+error*dt
    derivative = (error-y[counter-1])/dt
    print(derivative)
    correction=0
    correction += kp*error
    correction += ki*integral
    correction += kd*derivative
    pv=setp-y[counter]+correction # error goes down when correction is positive
    y.append(setp-pv)
    counter+=1
    t+=dt
    
plt.figure(1)
plt.plot(np.arange(0, final+dt, dt), y)