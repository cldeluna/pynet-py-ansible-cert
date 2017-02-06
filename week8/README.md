
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

3. Create two new test NetworkDevices in the database. Use both direct object creation and the .get_or_create() method to create the devices.


