# Software lab work


**Date:** 6/22/2019

**Members:** Hari, Claris (Advisor: Zach)

**Goal:** To set up and test some sensors and connect them with raspberry pi

####Summary: 

1. We installed raspberry pi noobs onto Hari’s computer and loaded it into onto the SD card
2. We set up the raspberry pi and connected all the things to it (computer, mouse, sd card…)
3. We spent some time debugging the raspberry pi because the monitor was not displaying the raspberry pi - The problem was the OS was still inside a single folder (which we removed it from, and it worked)
4. We set up the actual rasberry pi on the computer & installed raspbian.
5. We set up puTTY on the pi. To connect:
       - [Download puTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
       - The ip address of the pi is **192.168.1.164**
       - Connect to the pi, making sure it is on (only enter the IP, and click "Yes" on the warning)
       - Use this to access the pi remotely
6. We created and modified a text document (in the documents folder) using putty (it works!)
7. We set up a simple breadboard circuit with a joystick sensor that inputs both x and y movements.
8. Attempted to get inputs from the joystick in a python program (using the Thonny IDE, saved to desktop)  



####Notes: 

- Raspberry pi password --> **i<3science**, username --> **pi**
- ip --> **192.168.1.164**

#### To Do:

- Modify the code or the circuits (maybe both) to get the program to check for inputs successfully
- Create data-collecting infrastructure (how?)
- Integrate withh puTTY