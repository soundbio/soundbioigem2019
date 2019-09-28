import matplotlib.pyplot as plt
import numpy as np

kp=0.2
ki=0.2
kd=0.0
km=0.0 # just a test


integral=0
derivative=0

setp=18 # target temperature
pv=12 # current temperature

error=setp-pv
olderror=error
correction=0

cool=0.5 # how fast the reactor is cooled passively (this won't be constant for the real one)
maxheat=5 # how fast the heater can possibly increase temperature

dt=0.05 # timestep
final=10 # end of simulation

t=0

y1=[setp-pv]
y2=[pv]

while t<final:
    
    integral = integral+error*dt
    derivative = (error-olderror)/dt
    #print(derivative)
    
    correction=0
    correction += kp*error
    correction += ki*integral
    correction += kd*derivative
    correction += km*abs(derivative)*error # a test
    
    olderror=error
    #print(correction)
    
    
    if correction>maxheat: # heating cap
        correction=maxheat
    
    if correction<0: # no active cooling
        correction=0
    
    # new measured value
    pv = pv + correction - cool
    # DOES NOT take delay into account
    
    # error goes down when correction is positive
    #error up = cooling, error down = heating
    error=setp-pv
    
    y1.append(error)
    y2.append(pv)
    t+=dt
    
plt.figure(1)
plt.plot(np.arange(0, final+1*dt, dt), y1, label='Error')
plt.title("Error over time")
plt.plot(np.arange(0, final+1*dt, dt), np.zeros(int(final/dt)+1), label='Setpoint (Error=0)')
plt.legend()

plt.figure(2)
plt.plot(np.arange(0, final+1*dt, dt), y2, label='Temperature')
plt.title("Temperature over time")
plt.plot(np.arange(0, final+1*dt, dt), np.full(int((final/dt)+1), setp), label='Setpoint')
plt.legend()