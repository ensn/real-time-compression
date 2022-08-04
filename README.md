# [Downloads here](https://github.com/ensn/real-time-compression/releases/tag/release)

## The Real Time Compression Glitch
In the Minecraft versions b1.5_01 and earlier, there is a glitch that speeds up the game and therefore compressing more in-game time into a chunk of real time<br /><br />
The glitch can be performed by changing the system time of the computer ahead (Time Zone changes and playing during the beginning of daylight saving time don't work)<br /><br />
The factor by which the game gets sped up is maily dependent on hardware differences. On my system it reaches 31.5 times the normal speed without lag<br /><br />
The amount of time after the speed boost wears off depends on the amount of time that was changed. For example, after time changes of 1 minute, 1 day and 1 year, the boost last for approximately 15 seconds, 30 seconds and 1 minute respectively. After this time the speed increase slowly wears of, taking about the same time to reach normal speed<br />

## Setup
- [download and install python](https://www.python.org/downloads/) **!Make sure that you add Python to PATH!** <br />
- Run Command Prompt as administrator. If you are not administrator it doesn't work
- copy the path of the folder that contains the script that you want to run
- Type in the command line: cd [paste the path]
- Now run one of the scripts by typing: 'python automatic.py' or 'python manual.py'
- If there are no error messages and you aren't able to type anymore, the script is running
- To stop the script, close the command line window

## Automatic version
The automatic version of the script starts running 10 after start and changes the time by 1 day every 15 seconds.<br />
This way it is guaranteed that the game is always running at its maximum speed, even if a time change gets 'eaten' by lag

## Manual version
The manual versions of the script start running immediatly after start.<br />
It changes the time by 1 day in v1.0.0 and 1 minute in 1.1.0 every time a key is pressed. <br />
This key is B on default, but can be changed to any letter or number key by editing line 1 of manual.py in Notepad while keeping the syntax the same<br />
This version requires you to install the 'keyboard' library from pip ([tutorial](https://www.youtube.com/watch?v=jnpC_Ib_lbc))
