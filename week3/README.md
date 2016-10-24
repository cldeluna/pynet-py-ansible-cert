## PyNet Week 3 Exercises

### Class3 / SNMPv3, Graphing, and Email

### Exercise 1
Using SNMPv3 create a script that detects router configuration changes.

w3-01-FindCfgChg.py


```
Claudia@Mac-mini:~/Dropbox (Indigo Wire Networks)/scripts/python/2016/PyNetACert/week3$ python w3-01-FindCfgChg.py 'device_info.json'

Usage: w3-01-FindCfgChg.py <JSON file with device information> <Action "baseline" | "check">
Example: python w3-01-FindCfgChg.py python w3-01-FindCfgChg.py "device_info.json" "check"

```
This script takes two arguments, a JSON file with all the information required to establish and SNMP session to one (or more in the future) device and an action.  

Action: 

"snapshot" results in a "snapshot" of all the OIDs in the JSON file "oids.json" which is saved to a file.
"check" results in the latest snapshot file in the directory being selected and loaded in to a "snapshot" dictionary, all variables are refreshed and loaded into a current dictionary and comparisons are made.  A series of if statements are processed to build out a message as to what, if any, changes have ocurred since the snapshot along with the time of the snapshot and the approximate time of the change based on the sysUptime delta.  

Email is sent in the event of a change (which is a boolean set if any (or all) of the ccmHistory values changed.

Google email was selected for this project 

Note:  I strip these but I should lower as well.

```
Claudia@Mac-mini:~/Dropbox (Indigo Wire Networks)/scripts/python/2016/PyNetACert/week3$ python w3-01-FindCfgChg.py 'device_info.json' 'baseline'

ACTION IS BASELINE

Baseline Information for device arctic-sw01.uwaco.net has been saved to file arctic-sw01.uwaco.net-baseline-20161023-174627.json
Claudia@Mac-mini:~/Dropbox (Indigo Wire Networks)/scripts/python/2016/PyNetACert/week3$ 

```
