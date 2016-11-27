
# 

### 1. Using Ansible, configure three VLANs on the Arista switch specifying both the VLAN IDs and the VLAN names. For the VLAN IDs randomly pick three numbers between 100 and 999.

**Before**

```
pynet-sw2#show vlan
VLAN  Name                             Status    Ports
----- -------------------------------- --------- -------------------------------
1     default                          active    Cpu, Et1, Et2, Et3, Et4, Et5
                                                 Et6, Et7
```

**Run Ansible Playbook**
```
(applied_python)[cdeluna@ip-172-30-0-7 week6]$ ansible-playbook week6_ex1a.yml --module-path ~/ANSIBLE/library/

PLAY [Create Arista Vlans by Claudia] ******************************************

TASK [create Vlan from List] *******************
changed: [pynet-sw2] => (item={u'name': u'99ONE', u'vlanid': 991})
changed: [pynet-sw2] => (item={u'name': u'99TWO', u'vlanid': 992})
changed: [pynet-sw2] => (item={u'name': u'99THREE', u'vlanid': 993})
changed: [pynet-sw2] => (item={u'name': u'99FOUR', u'vlanid': 994})

PLAY RECAP *********************************************************************
pynet-sw2                  : ok=1    changed=1    unreachable=0    failed=0   

(applied_python)[cdeluna@ip-172-30-0-7 week6]$ 
```


**After**
```
pynet-sw2#show vlan
VLAN  Name                             Status    Ports
----- -------------------------------- --------- -------------------------------
1     default                          active    Cpu, Et1, Et2, Et3, Et4, Et5
                                                 Et6, Et7
991   99ONE                            active   
992   99TWO                            active   
993   99THREE                          active   
994   99FOUR                           active   

pynet-sw2#
```


### 2. Use Ansible to configure your 'primary Ethernet interface': 

interface description:     *** IN USE ***
switchport mode:          access
VLAN:                     991

**Before**
```
pynet-sw2#show run int eth6
interface Ethernet6
pynet-sw2#

```

**Run Ansible Playbook**
```

(applied_python)[cdeluna@ip-172-30-0-7 week6]$ ansible-playbook week6_ex2.yml --module-path ~/ANSIBLE/library/

PLAY [Configure Arista Interface by Claudia] ***********************************

TASK [Configure Primary Ethernet Interface Description] ************************
changed: [pynet-sw2] => (item={u'int': u'Ethernet6', u'vlanid': 991, u'desc': u'*** IN USE ***'})

TASK [Configure Primary Ethernet Interface Characteristics] ********************
changed: [pynet-sw2] => (item={u'int': u'Ethernet6', u'vlanid': 991, u'desc': u'*** IN USE ***'})

PLAY RECAP *********************************************************************
pynet-sw2                  : ok=2    changed=2    unreachable=0    failed=0   

(applied_python)[cdeluna@ip-172-30-0-7 week6]$ 

```

**After**
```
pynet-sw2#show run int eth6
interface Ethernet6
   description *** IN USE ***
   switchport access vlan 991
pynet-sw2#

```


### 3. Use Ansible to configure your 'primary Ethernet interface' as follows:

switchport mode:           trunk
trunk native VLAN:        VLAN1
trunk allowed VLANs:   991,992,993,994


**Before**
```
pynet-sw2#show run int eth6
interface Ethernet6
   description *** IN USE ***
   switchport access vlan 991


```

**Run Ansible Playbook**
```
(applied_python)[cdeluna@ip-172-30-0-7 week6]$ ansible-playbook week6_ex3.yaml --module-path ~/ANSIBLE/library/

PLAY [Configure Arista Trunk Interface by Claudia] *****************************

TASK [Default Interface] *******************************************************
changed: [pynet-sw2]

TASK [debug] *******************************************************************
ok: [pynet-sw2] => {
    "int_output": {
        "changed": true, 
        "changes": {}
    }
}

TASK [Configure Primary Ethernet Interface Description] ************************
changed: [pynet-sw2] => (item={u'int': u'Ethernet6', u'desc': u'*** TRUNK ***'})

TASK [Configure Primary Ethernet Interface Trunk Characteristics] **************
changed: [pynet-sw2] => (item={u'int': u'Ethernet6', u'vlanids': u'991,992,993,994'})

PLAY RECAP *********************************************************************
pynet-sw2                  : ok=4    changed=3    unreachable=0    failed=0   




```

**After first Task**
```
pynet-sw2#show run int eth6
interface Ethernet6
pynet-sw2#


```


**After complete run**
```
pynet-sw2#show run int eth6
interface Ethernet6
   description *** TRUNK ***
   switchport trunk allowed vlan 991-994
   switchport mode trunk
pynet-sw2#


```



### 4. Use Ansible to restore your 'primary Ethernet interface' back to the following state (or your secondary interface depending on which one you used):

description:                    ''
switchport mode:           access
access VLAN:                1
trunk allowed VLANs:    all

Also use Ansible to remove the three VLANs that you configured.




**Before**
```
pynet-sw2#show vlan
VLAN  Name                             Status    Ports
----- -------------------------------- --------- -------------------------------
1     default                          active    Cpu, Et1, Et2, Et3, Et4, Et5
                                                 Et7
991   99ONE                            active    Et6
992   99TWO                            active    Et6
993   99THREE                          active    Et6
994   99FOUR                           active    Et6

pynet-sw2#show run int Eth6
interface Ethernet6
   description *** TRUNK ***
   switchport trunk allowed vlan 991-994
   switchport mode trunk
pynet-sw2#


```

**Run Ansible Playbook**
```
(applied_python)[cdeluna@ip-172-30-0-7 week6]$ ansible-playbook week6_ex4.yml --module-path ~/ANSIBLE/library/

PLAY [Clean up Arista Trunk Interface by Claudia] ******************************

TASK [Default Interface] *******************************************************
changed: [pynet-sw2]

TASK [debug] *******************************************************************
ok: [pynet-sw2] => {
    "int_output": {
        "changed": true, 
        "changes": {}
    }
}

TASK [Remove Vlans] ************************************************************
changed: [pynet-sw2] => (item=991)
changed: [pynet-sw2] => (item=992)
changed: [pynet-sw2] => (item=993)
changed: [pynet-sw2] => (item=994)

PLAY RECAP *********************************************************************
pynet-sw2                  : ok=3    changed=2    unreachable=0    failed=0   




```

**After**
```
pynet-sw2#show vlan
VLAN  Name                             Status    Ports
----- -------------------------------- --------- -------------------------------
1     default                          active    Cpu, Et1, Et2, Et3, Et4, Et5
                                                 Et6, Et7

pynet-sw2#show run int Eth6
interface Ethernet6
pynet-sw2#


```


### 5. Use the cisco_file_transfer.py module to transfer a small file to the Cisco pynet-rtr1 router.


**Before**
```
pynet-rtr1#dir | i cdl
pynet-rtr1#


```

**Run Ansible Playbook**
```
(applied_python)[cdeluna@ip-172-30-0-7 week6]$ ansible-playbook week6_ex5.yml --module-path ~/ANSIBLE/library/

PLAY [Transfer file to Cisco Router] *******************************************

TASK [Testing File Transfer] ***************************************************
changed: [pynet-rtr1]

TASK [debug] *******************************************************************
ok: [pynet-rtr1] => {
    "file_output": {
        "changed": true, 
        "msg": "File successfully transferred to remote device"
    }
}

PLAY RECAP *********************************************************************
pynet-rtr1                 : ok=2    changed=1    unreachable=0    failed=0   




```

**After**
```
pynet-rtr1#dir | i cdl
   72  -rw-         277  Nov 27 2016 11:02:16 -08:00  cdl_cisco_acl.txt
pynet-rtr1#


```
