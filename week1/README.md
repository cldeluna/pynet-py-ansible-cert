## PyNet Class Working Directory
Claudia de Luna
cldeluna@yahoo.com

---
Week 1 - 2016-07-28
---
All git/GitHub actions completed.

###YAML/JSON Write:
This scripts takes in one argument, a cisco based configuration file with vlan information.  Using CiscoConfigParse, the file is parsed and the vlan parent child information is extracted.  The resulting elements are split using a space as a delimiter and elements 0 and 1 are used as key and value pairs respectively to generate a list of dictionaries.  The resulting data structures are saved in YAML and JSON formatted files.  The stdout output shows each element alont with the element type and the number of elements.

```
(applied_python)[cdeluna@ip-172-30-0-4 scratch]$ ls week1*
ls: cannot access week1*: No such file or directory
(applied_python)[cdeluna@ip-172-30-0-4 scratch]$ python w1-06-yml-json-w.py sin-dist-shrunonly.txt 


**************List of Dictionaries*****************
('Type is ', <type 'list'>)
('Total Vlans Found: ', '26')


{'vlan': '1,3,101,103-106,300,310,340,350,500,560-564,570-574,581,585,590-591'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 1)
{'vlan': '3', 'name': 'sin1-default'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '101', 'name': 'sin1-nvn-core-101'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '103', 'name': 'sin1-nvn-monitor-103'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '104', 'name': 'sin1-gvn-mgmt-104'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '105', 'name': 'sin1-gvn-vmotion-mgmt-105'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '106', 'name': 'sin1-nvn-sec-106'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '300', 'name': 'sin1-uc-vn-300'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '310', 'name': 'sin1-uc-vn-310-dmz'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '340', 'name': 'sin1-uc-vn-vmotion-340'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '350', 'name': 'sin1-uc-vn-350'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '500', 'name': 'sin1-avn-airsupport-500'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '560', 'name': 'sin1-gvn-gtlib-pd-560'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '561', 'name': 'sin1-gvn-gservers-pd-561'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '562', 'name': 'sin1-gvn-gvoip-pd-562'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '563', 'name': 'sin1-gvn-gafe-pd-563'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '564', 'name': 'sin1-gvn-gmgmt-pd-564'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '570', 'name': 'sin1-gvn-gtlib-570'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '571', 'name': 'sin1-gvn-gservers-571'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '572', 'name': 'sin1-gvn-gvoip-572'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '573', 'name': 'sin1-gvn-gafe-573'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '574', 'name': 'sin1-gvn-gmgmt-574'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '581', 'name': 'sin1-gvn-gvmotion-581'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '585', 'name': 'sin1-gvn-server-pxe-585'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '590', 'name': 'sin1-svn-590'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
{'vlan': '591', 'name': 'sin1-svn-aaa-591'} (' Type = ', <type 'dict'>) (' Number of Elements = ', 2)
(applied_python)[cdeluna@ip-172-30-0-4 scratch]$ ls week1*
week1-json-output.json  week1-yaml-output.yml
(applied_python)[cdeluna@ip-172-30-0-4 scratch]$ 

```

###YAML/JSON READ

```

(applied_python)[cdeluna@ip-172-30-0-4 scratch]$ python w1-07-yml-json-r.py

Usage: w1-07-yml-json-r.py <path to directory in which to look for JSON or YML files> 
This script will find all files with a .yml or .json file extension and Pretty Print each file.
Example: python w1-07-yml-json-r.py "."




(applied_python)[cdeluna@ip-172-30-0-4 scratch]$ python w1-07-yml-json-r.py "."
week1-json-output.json
week1-yaml-output.yml
donut.json


************** Printing JSON File Contents ************** 

('File name: ', 'week1-json-output.json')
[{u'vlan': u'1,3,101,103-106,300,310,340,350,500,560-564,570-574,581,585,590-591'},
 {u'name': u'sin1-default', u'vlan': u'3'},
 {u'name': u'sin1-nvn-core-101', u'vlan': u'101'},
 {u'name': u'sin1-nvn-monitor-103', u'vlan': u'103'},
 {u'name': u'sin1-gvn-mgmt-104', u'vlan': u'104'},
 {u'name': u'sin1-gvn-vmotion-mgmt-105', u'vlan': u'105'},
 {u'name': u'sin1-nvn-sec-106', u'vlan': u'106'},
 {u'name': u'sin1-uc-vn-300', u'vlan': u'300'},
 {u'name': u'sin1-uc-vn-310-dmz', u'vlan': u'310'},
 {u'name': u'sin1-uc-vn-vmotion-340', u'vlan': u'340'},
 {u'name': u'sin1-uc-vn-350', u'vlan': u'350'},
 {u'name': u'sin1-avn-airsupport-500', u'vlan': u'500'},
 {u'name': u'sin1-gvn-gtlib-pd-560', u'vlan': u'560'},
 {u'name': u'sin1-gvn-gservers-pd-561', u'vlan': u'561'},
 {u'name': u'sin1-gvn-gvoip-pd-562', u'vlan': u'562'},
 {u'name': u'sin1-gvn-gafe-pd-563', u'vlan': u'563'},
 {u'name': u'sin1-gvn-gmgmt-pd-564', u'vlan': u'564'},
 {u'name': u'sin1-gvn-gtlib-570', u'vlan': u'570'},
 {u'name': u'sin1-gvn-gservers-571', u'vlan': u'571'},
 {u'name': u'sin1-gvn-gvoip-572', u'vlan': u'572'},
 {u'name': u'sin1-gvn-gafe-573', u'vlan': u'573'},
 {u'name': u'sin1-gvn-gmgmt-574', u'vlan': u'574'},
 {u'name': u'sin1-gvn-gvmotion-581', u'vlan': u'581'},
 {u'name': u'sin1-gvn-server-pxe-585', u'vlan': u'585'},
 {u'name': u'sin1-svn-590', u'vlan': u'590'},
 {u'name': u'sin1-svn-aaa-591', u'vlan': u'591'}]


************** Printing YAML File Contents ************** 

('File name: ', 'week1-yaml-output.yml')
[{'vlan': '1,3,101,103-106,300,310,340,350,500,560-564,570-574,581,585,590-591'},
 {'name': 'sin1-default', 'vlan': '3'},
 {'name': 'sin1-nvn-core-101', 'vlan': '101'},
 {'name': 'sin1-nvn-monitor-103', 'vlan': '103'},
 {'name': 'sin1-gvn-mgmt-104', 'vlan': '104'},
 {'name': 'sin1-gvn-vmotion-mgmt-105', 'vlan': '105'},
 {'name': 'sin1-nvn-sec-106', 'vlan': '106'},
 {'name': 'sin1-uc-vn-300', 'vlan': '300'},
 {'name': 'sin1-uc-vn-310-dmz', 'vlan': '310'},
 {'name': 'sin1-uc-vn-vmotion-340', 'vlan': '340'},
 {'name': 'sin1-uc-vn-350', 'vlan': '350'},
 {'name': 'sin1-avn-airsupport-500', 'vlan': '500'},
 {'name': 'sin1-gvn-gtlib-pd-560', 'vlan': '560'},
 {'name': 'sin1-gvn-gservers-pd-561', 'vlan': '561'},
 {'name': 'sin1-gvn-gvoip-pd-562', 'vlan': '562'},
 {'name': 'sin1-gvn-gafe-pd-563', 'vlan': '563'},
 {'name': 'sin1-gvn-gmgmt-pd-564', 'vlan': '564'},
 {'name': 'sin1-gvn-gtlib-570', 'vlan': '570'},
 {'name': 'sin1-gvn-gservers-571', 'vlan': '571'},
 {'name': 'sin1-gvn-gvoip-572', 'vlan': '572'},
 {'name': 'sin1-gvn-gafe-573', 'vlan': '573'},
 {'name': 'sin1-gvn-gmgmt-574', 'vlan': '574'},
 {'name': 'sin1-gvn-gvmotion-581', 'vlan': '581'},
 {'name': 'sin1-gvn-server-pxe-585', 'vlan': '585'},
 {'name': 'sin1-svn-590', 'vlan': '590'},
 {'name': 'sin1-svn-aaa-591', 'vlan': '591'}]


************** Printing JSON File Contents ************** 

('File name: ', 'donut.json')
{u'batters': {u'batter': [{u'id': u'1001', u'type': u'Regular'},
                          {u'id': u'1002', u'type': u'Chocolate'},
                          {u'id': u'1003', u'type': u'Blueberry'},
                          {u'id': u'1004', u'type': u"Devil's Food"}]},
 u'id': u'0001',
 u'name': u'Cake',
 u'ppu': 0.55,
 u'topping': [{u'id': u'5001', u'type': u'None'},
              {u'id': u'5002', u'type': u'Glazed'},
              {u'id': u'5005', u'type': u'Sugar'},
              {u'id': u'5007', u'type': u'Powdered Sugar'},
              {u'id': u'5006', u'type': u'Chocolate with Sprinkles'},
              {u'id': u'5003', u'type': u'Chocolate'},
              {u'id': u'5004', u'type': u'Maple'}],
 u'type': u'donut'}
(applied_python)[cdeluna@ip-172-30-0-4 scratch]$ 


```
###CiscoConfigParse Parent/Child/Search

```
D:\Dropbox (Indigo Wire Networks)\scripts\python\2016\PyNetA>python w1-08-ccp-crypto.py

====PARENT LEVEL ITEMS===
crypto map CRYPTO 10 ipsec-isakmp
crypto map CRYPTO 20 ipsec-isakmp
crypto map CRYPTO 30 ipsec-isakmp
crypto map CRYPTO 40 ipsec-isakmp
crypto map CRYPTO 50 ipsec-isakmp



===PARENT=== crypto map CRYPTO 10 ipsec-isakmp
=======CHILD LEVEL ITEMS======
 set peer 1.1.1.1
 set transform-set AES-SHA
 set pfs group5
 match address VPN-TEST1

|
===PARENT=== crypto map CRYPTO 20 ipsec-isakmp
=======CHILD LEVEL ITEMS======
 set peer 2.2.2.1
 set transform-set AES-SHA
 set pfs group2
 match address VPN-TEST2

|
===PARENT=== crypto map CRYPTO 30 ipsec-isakmp
=======CHILD LEVEL ITEMS======
 set peer 3.3.3.1
 set transform-set AES-SHA
 set pfs group2
 match address VPN-TEST3

|
===PARENT=== crypto map CRYPTO 40 ipsec-isakmp
=======CHILD LEVEL ITEMS======
 set peer 4.4.4.1
 set transform-set AES-SHA
 set pfs group5
 match address VPN-TEST4

|
===PARENT=== crypto map CRYPTO 50 ipsec-isakmp
=======CHILD LEVEL ITEMS======
 set peer 5.5.5.1
 set transform-set 3DES-SHA
 set pfs group5
 match address VPN-TEST5

|


====PARENT LEVEL ITEMS in SEARCH for PFS Group2===
crypto map CRYPTO 20 ipsec-isakmp 
Parent: True
Children: False
Children items: [<IOSCfgLine # 93 ' set peer 2.2.2.1' (parent is # 92)>, <IOSCfgLine # 94 ' set transform-set AES-SHA ' (parent is # 92)>, <IOSCfgLine # 95 ' set pfs group2' (parent is # 92)>, <IOSCfgLine # 96 ' match address VPN-TEST2' (parent is # 92)>]
crypto map CRYPTO 30 ipsec-isakmp 
Parent: True
Children: False
Children items: [<IOSCfgLine # 98 ' set peer 3.3.3.1' (parent is # 97)>, <IOSCfgLine # 99 ' set transform-set AES-SHA ' (parent is # 97)>, <IOSCfgLine # 100 ' set pfs group2' (parent is # 97)>, <IOSCfgLine # 101 ' match address VPN-TEST3' (parent is # 97)>]



====PARENT LEVEL ITEMS in SEARCH for !AES===
crypto map CRYPTO 50 ipsec-isakmp 
Parent: True
Children: False
Children items: [<IOSCfgLine # 108 ' set peer 5.5.5.1' (parent is # 107)>, <IOSCfgLine # 109 ' set transform-set 3DES-SHA ' (parent is # 107)>, <IOSCfgLine # 110 ' set pfs group5' (parent is # 107)>, <IOSCfgLine # 111 ' match address VPN-TEST5' (parent is # 107)>]


(applied_python)[cdeluna@ip-172-30-0-4 scratch]$ 

```
