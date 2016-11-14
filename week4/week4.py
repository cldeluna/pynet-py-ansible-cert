
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


def pexp_conn(ip, user, passwd, cmd, port, hostname):

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(user, ip, port))
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
    print dev_dict
    netmiko_device_conn = ConnectHandler(**dev_dict)
    print netmiko_device_conn

    return netmiko_device_conn


def main():

    device = 'pynet-rtr2'
    #device = 'arctic-sw01'

    pynet_devices = {
        "pynet-rtr1": {
            "username": "pyclass",
            "": "",
            "snmp_port": "161",
            "ip_addr": "184.105.247.70",
            "ssh_port": "22",
            "eapi_port": "",
            "hostname": "pynet-rtr1",
            "device_type": "cisco_ios",
            "password": "88newclass"
        },
        "pynet-rtr2": {
            "username": "pyclass",
            "": "",
            "snmp_port": "161",
            "ip_addr": "184.105.247.71",
            "ssh_port": "22",
            "eapi_port": "",
            "hostname": "pynet-rtr2",
            "device_type": "cisco_ios",
            "password": "88newclass"
        },
        "arctic-sw01": {
            "username": "cisco",
            "": "",
            "snmp_port": "161",
            "ip_addr": "10.1.10.100",
            "ssh_port": "22",
            "eapi_port": "",
            "hostname": "arctic-sw01",
            "device_type": "cisco_ios",
            "password": "cisco"
        }
    }

    print "############## Device ###############"
    print pynet_devices[device]['hostname']
    print pynet_devices[device]['ip_addr']

    ip = pynet_devices[device]['ip_addr']
    usernm = pynet_devices[device]['username']
    passwd = pynet_devices[device]['password']
    sshport = pynet_devices[device]['ssh_port']
    hostname = pynet_devices[device]['hostname']


    #1. Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2.
    if arguments.all or arguments.ex1:
        print "\nExecuting exercise 1 - Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2."

        command = "show version\n"
        print "Sending command: " + command
        paramiko_connection = para_conn(ip, usernm, passwd, command, 'user_exec')

        print "In main after calling para_conn function: " + str(paramiko_connection)

    #2. Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.
    if arguments.all or arguments.ex2:
        print "\nExecuting exercise 2 - Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2."

        command = "logging buffered 12000 debugging\n"
        print "Sending command: " + command
        paramiko_connection = para_conn(ip, usernm, passwd, command, 'config')

        print "In main after calling para_conn function: " + str(paramiko_connection)

    #3.Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2
    if arguments.all or arguments.ex3:
        print "\nExecuting exercise 3 - Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2."

        command = "show ip int br\n"
        print "Sending command: " + command
        #pexp_conn(ip, user, passwd, cmd, port, hostname)
        pexpect_connection = pexp_conn(ip, usernm, passwd, command, sshport, hostname)

        print "In main after calling pexp_conn function: " + str(pexpect_connection)


    #4. Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2. Verify this change.
    if arguments.all or arguments.ex4:
        print "\nExecuting exercise 4 - Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2 and verify."

        command = "logging buffered 14000 debugging\n"
        print "Sending command: " + command
        # pexp_conn(ip, user, passwd, cmd, port, hostname)
        pexpect_connection = pexp_conn_en(ip, usernm, passwd, command, sshport, hostname)

        print "In main after calling pexp_conn function: " + str(pexpect_connection)


    #5. Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state.
    if arguments.all or arguments.ex5:
        print "\nExecuting exercise 5 - Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state."

        command = "logging buffered 14000 debugging\n"
        print "Sending command: " + command
        # netm_conn(dev_dict)
        netmiko_connection = netm_conn(pynet_devices[device])

        print "In main after calling pexp_conn function: " + str(pexpect_connection)




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

    arguments = parser.parse_args()
    main()