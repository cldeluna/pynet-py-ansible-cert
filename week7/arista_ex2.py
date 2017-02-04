#!/usr/bin/python -tt
# Project Name: PyNetA
# Project File: arista_ex2.py
# User: claud
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "9 / 20 / 2016 9:43 AM"
__copyright__ = "Copyright (c) 2016 Claudia de Luna"
__license__ = "Python"

import sys
import re
import os
import pyeapi
from pprint import pprint as pp
import argparse

def check_vlan(vlan_id, device):
    #print("From check_vlan function - vland_id: " + vlan_id)
    #print("From check_vlan function - device: " + str(device))

    sh_vlan_list = device.enable('show vlan')
    sh_vlan_dict = sh_vlan_list[0]

    sh_vlan_result = sh_vlan_dict['result']
    vlan_dict = sh_vlan_result['vlans']
    vlan_list = vlan_dict.keys()
    #print("vlan list in check vlan function: " + str(vlan_list))

    if vlan_id in vlan_list:
        found = True
    else:
        found = False

    return found



# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    Using Arista's pyeapi, create a script that allows you to add a VLAN (both the VLAN ID and the VLAN name).
    Your script should first check that the VLAN ID is available and only add the VLAN if it doesn't already exist.
    Use VLAN IDs between 100 and 999.  You should be able to call the script from the command line as follows:
       python eapi_vlan.py --name blue 100     # add VLAN100, name blue
    If you call the script with the --remove option, the VLAN will be removed.
       python eapi_vlan.py --remove 100          # remove VLAN100
    Once again only remove the VLAN if it exists on the switch.

    :return:
    """

    device_name = "pynet-sw2"
    dev_conn = pyeapi.connect_to(device_name)



    # Process option to add a vlan including name
    if results.name_num:
        add_vlan = results.name_num.split('_')
        add_vlan_name = add_vlan[0]
        add_vlan_num = add_vlan[1]
        vlan_found = check_vlan(add_vlan_num, dev_conn)


        if vlan_found:
            print("Vlan " + add_vlan_num + " is ALREADY configured on device " + device_name + " and so no action is required.")
        else:
            cmd1 = "vlan " + add_vlan_num
            cmd2 = "name " + add_vlan_name
            cmds = [cmd1, cmd2]
            config_add_vlan = dev_conn.config(cmds)
            check_add = check_vlan(add_vlan_num,dev_conn)
            if check_add:
                print("Vlan " + add_vlan_num + " has been added to device " + device_name + "and verified.")
            else:
                print("ERROR in adding vlan.")

    # Process option to remove
    if results.rem_vlan_num:
        rem_vlan = results.rem_vlan_num
        vlan_found = check_vlan(rem_vlan, dev_conn)
        # print("Vlan found: " + str(vlan_found))

        if vlan_found:
            cmd1 = " no vlan " + rem_vlan
            cmds = [cmd1]
            config_rem_vlan = dev_conn.config(cmds)
            check_add = check_vlan(rem_vlan, dev_conn)
            if check_add:
                print("ERROR in REMOVING vlan.")
            else:
                print("Vlan " + rem_vlan + " has been removed from device " + device_name + "and verified.")
        else:
            print("Vlan " + rem_vlan + " is NOT configured on device " + device_name + " and so no action is required.")



    # Process option to check if a vlan exists
    if results.check_vlan_num:
        check = check_vlan(results.check_vlan_num, dev_conn)

        if check:
            print("Vlan " + results.check_vlan_num + " is configured on device " + device_name)
        else:
            print("Vlan " + results.check_vlan_num + " is NOT configured on device " + device_name)

    # Process option to display device
    if results.display_device_value:
        print("The currently configured device is " + device_name +".")


# Standard call to the main() function.
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--name', action='store', dest='name_num',
                        help='Provide the name and the number of the Vlan to add if it does not exist usint the format VLANNAME_VLANNUMBER')

    parser.add_argument('--remove', action='store', dest='rem_vlan_num',
                        help='Store the number of the Vlan to remove if it exists')

    parser.add_argument('--verify', action='store', dest='check_vlan_num',
                        help='Store the number of the Vlan to check')

    parser.add_argument('--device', action='store_true', default=False, dest='display_device_value',
                        help='Set to True to display the device that is being worked on')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    results = parser.parse_args()


    main()

