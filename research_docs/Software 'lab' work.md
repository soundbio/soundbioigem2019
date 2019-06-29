# Software lab work


**Date:** 6/22/2019

**Members:** Hari, Claris (Advisor: Zach)

**Goal:** To set up and test some sensors and connect them with raspberry pi

### Summary: 

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



### Notes: 

- Raspberry pi password --> **i<3science**, username --> **pi**
- ip --> **192.168.1.164**

### To Do:

- Modify the code or the circuits (maybe both) to get the program to check for inputs successfully
- Create data-collecting infrastructure (how?)
- Integrate withh puTTY
  
  
  

**Date:** 6/24/2019

**Members:** Hari, Eric

**Goal:** correctly get sensor input, write it to a csv file, accessible remotely.

### Summary

1. Correctly initialized the r pi input (using GPIO # based referencing to pins)  
2. Testing sensors, creating a csv to write data to.
3. Testing ssh commands, including "python", "nohup", "kill [PID]", "killall" (oops).
4. Set up a pid text document where the program prints its pid every time it is run, allowing remote terminations

### Notes & commands to use:

- all these files can be found on the Desktop
- "cd [foldername]" to navigate to a subfolder, use ".." to go out of the current folder
- "ls" to list all items in current directory
- "python [filename.py]" to execute a program. include "-u" after python to see outputs.
- add "nohup" (no hangup) before python command (without "-u") to keep program running after you disconnect.
- DON'T run two nohup python files concurrently, since only one pid is stored in "pid.txt".
- kill [pid from pid.txt] to stop a program
- "pico [filename.txt]" to edit text (can be done with .csv and .py)
- "killall python" to stop all python scripts

### To Do:

- find command to copy file from raspberry pi to your computer
(try: scp pi@raspberrypi:/Desktop/test.txt /path/to/destination  
or: scp file.txt [destination IP]:/[destination path])
- use [dataplicity](https://www.dataplicity.com/) to connect with the pi over the internet
- make a program with a simple feedback loop to control temperature (using temperature sensor), but replace heater output with an LED (should be in the bag)



**Date:** 6/27/19

**Members:** Eric, Claris

**Goal:** To set up Dataplicity. try to copy file from raspberry pi to computer, temperature/humidity sensor

### Summary

1. We succesfully set up dataplicity

   * email: ericpingxia@gmail.com 
   * password: i<3science

2. We tested many commands on dataplicity

3. We used VNC viewer as a 'backup' when we can't use the monitor

   * Desktop number = 1

   * We were able to edit the files easily 
   * it looks exactly like how it looks on the monitor
   * We added comments to the sensor code and simplified it a bit and it is now on our Github

4. We tried using the scp command but it kept telling us *permission denied!*

### Notes

* We burned the temperature and humididty sensor because we forgot the resistor
* **REMEMBER TO PUT ANY NEEDED RESISTORS TO PREVENT BURNED SENSORS :))**
*   

### To-Do

* Try out fcp command instead to copy file from raspberry pi to your computer
* make a program with a simple feedback loop to control temperature (using temperature sensor), but replace heater output with an LED (should be in the bag) - why is temperature sensor giving only 0 and 1?
* 



