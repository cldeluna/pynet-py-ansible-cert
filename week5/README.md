#Week 5  [PyNet Python + Ansible] - Class5 / Ansible (Part1)


## Excercise 1 - Create an Ansible playbook that generates five switch configurations based upon the below partial switch configuration. The hostname, ip_addr, and default_gateway should be unique for each switch.

```

(applied_python)[cdeluna@ip-172-30-0-7 week5]$ ansible-playbook access_switch.yml 

PLAY [localhost] ***************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Generate access switch configuration files] ******************************
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.1.1', u'hostname': u'cdl-rtr1', u'secret': u'cisco', u'ip_addr': u'1.1.1.11'})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.2.1', u'hostname': u'cdl-rtr2', u'secret': u'cisco', u'ip_addr': u'1.1.2.12'})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.3.1', u'hostname': u'cdl-rtr3', u'secret': u'cisco', u'ip_addr': u'1.1.3.13'})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.4.1', u'hostname': u'cdl-rtr4', u'secret': u'cisco', u'ip_addr': u'1.1.4.14'})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.5.1', u'hostname': u'cdl-rtr5', u'secret': u'cisco', u'ip_addr': u'1.1.5.15'})

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0   

(applied_python)[cdeluna@ip-172-30-0-7 week5]$ cd CFG
(applied_python)[cdeluna@ip-172-30-0-7 CFG]$ ls
cdl-rtr1.cfg  cdl-rtr2.cfg  cdl-rtr3.cfg  cdl-rtr4.cfg  cdl-rtr5.cfg
(applied_python)[cdeluna@ip-172-30-0-7 CFG]$ 


```

## Excercise 2 - Expand upon the above template by adding a Jinja2 if conditional.  The if conditional should add the below SNMPv3 commands and associated ACL (i.e. if SNMPv3, then the below commands are added into the configuration file).

```

(applied_python)[cdeluna@ip-172-30-0-7 week5]$ ansible-playbook access_switch2.yml 

PLAY [localhost] ***************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Generate access switch configuration files] ******************************
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.1.1', u'hostname': u'cdl-rtr1', u'secret': u'cisco', u'ip_addr': u'1.1.1.11', u'snmpv3': True})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.2.1', u'hostname': u'cdl-rtr2', u'secret': u'cisco', u'ip_addr': u'1.1.2.12', u'snmpv3': False})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.3.1', u'hostname': u'cdl-rtr3', u'secret': u'cisco', u'ip_addr': u'1.1.3.13', u'snmpv3': True})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.4.1', u'hostname': u'cdl-rtr4', u'secret': u'cisco', u'ip_addr': u'1.1.4.14', u'snmpv3': False})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.5.1', u'hostname': u'cdl-rtr5', u'secret': u'cisco', u'ip_addr': u'1.1.5.15', u'snmpv3': True})

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0   

(applied_python)[cdeluna@ip-172-30-0-7 week5]$ cd CFG2
(applied_python)[cdeluna@ip-172-30-0-7 CFG2]$ ls
cdl-rtr1.cfg  cdl-rtr2.cfg  cdl-rtr3.cfg  cdl-rtr4.cfg  cdl-rtr5.cfg
(applied_python)[cdeluna@ip-172-30-0-7 CFG2]$ 


```

## Excercise 3 - In the above access_switch.j2 template use a Jinja2 for loop to create all of the interfaces from FastEthernet 0/1 to FastEthernet 0/24.  Each of the interfaces should have the following configuration.

```
(applied_python)[cdeluna@ip-172-30-0-7 week5]$ ansible-playbook access_switch3.yml 

PLAY [localhost] ***************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Generate access switch configuration files] ******************************
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.1.1', u'hostname': u'cdl-rtr1', u'secret': u'cisco', u'ip_addr': u'1.1.1.11', u'snmpv3': True})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.2.1', u'hostname': u'cdl-rtr2', u'secret': u'cisco', u'ip_addr': u'1.1.2.12', u'snmpv3': False})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.3.1', u'hostname': u'cdl-rtr3', u'secret': u'cisco', u'ip_addr': u'1.1.3.13', u'snmpv3': True})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.4.1', u'hostname': u'cdl-rtr4', u'secret': u'cisco', u'ip_addr': u'1.1.4.14', u'snmpv3': False})
changed: [localhost] => (item={u'access_vlan': 33, u'snmp_community': u'asdfjkl', u'default_gateway': u'1.1.5.1', u'hostname': u'cdl-rtr5', u'secret': u'cisco', u'ip_addr': u'1.1.5.15', u'snmpv3': True})

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0   

(applied_python)[cdeluna@ip-172-30-0-7 week5]$ cd CFG3
(applied_python)[cdeluna@ip-172-30-0-7 CFG3]$ ls
cdl-rtr1.cfg  cdl-rtr2.cfg  cdl-rtr3.cfg  cdl-rtr4.cfg  cdl-rtr5.cfg
(applied_python)[cdeluna@ip-172-30-0-7 CFG3]$ 
```