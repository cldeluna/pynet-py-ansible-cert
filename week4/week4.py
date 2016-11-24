
import paramiko
from getpass import getpass
import argparse
import time
import pexpect
from netmiko import ConnectHandler


def para_conn(ip, user, passwd, cmd, mode):

    # Mode
    # user_exec
    # priv_exec (enable)
    # config (config terminal)

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip, username=user, password=passwd, look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()

    #print "In para_conn function: " + str(remote_conn)

    if mode == 'user_exec':
        para_cmd_output = para_cmd(remote_conn, cmd)

    if mode == 'config':
        para_cmd_output = para_cmd_en(remote_conn, cmd)

   #print para_cmd_output

    return para_cmd_output


def para_cmd(remote_conn, cmd):

    out = ''
    outp = remote_conn.send('term len 0\n')
    time.sleep(2)
    outp = remote_conn.send(cmd)
    time.sleep(5)
    # print outp

    outp = remote_conn.recv(65535)
    #print outp
    #print remote_conn.recv_ready()

    #print "In para_cmd function: " + str(remote_conn)

    while remote_conn.recv_ready():
        outp = remote_conn.recv(65535)
        out = out + outp

    return outp



def para_cmd_en(remote_conn, cmd):

    out = ''
    outp = remote_conn.send('en\n')
    time.sleep(2)
    outp = remote_conn.send('config t\n')
    time.sleep(2)
    outp = remote_conn.send(cmd)
    time.sleep(5)
    #print outp

    outp = remote_conn.recv(65535)
    #print outp
    #print remote_conn.recv_ready()

    outp = remote_conn.send('end\n')
    time.sleep(2)

    outp = remote_conn.send('show run | i logging buff\n')
    time.sleep(2)
    #print outp
    outp = remote_conn.recv(65535)
    #print outp
    #print remote_conn.recv_ready()

    #print "In para_cmd function: " + str(remote_conn)

    return outp


def pexp_conn(ip, user, passwd, cmd, sshport, hostname):

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(user, ip, sshport))
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')

    ssh_conn.sendline(passwd)
    prompt = hostname.strip() + "#"
    ssh_conn.expect(prompt)

    ssh_conn.sendline(cmd)
    ssh_conn.expect(prompt)
    print ssh_conn.before
    print ssh_conn.after


    return ssh_conn.after



def pexp_conn_en(ip, user, passwd, cmd, port, hostname):

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(user, ip, port))
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')

    ssh_conn.sendline(passwd)
    prompt = hostname.strip() + "#"
    ssh_conn.expect(prompt)

    ssh_conn.sendline('config t')
    ssh_conn.expect("#")

    ssh_conn.sendline(cmd)
    ssh_conn.expect('#')
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.sendline('end')
    ssh_conn.expect(prompt)

    ssh_conn.sendline('show run | i logging')
    ssh_conn.expect(prompt)
    print ssh_conn.before
    print ssh_conn.after

    return ssh_conn.after


def netm_conn(dev_dict):
    netmiko_device_conn = ConnectHandler(**dev_dict)
    return netmiko_device_conn


def netm_cmd(conn_obj, cmd, configfile, mode):
    print conn_obj.find_prompt()
    status = ''
    if mode == 'config':
        output = conn_obj.config_mode()
        status = conn_obj.check_config_mode()

    elif mode == 'priv':
        status = conn_obj.send_command(cmd)

    elif mode == 'cmdfile':
        status = conn_obj.send_config_from_file(config_file=configfile)

    else:
        status = "Error"

    return status

def main():

    device = 'pynet-rtr2'
    #device = 'arctic-sw01'

    pynet_devices = {
        "pynet-rtr1": {
            "username": "pyclass",
            "snmp_port": "161",
            "ip": "184.105.247.70",
            "ssh_port": "22",
            "eapi_port": "",
            "hostname": "pynet-rtr1",
            "device_type": "cisco_ios",
            "password": "88newclass"
        },
        "pynet-rtr2": {
            "username": "pyclass",
            "snmp_port": "161",
            "ip": "184.105.247.71",
            "ssh_port": "22",
            "eapi_port": "",
            "hostname": "pynet-rtr2",
            "device_type": "cisco_ios",
            "password": "88newclass"
        },
        "arctic-sw01": {
            "username": "cisco",
            "snmp_port": "161",
            "ip": "10.1.10.100",
            "ssh_port": "22",
            "eapi_port": "",
            "hostname": "arctic-sw01",
            "device_type": "cisco_ios",
            "password": "cisco"
        }
    }

    print "############## Device ###############"
    print pynet_devices[device]['hostname']
    print pynet_devices[device]['ip']

    ip = pynet_devices[device]['ip']
    usernm = pynet_devices[device]['username']
    passwd = pynet_devices[device]['password']
    sshport = pynet_devices[device]['ssh_port']
    hostname = pynet_devices[device]['hostname']


    #1. Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2.
    if arguments.all or arguments.ex1:
        print "\nExecuting exercise 1 - Use Paramiko to retrieve the entire 'show version' output from device " + device + "."

        command = "show version\n"
        print "Sending command: " + command
        paramiko_connection = para_conn(ip, usernm, passwd, command, 'user_exec')

        print "In main after calling para_conn function: " + str(paramiko_connection)

    #2. Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.
    if arguments.all or arguments.ex2:
        print "\nExecuting exercise 2 - Use Paramiko to change the 'logging buffered <size>' configuration on " + device + "."

        command = "logging buffered 12000 debugging\n"
        print "Sending command: " + command
        paramiko_connection = para_conn(ip, usernm, passwd, command, 'config')

        print "In main after calling para_conn function: " + str(paramiko_connection)

    #3.Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2
    if arguments.all or arguments.ex3:
        print "\nExecuting exercise 3 - Use Pexpect to retrieve the output of 'show ip int brief' from " + device + "."

        command = "show ip int br\n"
        print "Sending command: " + command
        #pexp_conn(ip, user, passwd, cmd, port, hostname)
        pexpect_connection = pexp_conn(ip, usernm, passwd, command, sshport, hostname)

        print "In main after calling pexp_conn function: " + str(pexpect_connection)


    #4. Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2. Verify this change.
    if arguments.all or arguments.ex4:
        device = "pynet-rtr2"
        print "\nExecuting exercise 4 - Use PExpect to change the logging buffer size (logging buffered <size>) on " + device + " and verify."

        command = "logging buffered 14000 debugging\n"
        print "Sending command: " + command
        # pexp_conn(ip, user, passwd, cmd, port, hostname)
        pexpect_connection = pexp_conn_en(ip, usernm, passwd, command, sshport, hostname)

        print "In main after calling pexp_conn function: " + str(pexpect_connection)


    ## Netmiko Exercises

    netmiko_devices = {
        "pynet-rtr1": {
            "username": "pyclass",
            "ip": "184.105.247.70",
            "device_type": "cisco_ios",
            "password": "88newclass"
        },
        "pynet-rtr2": {
            "username": "pyclass",
            "ip": "184.105.247.71",
            "device_type": "cisco_ios",
            "password": "88newclass"
        },
        "arctic-sw01": {
            "username": "cisco",
            "ip": "10.1.10.100",
            "device_type": "cisco_ios",
            "password": "cisco"
        },
        "juniper-srx" : {
            "username": "pyclass",
            "ip": "184.105.247.76",
            "device_type": "juniper",
            "password": "88newclass",
            "secret": ''
        }
    }

    #5. Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state.
    if arguments.all or arguments.ex5:

        print "\nExecuting exercise 5 - Use Netmiko to enter into configuration mode on " + device + ". Also use Netmiko to verify your state."

        # Note: can't use pynet_devices dict as not in correct format (key/value) pairs
        # netm_conn(dev_dict)
        netmiko_connection = netm_conn(netmiko_devices[device])
        print "In main after calling netm_conn function: " + str(netmiko_connection)

        command = "config t"
        print "Sending command: " + command
        output = netm_cmd(netmiko_connection, command, '', 'config')
        if output:
            print "Device is in global configuration mode!"

    # 6. Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
    if arguments.all or arguments.ex6:

        #list_of_devices = ["arctic-sw01"]
        list_of_devices = ["pynet-rtr1", "pynet-rtr2", "juniper-srx"]
        print "\nExecuting exercise 6 - Use Netmiko to execute show arp on " + str(list_of_devices) + "."

        for dev in list_of_devices:
            netmiko_connection = netm_conn(netmiko_devices[dev])
            command = "show arp"
            print "Sending command: " + command
            output = netm_cmd(netmiko_connection, command, '', 'priv')
            print output

    #7. Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
    if arguments.all or arguments.ex7:

        print "\nExecuting exercise 7 - Use Netmiko to change the logging buffer size on " + device + "."
        netmiko_connection = netm_conn(netmiko_devices[device])

        command = "show run | inc logging buff"
        print "\nSending command: " + command
        output = netm_cmd(netmiko_connection, command, '', 'priv')
        print output

        command = "config t"
        print "\nSending command: " + command
        output = netm_cmd(netmiko_connection, command, '', 'config')

        if output:
            command = "logging buffered 13000 debugging"
            print "\nSending command: " + command
            output = netm_cmd(netmiko_connection, command, '', 'priv')

            command = "do show run | inc logging buff"
            print "\nSending command: " + command
            output = netm_cmd(netmiko_connection, command, '', 'priv')
            print output

    #8. Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable console logging
    # (no logging console) from a file on both pynet-rtr1 and pynet-rtr2 (see 'Errata and Other Info, item #4).
    if arguments.all or arguments.ex8:

        list_of_devices = ["pynet-rtr1", "pynet-rtr2"]
        #list_of_devices = ["arctic-sw01"]
        configfile = 'config_file.txt'

        print "\nExecuting exercise 8 - Use Netmiko to change the configuration on " + str(list_of_devices) + " using a file."

        for dev in list_of_devices:

            netmiko_connection = netm_conn(netmiko_devices[dev])

            command = "show run | inc logging buff"
            print "\nSending command: " + command
            output = netm_cmd(netmiko_connection, command, '', 'priv')
            print output

            command = "config t"
            print "\nSending command: " + command
            output = netm_cmd(netmiko_connection, command, '', 'config')

            if output:
                print "\nSending commands from file: " + configfile
                output = netm_cmd(netmiko_connection, command, configfile, 'cmdfile')

                command = "show run | inc logging"
                print "\nSending command: " + command
                output = netm_cmd(netmiko_connection, command, '', 'priv')
                print output


# Standard call to the main() function.
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="PyNet Python + Ansible Course - Week 4 Excercises",
                                     epilog="Usage: 'python week4.py  -a' to execute all exercises, 'python week4.py -1' to execute exercise 1 ")

    #parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',default=False)
    parser.add_argument('-1', '--ex1', help='Execute Exercise 1', action='store_true',default=False)
    parser.add_argument('-2', '--ex2', help='Execute Exercise 2', action='store_true',default=False)
    parser.add_argument('-3', '--ex3', help='Execute Exercise 3', action='store_true',default=False)
    parser.add_argument('-4', '--ex4', help='Execute Exercise 4', action='store_true',default=False)
    parser.add_argument('-5', '--ex5', help='Execute Exercise 5', action='store_true',default=False)
    parser.add_argument('-6', '--ex6', help='Execute Exercise 6', action='store_true',default=False)
    parser.add_argument('-7', '--ex7', help='Execute Exercise 7', action='store_true',default=False)
    parser.add_argument('-8', '--ex8', help='Execute Exercise 8', action='store_true',default=False)

    arguments = parser.parse_args()
    main()