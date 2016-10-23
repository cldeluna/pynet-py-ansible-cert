#!/usr/bin/python -tt
# telnet-test.py
# Claudia
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "8/13/16  1:02 PM"
__copyright__ = "Copyright (c) 2015 Claudia de Luna"
__license__ = "Python"



import sys
import re
import os
import telnetlib
import time
import yaml
import socket




TELNET_PORT = 23
TELNET_TIMEOUT = 6

def login(tn,uname,upwd):
    # Read from connection object until you get "Username" prompt
    # Note, in my devince I have to send a LF before I get the Unsername prompt and  in that case I have to give it the full Username prompte vs "sername"
    output = tn.read_until("\nUsername: ")
    # send username
    tn.write(uname + "\n")
    if upwd:
        # If the password is defined, read until you get the "Password" prompt
        output += tn.read_until("Password: ")
        tn.write(upwd + "\n")
    return output

def sendcmd(tn, cmd):
    # strip off if any trailing spaces and LF/CR
    cmd = cmd.rstrip()
    tn.write(cmd + '\n')
    time.sleep(1)
    output  = tn.read_very_eager()
    return output

def telnet_connection(ip, port, timeout):
    try:
        tn = telnetlib.Telnet(ip, port, timeout)
        print("remote_conn: " + str(tn))
    except socket.timeout:
        sys.exit("Connection timed out!")
    return tn


def dump2yaml(filename, data):
    with open(filename, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=True)

def currwkdir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path


# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    Description
    :return:
    """

    ip = '10.1.10.100'
    uname = 'cisco'
    upwd = 'cisco'
    ymlfile = sys.argv[1]
    addshowcmd = sys.argv[2]
    out4 = ''

    tn = telnet_connection(ip, TELNET_PORT, TELNET_TIMEOUT)
    #print tn

    out = login(tn,uname,upwd)
    print("Output from login function: " + out)

    # output = tn.read_until("\nUsername: ")
    # print output
    # tn.write(uname + "\n")
    # if upwd:
    #     output = tn.read_until("Password: ")
    #     tn.write(upwd + "\n")
    # print output


    out1 = sendcmd(tn,'show ip int br')
    print out1

    out2 = sendcmd(tn,'term len 0')
    print out2

    out3 = sendcmd(tn,'show version')
    print out3

    if addshowcmd:
        out4 = sendcmd(tn,addshowcmd)

    print("\n\nOut1: " + out1)
    print("\n\nOut2: " + out2)
    print("\n\nOut3: " + out3)
    print("\n\nOut4: " + out4)

    tn.write("exit\n")

    #print tn.read_all()

    tn.close()

    dump2yaml(ymlfile,out1+out2+out3+out4)

    print(currwkdir())

# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '\nUsage: telnet-test.py.py <YAML Output file name> <additional show command to run>\nExample: python telnet-test.py "MyYamlFile.yml" "show inventory"\n\n'
        sys.exit()
    else:
        main()

