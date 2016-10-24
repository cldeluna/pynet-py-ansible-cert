## PyNet Week 3 Exercises

### Class3 / SNMPv3, Graphing, and Email

### Exercise 1
Using SNMPv3 create a script that detects router configuration changes.

w3_01_FindConfChg.py


```
Claudia@Mac-mini:~/Dropbox (Indigo Wire Networks)/scripts/python/2016/PyNetACert/week3$ python w3_01_FindConfChg.py 'device_info.json'

Usage: w3_01_FindConfChg.py <JSON file with device information> <Action "baseline" | "check">
Example: python w3_01_FindConfChg.py "device_info.json" "check"

```
This script takes two arguments, a JSON file with all the information required to establish and SNMP session to one (or more in the future) device and an action.  

Action: 

"snapshot" results in a "snapshot" of all the OIDs in the JSON file "oids.json" which is saved to a file.
"check" results in the latest snapshot file in the directory being selected and loaded in to a "snapshot" dictionary, all variables are refreshed and loaded into a current dictionary and comparisons are made.  A series of if statements are processed to build out a message as to what, if any, changes have ocurred since the snapshot along with the time of the snapshot and the approximate time of the change based on the sysUptime delta.  

Both actions use the get_snmp3_info function.  Snapshot saves it to a file.  Check saves it to a variable for comparison with the loaded data from the snapshot Json file.

During the snapshot action one of the key:value pairs saved is the time using the time.time() function.  That allows us to correlate time wiht sysUpTime.
During the check function the current sysUpTime is added to the snapshot time and converted using time.ctime(snapshot.time + curr.time) to derive the approximate time of the change.  I'm sure there is a better way to do this as tihs has many flaws including needed the sysUpTime to be uninterrupted.  This fails if the router is rebooted between the snapshot and the check actions.

Email is sent in the event of a change (which is a boolean set if any (or all) of the ccmHistory values changed.

Google email was selected for this project 

Enhancement:  I strip these but I should lower as well.  I don't do alot of error checking particulary with respect to file handling.

### Functions

- load_json(file)
- get_snmp3_info(dev_info)
- print_dict(dict)
- compare_ccmHistory(base, curr)
- sendemail

### Script in "Baseline" Mode

```
Claudia@Mac-mini:~/Dropbox (Indigo Wire Networks)/scripts/python/2016/PyNetACert/week3$ python w3_01_FindConfChg.py 'device_info.json' 'baseline'

ACTION IS BASELINE

Baseline Information for device arctic-sw01.uwaco.net has been saved to file arctic-sw01.uwaco.net-baseline-20161023-174627.json
Claudia@Mac-mini:~/Dropbox (Indigo Wire Networks)/scripts/python/2016/PyNetACert/week3$ 

```

### Script in "Check" Mode without changes

```
Claudia@Mac-mini:~/Dropbox (Indigo Wire Networks)/scripts/python/2016/PyNetACert/week3$ python w3_01_FindConfChg.py 'device_info.json' 'check'

ACTION IS CHECK

BASELINE DATA
sysName:                arctic-sw01.uwaco.net
sysObjectID:            SNMPv2-SMI::enterprises.9.1.540
RunLastChanged:                 467223225
RunLastSaved:           467223432
StartLastChanged:               467223432
ifNumber:               11
sysUpTime:              467371445
time:           		1477269987.26
sysDescr:               Cisco Internetwork Operating System Software 
IOS (tm) C2940 Software (C2940-I6K2L2Q4-M), Version 12.1(22)EA11, RELEASE SOFTWARE (fc2)
Copyright (c) 1986-2008 by cisco Systems, Inc.
Compiled Tue 08-Jan-08 11:14 by amvarma
sysContact:             Indigo Wire Operations

CURRENT DATA
sysName:                arctic-sw01.uwaco.net
sysObjectID:            SNMPv2-SMI::enterprises.9.1.540
RunLastChanged:                 467223225
RunLastSaved:           467223432
StartLastChanged:               467223432
ifNumber:               11
sysUpTime:              467685570
time:           		1477273128.53
sysDescr:               Cisco Internetwork Operating System Software 
IOS (tm) C2940 Software (C2940-I6K2L2Q4-M), Version 12.1(22)EA11, RELEASE SOFTWARE (fc2)
Copyright (c) 1986-2008 by cisco Systems, Inc.
Compiled Tue 08-Jan-08 11:14 by amvarma
sysContact:             Indigo Wire Operations
{'StartLastChanged': 0, 'RunLastChanged': 0, 'RunLastSaved': 0, 'sysUpTime': 52}
StartLastChanged:               0
RunLastChanged:                 0
RunLastSaved:           0
sysUpTime:              52

Device arctic-sw01.uwaco.net has baseline from 52 minutes ago at: Sun Oct 23 17:46:27 2016

Running Configuration has not changed.

Running Configuration has not been saved.

StarupConfiguration has not changed.
Claudia@Mac-mini:~/Dropbox (Indigo Wire Networks)/scripts/python/2016/PyNetACert/week3$ 

```

###Script in "Check" Mode with changes to running and saved to startup

```
....
Device arctic-sw01.uwaco.net has baseline from 54 minutes ago at: Sun Oct 23 17:46:27 2016

Running Configuration changed at approximately Sun Oct 23 18:40:27 2016.  Delta Value: 79

Running Configuration was saved.  Delta Value: 79

Startup Configuration changed. Delta Value: 79
Send Email

```


###Resulting Email

```

----- Forwarded Message -----
From: "delunac@gmail.com" <delunac@gmail.com>
To: c <c@>; l <l@>; d <d@>; e <e@>; l <l@>; u <u@>; n <n@>; a <a@>; y <y@>; a <a@>; h <h@>; o <o@>; o <o@>; . <.@>; c <c@>; o <o@>; m <m@> 
Cc: c <c@>; l <l@>; d <d@>; e <e@>; l <l@>; u <u@>; n <n@>; a <a@>; y <y@>; a <a@>; h <h@>; o <o@>; o <o@>; . <.@>; c <c@>; o <o@>; m <m@>
Sent: Sunday, October 23, 2016 5:20 PM
Subject: Router Configuration Changed: arctic-sw01.uwaco.net


Device arctic-sw01.uwaco.net has baseline from 16 minutes ago at: Sun Oct 23 17:03:40 2016
Running Configuration changed at approximatelySun Oct 23 17:19:40 2016.  Delta Value: 59
Running Configuration has not been saved.
StarupConfiguration has not changed.

w3_01_FindConfChg.py


```

### Exercise 2
Using SNMPv3 create two SVG image files

w3_02_IntGraph.py

This script leverages the functions in the w3_01_FindConfChg.py script and in imported into the Interface Graph script.

- load_json(file)
- get_snmp3_info(dev_info)
- print_dict(dict)
- compare_ccmHistory(oid_list,base, curr)
- compare_iods(oid_list, base, curr)

It also has some functions of its own:

- pygal_plot(dict_of_lists, title, x_labels,output_filename)
- save2json(payload)

The script takes as arguments 
- the JSON Device information file (the same one in fact used for Exercise 1 but with additional OIDS).
- the interface index (for future funcitonality)
- the time interval to poll in seconds

Note:  Future versions should also include the maximum polling time.

Once the device information is loaded in and the device can be queried via SNMPv3 we loop through and poll each time_interval up to the max_monitor interval.

The data returned from the function w3_01_FindConfChg.get_snmp3_info (a dictionary) is appended to a list (list_of_all_gets).  That payload can be saved.

Then there are two sections of the remaining main function. The first generates the Octet graph and the second generates the Packet graph.


```
Claudia@Mac-mini:~/Dropbox/scripts/python/2016/PyNetACert/week3$ python w3_02_IntGraph.py

Usage: w3_02_IntGraph.py <JSON file with device information> <SNMP Interface Index Number> <time interval in seconds>
Example: python w3_02_IntGraph.py "device_info.json" "9" "300"
```



