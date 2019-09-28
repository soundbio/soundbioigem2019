import matplotlib.pyplot as plt
import os
import csv

os.chdir("/")

data=[]
with open("home/pi/Desktop/pid.txt", 'r') as source:
    temp=csv.reader(source, delimiter=',')
    for row in temp:
        data.append(row)
y=[data[i][2] for i in range(len(data))]
x=[data[i][1]-data[0][1] for i in range(len(data))]

plt.figure(1)
plt.plot(x, y)
plt.ylabel('Temperature (C)');
plt.xlabel('Time since start (minutes)');
plt.title('Temperature over time');
plt.grid(True);

y=[data[i][4] for i in range(len(data))]

plt.figure(2)
plt.plot(x, y)
plt.ylabel('Duty Cycle (%)');
plt.xlabel('Time since start (minutes)');
plt.title('Duty Cycle over time');
plt.grid(True);

plt.show()