
# : [PyNet Python + Ansible] - Class8 / Integrating to a Database and Concurrency


1. Initialize your Django database. Add the seven NetworkDevice objects and two Credentials objects into your database

```

(applied_python)[cdeluna@ip-172-30-0-7 djproject]$ ls
djproject  manage.py  net_system
(applied_python)[cdeluna@ip-172-30-0-7 djproject]$ python manage.py makemigrations
Migrations for 'net_system':
  0001_initial.py:
    - Create model Credentials
    - Create model NetworkDevice
(applied_python)[cdeluna@ip-172-30-0-7 djproject]$ # Have a Blank DB now
(applied_python)[cdeluna@ip-172-30-0-7 djproject]$ python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, contenttypes, net_system, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying net_system.0001_initial... OK
  Applying sessions.0001_initial... OK
(applied_python)[cdeluna@ip-172-30-0-7 djproject]$ cd net_system/
(applied_python)[cdeluna@ip-172-30-0-7 net_system]$ ls
admin.py   __init__.py   load_credentials.py  migrations  models.pyc  views.py
admin.pyc  __init__.pyc  load_devices.py      models.py   tests.py
(applied_python)[cdeluna@ip-172-30-0-7 net_system]$ python load_devices.py

admin.pyc  __init__.pyc  load_devices.py      models.py   tests.py
(applied_python)[cdeluna@ip-172-30-0-7 net_system]$ python load_devices.py 
(<NetworkDevice: pynet-rtr2>, True)
(<NetworkDevice: pynet-sw1>, True)
(<NetworkDevice: pynet-sw2>, True)
(<NetworkDevice: pynet-sw3>, True)
(<NetworkDevice: pynet-sw4>, True)
(<NetworkDevice: juniper-srx>, True)
(applied_python)[cdeluna@ip-172-30-0-7 net_system]$ python load_credentials.py 
(<Credentials: pyclass>, True)
(<Credentials: admin1>, True)
(applied_python)[cdeluna@ip-172-30-0-7 net_system]$ 
(applied_python)[cdeluna@ip-172-30-0-7 net_system]$ 
(applied_python)[cdeluna@ip-172-30-0-7 net_system]$ cd ..
(applied_python)[cdeluna@ip-172-30-0-7 djproject]$ python manage.py shell
Python 2.7.12 (default, Sep  1 2016, 22:14:00) 
[GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from net_system.models import NetworkDevice
>>> NetworkDevice.objects.all()
[<NetworkDevice: pynet-rtr1>, <NetworkDevice: pynet-rtr2>, <NetworkDevice: pynet-sw1>, <NetworkDevice: pynet-sw2>, <NetworkDevice: pynet-sw3>, <NetworkDevice: pynet-sw4>, <NetworkDevice: juniper-srx>]
>>> devs = NetworkDevice.objects.all()
>>> devs
[<NetworkDevice: pynet-rtr1>, <NetworkDevice: pynet-rtr2>, <NetworkDevice: pynet-sw1>, <NetworkDevice: pynet-sw2>, <NetworkDevice: pynet-sw3>, <NetworkDevice: pynet-sw4>, <NetworkDevice: juniper-srx>]
>>> type(devs)
<class 'django.db.models.query.QuerySet'>
>>> creds = Credentials.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Credentials' is not defined
>>> from net_system.models import NetworkDevice, Credentials
>>> type(devs)
<class 'django.db.models.query.QuerySet'>
>>> creds = Credentials.objects.all()
>>> creds
[<Credentials: pyclass>, <Credentials: admin1>]
>>> type(creds)
<class 'django.db.models.query.QuerySet'>
>>> dir(creds)
['__and__', '__bool__', '__class__', '__deepcopy__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__getstate__', '__hash__', '__init__', '__iter__', '__len__', '__module__', '__new__', '__nonzero__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_hints', '_as_sql', '_batched_insert', '_clone', '_create_object_from_params', '_db', '_earliest_or_latest', '_extract_model_params', '_fetch_all', '_filter_or_exclude', '_for_write', '_has_filters', '_hints', '_insert', '_known_related_objects', '_merge_known_related_objects', '_merge_sanity_check', '_next_is_sticky', '_populate_pk_values', '_prefetch_done', '_prefetch_related_lookups', '_prefetch_related_objects', '_prepare', '_raw_delete', '_result_cache', '_setup_aggregate_query', '_sticky_filter', '_update', 'aggregate', 'all', 'annotate', 'as_manager', 'bulk_create', 'complex_filter', 'count', 'create', 'dates', 'datetimes', 'db', 'defer', 'delete', 'distinct', 'earliest', 'exclude', 'exists', 'extra', 'filter', 'first', 'get', 'get_or_create', 'in_bulk', 'is_compatible_query_object_type', 'iterator', 'last', 'latest', 'model', 'none', 'only', 'order_by', 'ordered', 'prefetch_related', 'query', 'raw', 'reverse', 'select_for_update', 'select_related', 'update', 'update_or_create', 'using', 'value_annotation', 'values', 'values_list']
>>> help(creds)

```

    b. Update the NetworkDevice objects such that each NetworkDevice links to the correct Credentials.

```
>>> creds
[<Credentials: pyclass>, <Credentials: admin1>]
>>> devs
[<NetworkDevice: pynet-rtr1>, <NetworkDevice: pynet-rtr2>, <NetworkDevice: pynet-sw1>, <NetworkDevice: pynet-sw2>, <NetworkDevice: pynet-sw3>, <NetworkDevice: pynet-sw4>, <NetworkDevice: juniper-srx>]
>>> std_creds = creds[0]
>>> arista_creds = creds[1]
>>> std_creds
<Credentials: pyclass>
>>> type(std_creds)
<class 'net_system.models.Credentials'>
>>> arista_creds
<Credentials: admin1>
>>> for a_dev in devs:
...   if 'pynet-sw' in a_dev.device_name:
...     a_dev.credentials = arista_creds
...   else:
...     a_dev.credentials = std_creds
...   a_dev.save()
... 
>>> for a_dev in devs:
...   print a_dev, a_dev.credentials
... 
pynet-rtr1 pyclass
pynet-rtr2 pyclass
pynet-sw1 admin1
pynet-sw2 admin1
pynet-sw3 admin1
pynet-sw4 admin1
juniper-srx pyclass
>>> for a_dev in devs:
...   print a_dev, a_dev.credentials.username
... 
pynet-rtr1 pyclass
pynet-rtr2 pyclass
pynet-sw1 admin1
pynet-sw2 admin1
pynet-sw3 admin1
pynet-sw4 admin1
juniper-srx pyclass
>>> for a_dev in devs:
...   print a_dev, a_dev.credentials.username, a_dev.credentials.password
... 
pynet-rtr1 pyclass 88newclass
pynet-rtr2 pyclass 88newclass
pynet-sw1 admin1 99saturday
pynet-sw2 admin1 99saturday
pynet-sw3 admin1 99saturday
pynet-sw4 admin1 99saturday
juniper-srx pyclass 88newclass
>>> arista_creds.networkdevice_set.all()
[<NetworkDevice: pynet-sw1>, <NetworkDevice: pynet-sw2>, <NetworkDevice: pynet-sw3>, <NetworkDevice: pynet-sw4>]
>>> std_creds.networkdevice_set.all()
[<NetworkDevice: pynet-rtr1>, <NetworkDevice: pynet-rtr2>, <NetworkDevice: juniper-srx>]
```


2. Set the vendor field of each NetworkDevice to the appropriate vendor. Save this field to the database.


```

>>> for a_dev in devs:
...   if 'pynet-sw' in a_dev.device_name:
...     a_dev.vendor = "Arista Switch"
...   elif 'srx' in a_dev.device_name:
...     a_dev.vendor = "Juniper Router"
...   else:
...     a_dev.vendor = "Cisco Router"
...   a_dev.save()
... 
>>> for a_dev in devs:
...   print a_dev, a_dev.vendor
... 
pynet-rtr1 Cisco Router
pynet-rtr2 Cisco Router
pynet-sw1 Arista Switch
pynet-sw2 Arista Switch
pynet-sw3 Arista Switch
pynet-sw4 Arista Switch
juniper-srx Juniper Router
>>> 


```

## Exercises 3 - 7 can be executed using the appropriate argument to the wk8_db_th_proc.py script

```

(applied_python)[cdeluna@ip-172-30-0-7 week8]$ python wk8_db_th_proc.py -h
usage: wk8_db_th_proc.py [-h] [-3] [-4] [-5] [-6] [-7] [-l]

[PyNet Python + Ansible] - Class8 / Integrating to a Database and Concurrency

optional arguments:
  -h, --help           show this help message and exit
  -3, --adddev         Week8 Ex3 add device to DB.
  -4, --deldev         Week8 Ex4 Remove device from DB.
  -5, --connect        Week8 Ex5 Connect to devices in DB and execute show
                       command
  -6, --threadconnect  Week8 Ex6 Connect to devices in DB and execute show
                       command using threads
  -7, --procconnect    Week8 Ex7 Connect to devices in DB and execute show
                       command using processes.
  -l, --list           Week8 - List DB

Usage: ' python wk8_db_th_proc.py'
(applied_python)[cdeluna@ip-172-30-0-7 week8]$ 

```

## Exercise 3

```
(applied_python)[cdeluna@ip-172-30-0-7 week8]$ python wk8_db_th_proc.py -3
-----------------------------
Database Objects prior to ADD
-----------------------------

Network Devices
pynet-rtr1
pynet-rtr2
pynet-sw1
pynet-sw2
pynet-sw3
pynet-sw4
juniper-srx

Network Device Credentials
pyclass
admin1
-----------------------------


Check for device in DB prior to add (default = Y)? Y|N: N
ADD Device Name: cdl-rtr1  
Device Type cisco_ios | cisco_nxos etc.: cisco_ios
Device IP: "2.2.2.2"
Device Credentials pyclass | admin1: pyclass
NOT checking DB prior to add!
<class 'net_system.models.NetworkDevice'>
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', u'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_base_manager', '_check_column_name_clashes', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_ordering', '_check_swappable', '_check_unique_together', '_credentials_cache', '_default_manager', '_deferred', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'check', 'clean', 'clean_fields', 'credentials', 'credentials_id', 'date_error_message', 'delete', 'device_name', 'device_type', 'from_db', 'full_clean', 'get_deferred_fields', 'ip_address', 'model', 'objects', 'os_version', 'pk', 'port', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serial_number', 'serializable_value', 'unique_error_message', 'uptime_seconds', 'validate_unique', 'vendor']
cdl-rtr1
--------------------------
Database Objects after ADD
--------------------------

Network Devices
pynet-rtr1
pynet-rtr2
pynet-sw1
pynet-sw2
pynet-sw3
pynet-sw4
juniper-srx
cdl-rtr1

Network Device Credentials
pyclass
admin1
--------------------------


(applied_python)[cdeluna@ip-172-30-0-7 week8]$ 

```

## Exercise 4


```

(applied_python)[cdeluna@ip-172-30-0-7 week8]$ python wk8_db_th_proc.py -4
--------------------------------
Database Objects prior to DELETE
--------------------------------

Network Devices
pynet-rtr1
pynet-rtr2
pynet-sw1
pynet-sw2
pynet-sw3
pynet-sw4
juniper-srx
cdl-rtr1

Network Device Credentials
pyclass
admin1
--------------------------------


DELETE Device Name: cdl-rtr1
-----------------------------
Database Objects after DELETE
-----------------------------

Network Devices
pynet-rtr1
pynet-rtr2
pynet-sw1
pynet-sw2
pynet-sw3
pynet-sw4
juniper-srx

Network Device Credentials
pyclass
admin1
-----------------------------


(applied_python)[cdeluna@ip-172-30-0-7 week8]$ 

```


## Exercise 5


```

(applied_python)[cdeluna@ip-172-30-0-7 week8]$ python wk8_db_th_proc.py -5
-------------------------------
Database Objects to Connect to.
-------------------------------

Network Devices
pynet-rtr1
pynet-rtr2
pynet-sw1
pynet-sw2
pynet-sw3
pynet-sw4
juniper-srx

Network Device Credentials
pyclass
admin1
-------------------------------


Show command to execute on each device (default is show version): 


=====================================================
Executing command <show version> on device pynet-rtr1
=====================================================
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Thu 26-Jun-14 14:15 by prod_rel_team

ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

pynet-rtr1 uptime is 32 weeks, 4 days, 5 hours, 36 minutes
System returned to ROM by reload
System restarted at 12:42:49 PDT Wed Jun 22 2016
System image file is "flash:c880data-universalk9-mz.154-2.T1.bin"
Last reload type: Normal Reload
Last reload reason: power-on



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
Processor board ID FTX1512038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)


License Info:

License UDI:

-------------------------------------------------
Device#	  PID			SN
-------------------------------------------------
*0  	  CISCO881-SEC-K9       FTX1512038X     



License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices


Configuration register is 0x2102



=====================================================
Executing command <show version> on device pynet-rtr2
=====================================================
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Thu 26-Jun-14 14:15 by prod_rel_team

ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

pynet-rtr2 uptime is 30 weeks, 3 days, 5 hours, 43 minutes
System returned to ROM by reload at 19:10:00 UTC Thu Jul 7 2016
System restarted at 12:35:53 PDT Thu Jul 7 2016
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



====================================================
Executing command <show version> on device pynet-sw1
====================================================
Arista vEOS
Hardware version:    
Serial number:       
System MAC address:  5254.aba8.9aea

Software image version: 4.15.4F
Architecture:           i386
Internal build version: 4.15.4F-2923910.4154F
Internal build ID:      d8a3c846-c735-4766-93cd-82bb7427da51

Uptime:                 4 weeks, 3 days, 1 hour and 14 minutes
Total memory:           3893916 kB
Free memory:            1322976 kB



====================================================
Executing command <show version> on device pynet-sw2
====================================================
Arista vEOS
Hardware version:    
Serial number:       
System MAC address:  5254.abbe.5b7b

Software image version: 4.15.4F
Architecture:           i386
Internal build version: 4.15.4F-2923910.4154F
Internal build ID:      d8a3c846-c735-4766-93cd-82bb7427da51

Uptime:                 4 weeks, 3 days, 1 hour and 14 minutes
Total memory:           3893916 kB
Free memory:            1296648 kB



====================================================
Executing command <show version> on device pynet-sw3
====================================================
Arista vEOS
Hardware version:    
Serial number:       
System MAC address:  5254.ab71.e119

Software image version: 4.15.4F
Architecture:           i386
Internal build version: 4.15.4F-2923910.4154F
Internal build ID:      d8a3c846-c735-4766-93cd-82bb7427da51

Uptime:                 4 weeks, 3 days, 1 hour and 14 minutes
Total memory:           3893916 kB
Free memory:            1288720 kB



====================================================
Executing command <show version> on device pynet-sw4
====================================================
Arista vEOS
Hardware version:    
Serial number:       
System MAC address:  5254.ab81.5693

Software image version: 4.15.4F
Architecture:           i386
Internal build version: 4.15.4F-2923910.4154F
Internal build ID:      d8a3c846-c735-4766-93cd-82bb7427da51

Uptime:                 4 weeks, 3 days, 1 hour and 14 minutes
Total memory:           3893916 kB
Free memory:            1288760 kB



======================================================
Executing command <show version> on device juniper-srx
======================================================

Hostname: pynet-jnpr-srx1
Model: srx100h2
JUNOS Software Release [12.1X44-D35.5]

Elapsed time: 0:00:41.229619
(applied_python)[cdeluna@ip-172-30-0-7 week8]$ 


```


## Exercise 6

Elapsed time: 0:00:16.952990
Single Threaded Time: 0:00:45.968365

```
(applied_python)[cdeluna@ip-172-30-0-7 week8]$ python wk8_db_th_proc.py -6
-------------------------------
Database Objects to Connect to.
-------------------------------

Network Devices
pynet-rtr1
pynet-rtr2
pynet-sw1
pynet-sw2
pynet-sw3
pynet-sw4
juniper-srx

Network Device Credentials
pyclass
admin1
-------------------------------


Show command to execute on each device (default is show version): sh run | i hostname
<Thread(Thread-1, started 140378777409280)>


============================================================
Executing command <sh run | i hostname> on device pynet-rtr2
============================================================


============================================================
Executing command <sh run | i hostname> on device pynet-rtr1
============================================================
hostname pynet-rtr2
hostname pynet-rtr1
<Thread(Thread-3, started 140378760361728)>


=============================================================
Executing command <sh run | i hostname> on device juniper-srx
=============================================================
                              ^
syntax error, expecting <command>.
pyclass@pynet-jnpr-srx1> show run   |
                              ^
syntax error, expecting <command>.
pyclass@pynet-jnpr-srx1> show run|   i
                              ^
syntax error, expecting <command>.
pyclass@pynet-jnpr-srx1> show run|i   hostname
                              ^
syntax error, expecting <command>.



===========================================================
Executing command <sh run | i hostname> on device pynet-sw1
===========================================================


===========================================================
Executing command <sh run | i hostname> on device pynet-sw2
===========================================================


===========================================================
Executing command <sh run | i hostname> on device pynet-sw3
===========================================================


===========================================================
Executing command <sh run | i hostname> on device pynet-sw4
===========================================================
hostname pynet-sw2
hostname pynet-sw1
<Thread(Thread-2, stopped 140378769016576)>
<Thread(Thread-7, started 140378388821760)>
hostname pynet-sw3
hostname pynet-sw4
<paramiko.Transport at 0x7b2c0510L (unconnected)>
<Thread(Thread-5, stopped 140378743576320)>
<Thread(Thread-4, stopped 140378751969024)>
<paramiko.Transport at 0x7a25c410L (unconnected)>
<Thread(Thread-8, stopped 140378380429056)>
Elapsed time: 0:00:16.952990
Single Threaded Time: 0:00:45.968365
(applied_python)[cdeluna@ip-172-30-0-7 week8]$ 

```


## Exercise 7

Multi Process Elapsed time: 0:00:16.031519
Single Threaded Time: 0:00:45.968365
Multi Threaded Time: 0:00:10.987360

```
(applied_python)[cdeluna@ip-172-30-0-7 week8]$ python wk8_db_th_proc.py -7
-------------------------------
Database Objects to Connect to.
-------------------------------

Network Devices
pynet-rtr1
pynet-rtr2
pynet-sw1
pynet-sw2
pynet-sw3
pynet-sw4
juniper-srx

Network Device Credentials
pyclass
admin1
-------------------------------


Show command to execute on each device (default is show version): sh run | i hostname
<Process(Process-1, started)>


============================================================
Executing command <sh run | i hostname> on device pynet-rtr1
============================================================


============================================================
Executing command <sh run | i hostname> on device pynet-rtr2
============================================================
hostname pynet-rtr2
hostname pynet-rtr1
<Process(Process-2, stopped)>
<Process(Process-3, started)>


=============================================================
Executing command <sh run | i hostname> on device juniper-srx
=============================================================
                              ^
syntax error, expecting <command>.
pyclass@pynet-jnpr-srx1> show run   |
                              ^
syntax error, expecting <command>.
pyclass@pynet-jnpr-srx1> show run|   i
                              ^
syntax error, expecting <command>.
pyclass@pynet-jnpr-srx1> show run|i   hostname
                              ^
syntax error, expecting <command>.



===========================================================
Executing command <sh run | i hostname> on device pynet-sw2
===========================================================


===========================================================
Executing command <sh run | i hostname> on device pynet-sw3
===========================================================


===========================================================
Executing command <sh run | i hostname> on device pynet-sw1
===========================================================


===========================================================
Executing command <sh run | i hostname> on device pynet-sw4
===========================================================
hostname pynet-sw2
hostname pynet-sw3
hostname pynet-sw1
hostname pynet-sw4
<Process(Process-4, stopped)>
<Process(Process-5, stopped)>
<Process(Process-6, stopped)>
<Process(Process-7, stopped)>
Multi Process Elapsed time: 0:00:16.031519
Single Threaded Time: 0:00:45.968365
Multi Threaded Time: 0:00:10.987360
(applied_python)[cdeluna@ip-172-30-0-7 week8]$ 


```