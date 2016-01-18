#   Network monitoring and analysis of WSN using Raspberry Pi 

##Design of network architecture
In our setup we are using a Mac OS X. So all the steps are relative to it.For setting up the network in this project, we would require:
-Raspberry Pi 2 Model B+
-Micro SD card(8GB) 
-Wifi Dongle
-Sensor (DHT11)
-Ethernet cable

##Raspberry Pi configuration:
First to configure the Raspberry Pi 2, we need to follow these steps:

###Step1:
First, take the microSD card insert into your computer and download the latest OS for the raspberry Pi into your computer from  www.raspberrypi.org (Raspbian-Wheezy-2015 image)

###Step 2:
	$ diskutil list
In the terminal enter the command.This command defines the memory partitions in the CPU.

###Step 3:
	$ diskutil unmountDisk /dev/disk<disk no from diskutil list>
	For example: $ diskutil unmount /dev/disk4 
Carefully, identify the disk(not the partition) of the corresponding SD card (e.g. disk4 not disk4s1). Unmount the SDcard by using by using this command
	
###Step 4:
	$ sudo dd bs=1m if=image.img of=/dev/rdisk<disk no from diskutil>
	NOTE: If it results in an error,  try with “bs=1M”
Navigate into the folder where the Raspbian-wheezy-2015 image is downloaded and then copy the data to your SD card, using the command:
	
###Step 5:
To check the initial setup, we need to change the network settings and change the ethernet preferences to “Using DHCP” and configure the location to “automatic”.

###Step 6:
	$ ping raspberrypi.local
Connect the raspberry pi to a power  source and through a wired connection to your computer and check if it works.This command gives the ip address of the raspberry pi.

###Step 7:
	$ ssh -X pi@raspberrypi.local (raspberry pi IP address)
We can login using a secure shell using the above command.This would prompt the user with a user password(“raspberry”).

###NOTE:
	$ ssh-keyscan “ip address of raspberry pi” >> ~/.ssh/known_hosts
In case of warnings mentioning possible DNS SPOOFING DETECTED type errors try the above command.
	
##SETTING UP WIFI DONGLE:
	$ startlxde & 
To setup WIFI on the raspberry pi, we need to first connect the raspberry pi via ethernet and then insert the WIFI dongle in one of the USB slots.Enter the above command in the terminal, which forms a seperate virtual screen. Once that opens up, you can open the Wpa_gui on the desktop, and click on “Scan”  to scan the wireless networks available. You can choose the one which you can enter and double click on it. 

Here we enter the user details like :
Identity: (Email id)
password: (password)
Inner Auth: PAP


##INSTALLING ADAFRUIT DHT11 LIBRARY
 	git clone https://github.com/adafruit/Adafruit_python_DHT.git
	$ sudo apt-get update
	$ sudo apt-get install build-essential python-dev python-openssl
	$ cd Adafruit_DHT
	$ sudo python setup.py install (This installs the library)
	
To install adafruit DHT11 library, we have to follow these steps as shown above. Once git clone command is done, it grabs the files from github repository. Open the adafruit folder and follow the next steps as root user.

##INSTALLATION OF PLOTLY LIBRARY:
	$ sudo pip install plotly
At the server end, we have imported the libraries of plotly. At first, we have created an account in plotly, this creates API key for my account. As we are using streaming real-time data continuously, plotly generates a separate API stream tokens.In order for the server to support plotly, we need to install few libraries, they can be done from the command line using the above command.
Once it is installed you can check it, by opening python and enter in the interpreter,
   >>> import plotly
   >>>
   
which should return you to the line, successfully. 
Once that is done, we can import the same library in the code and use it by 
py.sign_in(“username”,”api_key”)

##INSTRUCTIONS TO RUN THE CODE
In this project, we tried to monitor an application where a wireless sensor network is setup up. In this we have a single server and two client connected Wirelessly through 802.11 b/g.
The two sensor nodes are chosen in such a way that , they are capable enough to have its own OS to handle the sensor information.   From the command line terminal, the server can be switched on to make it available to listen to the sensor node information as follows: 

#####$ sudo python server.py -s 
(This is run as a root, and an argument ”-s” informs that it is a server)

and on either of the clients the sensor nodes, one can run the client code as below:

#####$ sudo python client1.py -c (server address) 
#####$ sudo python client2.py -c (server address)

Here is a video demo of our project, and how the system actually reacts in this link below:
    https://www.youtube.com/watch?v=z0Jn7DMbfEM

#IMPROVEMENTS AND EXTENSIONS
In this program, we were able to implement with just few network parameters. But however, this can be extended up to more number of parameters as well. Increase in the number of monitoring parameters gives us an idea to attack and solve them precisely. 
We have just implemented with two sensor nodes in a network, but which can be implemented with more number of sensor nodes to attain the data accurately. 
However, looking at the extensions sections, we can also improve it by sending the user, a warning email whenever the values drop below a threshold level. 


##TEST CASES
###CASE 1:
In our case, we have a server serving multiple clients. These are continuously transmitting data and this when it reaches the server will be opening a GUI or visualization tool to represent them in a graph. This works fine when a single client is connected. But when two clients are connected, it mixes up the data coming from both the clients and gives the output and this is not desirable. 

###CASE 2:
Connecting the raspberry pi’s to the network requires its ip address. However, if there is a shutdown in the power, depending on the IP addresses DHCP licenses of the sensor nodes might change. This may or may not lead to reconfiguration of the sensor node. As this is unreliable, we might have some issues regarding the remote login. We have faced one such problem and could solve it using the ssh-keyscan method.

##REFERENCES:
[1]https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/software-install-updated
[2]https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis
[3]http://raspberryalphaomega.org.uk/2013/07/10/a-solution-to-multiple-raspberry-pi-ssh-key-woes/
[4]https://plot.ly/python/getting-started/

