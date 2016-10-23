## PyNet Week 2 Exercises 

### Exercise 1 - Python Libraries

a. Verified that both modules were installed

b. Verified versions of both modules

```
>>> paramiko.__version_info__
(2, 0, 0)
>>> pysnmp.version
(4, 3, 2)
>>> dir(paramiko)
['AUTH_FAILED', 'AUTH_PARTIALLY_SUCCESSFUL', 'AUTH_SUCCESSFUL', 'Agent', 'AgentKey', 'AuthHandler', 'AuthenticationException', 'AutoAddPolicy', 'BadAuthenticationType', 'BadHostKeyException', 'BaseSFTP', 'BufferedFile', 'Channel', 'ChannelException', 'ChannelFile', 'DSSKey', 'ECDSAKey', 'GSSAuth', 'GSS_AUTH_AVAILABLE', 'HostKeys', 'InteractiveQuery', 'Message', 'MissingHostKeyPolicy', 'OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED', 'OPEN_FAILED_CONNECT_FAILED', 'OPEN_FAILED_RESOURCE_SHORTAGE', 'OPEN_FAILED_UNKNOWN_CHANNEL_TYPE', 'OPEN_SUCCEEDED', 'PKey', 'Packetizer', 'PasswordRequiredException', 'ProxyCommand', 'ProxyCommandFailure', 'RSAKey', 'RejectPolicy', 'SFTP', 'SFTPAttributes', 'SFTPClient', 'SFTPError', 'SFTPFile', 'SFTPHandle', 'SFTPServer', 'SFTPServerInterface', 'SFTP_BAD_MESSAGE', 'SFTP_CONNECTION_LOST', 'SFTP_EOF', 'SFTP_FAILURE', 'SFTP_NO_CONNECTION', 'SFTP_NO_SUCH_FILE', 'SFTP_OK', 'SFTP_OP_UNSUPPORTED', 'SFTP_PERMISSION_DENIED', 'SSHClient', 'SSHConfig', 'SSHException', 'SecurityOptions', 'ServerInterface', 'SubsystemHandler', 'Transport', 'WarningPolicy', '__all__', '__author__', '__builtins__', '__doc__', '__file__', '__license__', '__name__', '__package__', '__path__', '__version__', '__version_info__', '_version', 'agent', 'auth_handler', 'ber', 'buffered_pipe', 'channel', 'client', 'common', 'compress', 'config', 'dsskey', 'ecdsakey', 'file', 'hostkeys', 'io_sleep', 'kex_gex', 'kex_group1', 'kex_group14', 'kex_gss', 'message', 'packet', 'pipe', 'pkey', 'primes', 'proxy', 'py3compat', 'resource', 'rsakey', 'server', 'sftp', 'sftp_attr', 'sftp_client', 'sftp_file', 'sftp_handle', 'sftp_server', 'sftp_si', 'ssh_exception', 'ssh_gss', 'sys', 'transport', 'util']
>>> dir(pysnmp)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', '__version__', 'majorVersionId', 'version', 'x']

```
c. Import custom module from various locations on file system
- As expected, when the module "telnet_test" was located in the same directory as the script importing it, 
import was sucessful.
- When the module was in another directory I had to either set the PYTHONPATH env variable or use sys.path.append to add the location of the custom module to the python search scope before the modudle would import.
- When the module was located in the site-packages folder (root level) import was sucessful.
```
Claudia@Mac-mini:~/Dropbox/scripts/python/2016/PyNetA/week2$ python save2yaml.py 
Importing the telnet_test.py module in this script: save2yaml.py
/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packag
```

### Excercise 2 - telnetlib

The telnet_test.py script performs the following functions:
it establishes a telnet connection to a device (parameters hardcoded into script)
it sends 3 hardcoded commands plus one that can be provided via argument when the script is called
-- show ip in br
-- term len 0
-- show version
-- additional show command provided on command line during execution
it prints the output of each call
finally, it saves all the output into a yaml file whose name is defined as a command line argument and the prints the working directory (where the yaml file will be located)

The script has the following functions:
- login
- sendcmd
- telnet_connection
- dump2yaml (yes, should have used the one from last week...i know)
- currwkdir

### Exercise 3 - telnetlib (optional - challenge question)
Working in Progress

### Exercise 4 - SNMP Basics
a & b I'm not using the snmp_helper library

c. See snmp_test.py
Sample Output from snmp_test.py

```
Claudia@Mac-mini:~/Dropbox/scripts/python/2016/PyNetA/week2$ python snmp_test.py

Usage: snmp_test.py <YAML File to import with device information>
Example: python snmp_test.py dataFalse.yml


Claudia@Mac-mini:~/Dropbox/scripts/python/2016/PyNetA/week2$ python snmp_test.py dataFalse.yml
[{'ip': '10.1.10.100', 'commstr': 'cisco', 'snmp_port': '161'}, {'ip': '10.1.10.17', 'commstr': 'public', 'snmp_port': '161'}]
Number of devices to query: 2
Top level data structure from YAML File: <type 'list'>
########################################################

        Element level data structure from YAML File: <type 'dict'>
                OID for sysName: 1.3.6.1.2.1.1.5.0   arctic-sw01.uwaco.net

                Cisco Internetwork Operating System Software 
IOS (tm) C2940 Software (C2940-I6K2L2Q4-M), Version 12.1(22)EA11, RELEASE SOFTWARE (fc2)
Copyright (c) 1986-2008 by cisco Systems, Inc.
Compiled Tue 08-Jan-08 11:14 by amvarma

########################################################

        Element level data structure from YAML File: <type 'dict'>
                OID for sysName: 1.3.6.1.2.1.1.5.0   arctic-rtr01.uwaco.net

                Cisco IOS Software, 2800 Software (C2800NM-SPSERVICESK9-M), Version 12.4(20)T3, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2009 by Cisco Systems, Inc.
Compiled Tue 28-Apr-09 15:57 by prod_rel_team

Claudia@Mac-mini:~/Dropbox/scripts/python/2016/PyNetA/week2$ cat dataFalse.yml 
- {commstr: cisco, ip: 10.1.10.100, snmp_port: '161'}
- {commstr: public, ip: 10.1.10.17, snmp_port: '161'}

Claudia@Mac-mini:~/Dropbox/scripts/python/2016/PyNetA/week2$ 

```

