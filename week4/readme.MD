#Week 4  [PyNet Python + Ansible] - Class4 / Paramiko, Pexpect, Netmiko



D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetACert\week4>python week4.py -h
usage: week4.py [-h] [-a] [-1] [-2] [-3] [-4] [-5] [-6] [-7] [-8]

PyNet Python + Ansible Course - Week 4 Excercises

optional arguments:
  -h, --help  show this help message and exit
  -a, --all   Execute all exercises in week 4 assignment
  -1, --ex1   Execute Exercise 1
  -2, --ex2   Execute Exercise 2
  -3, --ex3   Execute Exercise 3
  -4, --ex4   Execute Exercise 4
  -5, --ex5   Execute Exercise 5
  -6, --ex6   Execute Exercise 6
  -7, --ex7   Execute Exercise 7
  -8, --ex8   Execute Exercise 8

Usage: 'python week4.py -a' to execute all exercises, 'python week4.py -1' to
execute exercise 1

```

pplied_python)[cdeluna@ip-172-30-0-7 week4]$ python week4.py -a > Week4-FullRunReport.txt
(applied_python)[cdeluna@ip-172-30-0-7 week4]$ ls
config_file.txt  test.py  Week4-FullRunReport.txt  week4.py
(applied_python)[cdeluna@ip-172-30-0-7 week4]$ cat Week4-FullRunReport.txt 
############## Device ###############
pynet-rtr2
184.105.247.71

Executing exercise 1 - Use Paramiko to retrieve the entire 'show version' output from device pynet-rtr2.
Sending command: show version

In main after calling para_conn function: 
pynet-rtr2#term len 0
pynet-rtr2#show version
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Thu 26-Jun-14 14:15 by prod_rel_team

ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

pynet-rtr2 uptime is 20 weeks, 1 hour, 18 minutes
System returned to ROM by reload at 19:10:00 UTC Thu Jul 7 2016
System restarted at 12:35:46 PDT Thu Jul 7 2016
System image file is "flash:c880data-universalk9-mz.154-2.T1.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX18298312

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
125440K bytes of ATA CompactFlash (Read/Write)


License Info:

License UDI:

-------------------------------------------------
Device#	  PID			SN
-------------------------------------------------
*0  	  CISCO881-K9           FTX18298312     



License Information for 'c880-data'
    License Level: advsecurity   Type: Permanent
        Next reboot license Level: advsecurity
	
	
	Configuration register is 0x2102
	
	pynet-rtr2#
	
	Executing exercise 2 - Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2.
	Sending command: logging buffered 12000 debugging
	
	In main after calling para_conn function: end
	pynet-rtr2#show run | i logging buff
	logging buffered 12000
	pynet-rtr2#
	
	Executing exercise 3 - Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
	Sending command: show ip int br
	
	show ip int br
	Interface                  IP-Address      OK? Method Status                Protocol
	FastEthernet0              unassigned      YES unset  down                  down    
	FastEthernet1              unassigned      YES unset  down                  down    
	FastEthernet2              unassigned      YES unset  down                  down    
	FastEthernet3              unassigned      YES unset  down                  down    
	FastEthernet4              10.220.88.21    YES NVRAM  up                    up      
	Vlan1                      unassigned      YES unset  down                  down    
	
	pynet-rtr2#
	In main after calling pexp_conn function: pynet-rtr2#
	
	Executing exercise 4 - Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2 and verify.
	Sending command: logging buffered 14000 debugging
	
	logging buffered 14000 debugging
	pynet-rtr2(config)
	#
	show run | i logging
	logging count
	logging buffered 14000
	no logging console
	
	pynet-rtr2#
	In main after calling pexp_conn function: pynet-rtr2#
	
	Executing exercise 5 - Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state.
	In main after calling netm_conn function: <netmiko.cisco.cisco_ios.CiscoIosSSH object at 0x7f9bfbce27d0>
	Sending command: config t
	pynet-rtr2#
	Device is in global configuration mode!
	
	Executing exercise 6 - Use Netmiko to execute show arp on ['pynet-rtr1', 'pynet-rtr2', 'juniper-srx'].
	Sending command: show arp
	pynet-rtr1#
	Protocol  Address          Age (min)  Hardware Addr   Type   Interface
	Internet  10.220.88.1            10   0062.ec29.70fe  ARPA   FastEthernet4
	Internet  10.220.88.20            -   c89c.1dea.0eb6  ARPA   FastEthernet4
	Internet  10.220.88.21          137   1c6a.7aaf.576c  ARPA   FastEthernet4
	Internet  10.220.88.28           18   5254.aba8.9aea  ARPA   FastEthernet4
	Internet  10.220.88.29           51   5254.abbe.5b7b  ARPA   FastEthernet4
	Internet  10.220.88.30           27   5254.ab71.e119  ARPA   FastEthernet4
	Internet  10.220.88.32           16   5254.abc7.26aa  ARPA   FastEthernet4
	Internet  10.220.88.37          166   0001.00ff.0001  ARPA   FastEthernet4
	Internet  10.220.88.38           24   0002.00ff.0001  ARPA   FastEthernet4
	Internet  10.220.88.40           21   001c.c4bf.826a  ARPA   FastEthernet4
	Internet  10.220.88.41           98   001b.7873.5634  ARPA   FastEthernet4
	Sending command: show arp
	pynet-rtr2#
	Protocol  Address          Age (min)  Hardware Addr   Type   Interface
	Internet  10.220.88.1            10   0062.ec29.70fe  ARPA   FastEthernet4
	Internet  10.220.88.20          137   c89c.1dea.0eb6  ARPA   FastEthernet4
	Internet  10.220.88.21            -   1c6a.7aaf.576c  ARPA   FastEthernet4
	Internet  10.220.88.28           42   5254.aba8.9aea  ARPA   FastEthernet4
	Internet  10.220.88.29           22   5254.abbe.5b7b  ARPA   FastEthernet4
	Internet  10.220.88.30           56   5254.ab71.e119  ARPA   FastEthernet4
	Internet  10.220.88.40           52   001c.c4bf.826a  ARPA   FastEthernet4
	Internet  10.220.88.41          102   001b.7873.5634  ARPA   FastEthernet4
	Sending command: show arp
	pyclass@pynet-jnpr-srx1>
	
	MAC Address       Address         Name                      Interface           Flags
	00:62:ec:29:70:fe 10.220.88.1     10.220.88.1               vlan.0              none
	00:1c:c4:bf:82:6a 10.220.88.40    10.220.88.40              vlan.0              none
	Total entries: 2
	
	
	Executing exercise 7 - Use Netmiko to change the logging buffer size on pynet-rtr2.
	
	Sending command: show run | inc logging buff
	pynet-rtr2#
	logging buffered 14000
	
	Sending command: config t
	pynet-rtr2#
	
	Sending command: logging buffered 13000 debugging
	pynet-rtr2(config)#
	
	Sending command: do show run | inc logging buff
	pynet-rtr2(config)#
	logging buffered 13000
	
	Executing exercise 8 - Use Netmiko to change the configuration on ['pynet-rtr1', 'pynet-rtr2'] using a file.
	
	Sending command: show run | inc logging buff
	pynet-rtr1#
	logging buffered 12000
	
	Sending command: config t
	pynet-rtr1#
	
	Sending commands from file: config_file.txt
	pynet-rtr1(config)#
	
	Sending command: show run | inc logging
	pynet-rtr1#
	logging buffered 12000
	no logging console
	
	Sending command: show run | inc logging buff
	pynet-rtr2#
	logging buffered 13000
	
	Sending command: config t
	pynet-rtr2#
	
	Sending commands from file: config_file.txt
	pynet-rtr2(config)#
	
	Sending command: show run | inc logging
	pynet-rtr2#
	logging count
	logging buffered 12000
	no logging console
	



```
