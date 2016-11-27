PyNet + Ansible Week 7
==============

Exercise 1
--------------

Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.  Accomplish this using Arista's pyeapi.

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>python arista_ex1.py veos-cs02

	****** Device is: veos-cs02******

	==== Management1 ===
	=========================
	inOctets: 149205
	outOctets: 443466
	=========================
	==== Ethernet2 ===
	=========================
	inOctets: 3943164
	outOctets: 367628
	=========================
	==== Ethernet3 ===
	=========================
	inOctets: 0
	outOctets: 3954221
	=========================
	==== Ethernet1 ===
	=========================
	inOctets: 168553130
	outOctets: 1160036
	=========================
	==== Ethernet6 ===
	=========================
	inOctets: 0
	outOctets: 3954098
	=========================
	==== Ethernet4 ===
	=========================
	inOctets: 0
	outOctets: 3954221
	=========================
	==== Ethernet5 ===
	=========================
	inOctets: 0
	outOctets: 3954221
	=========================

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>

Exercise 2
--------------

Using Arista's pyeapi, create a script that allows you to add a VLAN (both the VLAN ID and the VLAN name).  

Your script should first check that the VLAN ID is available and only add the VLAN if it doesn't already exist.  Use VLAN IDs between 100 and 999.  You should be able to call the script from the command line as follows:

   python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.

   python eapi_vlan.py --remove 100          # remove VLAN100


*This output is from a local environment using a multi host Vagrant veos configuration*
   
**eapi.conf file**

	claud@DESKTOP-S41OCM2 MINGW64 ~
	$ cat .eapi.conf
	[connection:veos-cs01]
	host: 10.1.10.221
	username: vagrant
	password: vagrant
	transport: https

	[connection:veos-cs02]
	host: 10.1.10.222
	username: vagrant
	password: vagrant
	transport: https


claud@DESKTOP-S41OCM2 MINGW64 ~
$

   
**Starting Switch Config**

	veos-cs01#sh vlan
	VLAN  Name                             Status    Ports
	----- -------------------------------- --------- -------------------------------
	1     default                          active    Et2, Et3, Et4, Et5, Et6

	veos-cs01#


**Help Option**

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>python arista_ex2.py -h
	usage: arista_ex2.py [-h] [--name NAME_NUM] [--remove REM_VLAN_NUM]
						 [--verify CHECK_VLAN_NUM] [--device] [--version]

	optional arguments:
	  -h, --help            show this help message and exit
	  --name NAME_NUM       Provide the name and the number of the Vlan to add if
							it does not exist usint the format VLANNAME_VLANNUMBER
	  --remove REM_VLAN_NUM
							Store the number of the Vlan to remove if it exists
	  --verify CHECK_VLAN_NUM
							Store the number of the Vlan to check
	  --device              Set to True to display the device that is being worked
							on
	  --version             show program's version number and exit

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>


**Version Option**

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>python arista_ex2.py --version
	arista_ex2.py 1.0

**Device Option (Extra)**

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>python arista_ex2.py --device
	The currently configured device is veos-cs01.

**Check Vlan Option (Extra)**

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>python arista_ex2.py --verify 101
	Vlan 101 is NOT configured on device veos-cs01

**Remove Vlan Option when Vlan does not exists**

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>python arista_ex2.py --remove 101
	Vlan 101 is NOT configured on device veos-cs01 and so no action is required.

**Add Vlan Option when Vlan does not exist**

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>python arista_ex2.py --name SERVER_101
	Vlan 101 has been added to device veos-cs01and verified.

**Switch Config after adding vlan**

	veos-cs01#sh vlan
	VLAN  Name                             Status    Ports
	----- -------------------------------- --------- -------------------------------
	1     default                          active    Et2, Et3, Et4, Et5, Et6
	101   SERVER                           active

**Add Vlan Option when Vlan does exist**

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>python arista_ex2.py --name SERVER_101
	Vlan 101 is ALREADY configured on device veos-cs01 and so no action is required.

**Remove Vlan Option when Vlan exists**

	D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA\week7>python arista_ex2.py --remove 101
	Vlan 101 has been removed from device veos-cs01and verified.

**Switch Config after removing vlan**

	veos-cs01#sh vlan
	VLAN  Name                             Status    Ports
	----- -------------------------------- --------- -------------------------------
	1     default                          active    Et2, Et3, Et4, Et5, Et6


Exercise 2 on PyNet environment
--------------


**eapi.conf file**

	(applied_python)[cdeluna@ip-172-30-0-4 ~]$ cat .eapi.conf 
	[connection:pynet-sw4]
	username: eapi
	password: 17mendel
	host: 184.105.247.75
	transport: https

**Results in PyNet Environment**

	(applied_python)[cdeluna@ip-172-30-0-4 ~]$ pwd
	/home/cdeluna

	(applied_python)[cdeluna@ip-172-30-0-4 week7]$ python arista_ex2.py -h
	usage: arista_ex2.py [-h] [--name NAME_NUM] [--remove REM_VLAN_NUM]
						 [--verify CHECK_VLAN_NUM] [--device] [--version]

	optional arguments:
	  -h, --help            show this help message and exit
	  --name NAME_NUM       Provide the name and the number of the Vlan to add if
							it does not exist usint the format VLANNAME_VLANNUMBER
	  --remove REM_VLAN_NUM
							Store the number of the Vlan to remove if it exists
	  --verify CHECK_VLAN_NUM
							Store the number of the Vlan to check
	  --device              Set to True to display the device that is being worked
							on
	  --version             show program's version number and exit
	(applied_python)[cdeluna@ip-172-30-0-4 week7]$ python arista_ex2.py --device
	The currently configured device is pynet-sw4.
	(applied_python)[cdeluna@ip-172-30-0-4 week7]$ python arista_ex2.py --verify 101
	Vlan 101 is configured on device pynet-sw4
	(applied_python)[cdeluna@ip-172-30-0-4 week7]$ python arista_ex2.py --name SERVER_101
	Vlan 101 is ALREADY configured on device pynet-sw4 and so no action is required.
	(applied_python)[cdeluna@ip-172-30-0-4 week7]$ python arista_ex2.py --remove 101
	Vlan 101 has been removed from device pynet-sw4and verified.
	(applied_python)[cdeluna@ip-172-30-0-4 week7]$ python arista_ex2.py --verify 101
	Vlan 101 is NOT configured on device pynet-sw4
	(applied_python)[cdeluna@ip-172-30-0-4 week7]$ python arista_ex2.py --name SERVER_101
	Vlan 101 has been added to device pynet-sw4and verified.
	(applied_python)[cdeluna@ip-172-30-0-4 week7]$ python arista_ex2.py --name SERVER_101
	Vlan 101 is ALREADY configured on device pynet-sw4 and so no action is required.
	(applied_python)[cdeluna@ip-172-30-0-4 week7]$ 


   
Exercise 3
-------------- 

Challenge exercise (optional) -- Using Arista's eAPI, write an Ansible module that adds a VLAN (both a VLAN ID and a VLAN name).  Do this in an idempotent manner i.e. only add the VLAN if it doesn't exist; only change the VLAN name if it is not correct. 


