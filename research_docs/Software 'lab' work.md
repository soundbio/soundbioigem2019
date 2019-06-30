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



**Date:** 6/30/19

**Members:** Eric
**Goal:** Figure out why scp is denied and we can't access stuff, misc other tasks

### Summary
The key understanding here is that pi and dataplicity are two separate users. From the dataplicity client, you must run
*su pi*
In order to change to pi@raspberrypi from remote access. The password is i<3science as seen before. From there, you can run python PythonTest.py and the console log will show up on your computer as well!
I'm curious about how to export the data from pi@raspberrypi to an actual computer, however. I think scp from pi to dataplicity should be easy to do, but from dataplicity where do we go? How do we get it onto a computer...

Ok well I figured out a nice file transfer method if you share wifi:
- start your computer, go to dataplicity.com and log in as me (ericpingxia@gmail.com, soundbio or i<3science I think)
- select Raspberry Pi Model etc... (the only option) 
- you should have a prompt labeled dataplicity@raspberrypi:/$
- type *su pi* and then the password i<3science
- you should have a prompt labeled pi@raspberrypi:/ $
- type sudo raspi-config. A nice GUI should pop up
- Use the drop down to get to option 5, select it, then "P2 SSH"
- Enable SSH
- Now that SSH is enabled, click finish, which should return you to pi@raspberrypi:/ $
 - Download WinSCP
 - Enter 192.168.1.164 as the IP, 22 as port number as usual in WinSCP. leave the dropdown as SFTP. No username or password needed. Click connect
 - Enter pi as the username and i<3science as the password in the following popup.
 - Connect. There should be two file managers, one on the Pi side and one on computer side. Simply copy and paste files you need
### Notes
Still doesn't work for remote file transfer
### To-Do
Remote file transfer
Working with temperature sensors
see above

