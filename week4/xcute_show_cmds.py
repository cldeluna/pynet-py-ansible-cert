

import argparse
import time
from netmiko import ConnectHandler
import json


def pluck_payload(json_data, key):
    for jlist in json_data:
        if key in jlist.keys():
            data = jlist[key]
            # print list['vlan']
    return data



def netm_conn(type, host, uname, pwd):
    #netmiko_device_conn = ConnectHandler(**dev_dict)
    #device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    netmiko_device_conn = ConnectHandler(device_type=type, ip=host, username=uname, password=pwd)
    time.sleep(10)
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


    # set variable filename to the json file passed as the first argument
    filename = arguments.payload_file

    start_time = time.clock()

    # # Create a Log file
    # filename_base = filename.split(".")[0]
    # timestr = time.strftime("%Y%m%d-%H%M%S")
    # log_filename = filename_base + "-" + action_text.upper() + "-" + timestr + ".log"
    # log_file = open(log_filename, 'w')

    ##### LOAD DATA #####

    try:
        with open(filename) as json_data:
            json_payload = json.load(json_data)
        #log_file.write("\nPayload used in this script from file: " + filename + "\n\n")
    except IOError:
        print "There was a problem opening the Payload file " + filename + "!"
        #log_file.write("\nThere was a problem opening the Payload file: " + filename + "\n\n")
        sys.exit('Aborting program Execution')



    # print json.dumps(json_payload, indent = 4)
    # print type(json_payload)
    # print len(json_payload)

    # raw_input("Press Enter to continue...")

    prov_net_devices = {
        "router": {
            "username": "admin",
            "ip": "192.0.2.1",
            "device_type": "cisco_ios",
            "password": "AutoM3"
        },
        "switch": {
            "username": "admin",
            "ip": "192.0.2.5",
            "device_type": "cisco_ios",
            "password": "AutoM3"
        }
    }

    ## Netmiko Exercises


    #5. Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state.
    if arguments.all or arguments.ex1:

        data = pluck_payload(json_payload, 'ztp_devices')

        print data

        print "\nExecuting exercise 5 - Use Netmiko to enter into configuration mode on router."

        #netmiko_switch_conn = netm_conn(prov_net_devices['switch'])
        print "*****"
        print prov_net_devices['switch']
        platform = 'cisco_ios'
        host = '192.0.2.1'
        username = 'admin'
        password = 'AutoM3'
        netmiko_switch_conn = netm_conn(platform, host, username, password)

        for line in data:
            # netm_conn(dev_dict)
            netmiko_router_conn = netm_conn(prov_net_devices['router'])

            print netmiko_router_conn

            command = "config t"
            print "Sending command: " + command
            output = netm_cmd(netmiko_router_conn, command, '', 'config')
            if output:
                print "Device is in global configuration mode!"

                command = "int g0/1." + line['vlan']
                print "\nSending command: " + command
                output = netm_cmd(netmiko_router_conn, command, '', 'priv')

                command = "encapsulation dot1Q " + line['vlan']
                print "\nSending command: " + command
                output = netm_cmd(netmiko_router_conn, command, '', 'priv')
                print output

                command = "ip address " + line['mgmt_net'] +" " + line['mgmt_mask']
                print "\nSending command: " + command
                output = netm_cmd(netmiko_router_conn, command, '', 'priv')
                print output

    #
    # # 6. Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
    # if arguments.all or arguments.ex6:
    #
    #     #list_of_devices = ["arctic-sw01"]
    #     list_of_devices = ["pynet-rtr1", "pynet-rtr2", "juniper-srx"]
    #     print "\nExecuting exercise 6 - Use Netmiko to execute show arp on " + str(list_of_devices) + "."
    #
    #     for dev in list_of_devices:
    #         netmiko_connection = netm_conn(prov_net_devices[dev])
    #         command = "show arp"
    #         print "Sending command: " + command
    #         output = netm_cmd(netmiko_connection, command, '', 'priv')
    #         print output
    #
    # #7. Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
    # if arguments.all or arguments.ex7:
    #
    #     print "\nExecuting exercise 7 - Use Netmiko to change the logging buffer size on " + device + "."
    #     netmiko_connection = netm_conn(prov_net_devices[device])
    #
    #     command = "show run | inc logging buff"
    #     print "\nSending command: " + command
    #     output = netm_cmd(netmiko_connection, command, '', 'priv')
    #     print output
    #
    #     command = "config t"
    #     print "\nSending command: " + command
    #     output = netm_cmd(netmiko_connection, command, '', 'config')
    #
    #     if output:
    #         command = "logging buffered 13000 debugging"
    #         print "\nSending command: " + command
    #         output = netm_cmd(netmiko_connection, command, '', 'priv')
    #
    #         command = "do show run | inc logging buff"
    #         print "\nSending command: " + command
    #         output = netm_cmd(netmiko_connection, command, '', 'priv')
    #         print output
    #
    # #8. Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable console logging
    # # (no logging console) from a file on both pynet-rtr1 and pynet-rtr2 (see 'Errata and Other Info, item #4).
    # if arguments.all or arguments.ex8:
    #
    #     list_of_devices = ["pynet-rtr1", "pynet-rtr2"]
    #     #list_of_devices = ["arctic-sw01"]
    #     configfile = 'config_file.txt'
    #
    #     print "\nExecuting exercise 8 - Use Netmiko to change the configuration on " + str(list_of_devices) + " using a file."
    #
    #     for dev in list_of_devices:
    #
    #         netmiko_connection = netm_conn(prov_net_devices[dev])
    #
    #         command = "show run | inc logging buff"
    #         print "\nSending command: " + command
    #         output = netm_cmd(netmiko_connection, command, '', 'priv')
    #         print output
    #
    #         command = "config t"
    #         print "\nSending command: " + command
    #         output = netm_cmd(netmiko_connection, command, '', 'config')
    #
    #         if output:
    #             print "\nSending commands from file: " + configfile
    #             output = netm_cmd(netmiko_connection, command, configfile, 'cmdfile')
    #
    #             command = "show run | inc logging"
    #             print "\nSending command: " + command
    #             output = netm_cmd(netmiko_connection, command, '', 'priv')
    #             print output


# Standard call to the main() function.
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Configure Client Envoronment and Execute Show Commands",
                                     epilog="Usage: 'python ecute_show_cmds.py  -a' to execute all exercises, 'python week4.py -1' to execute exercise 1 ")

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument('payload_file', help='Name of the payload file to use in this script.')
    parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',
                        default=False)
    parser.add_argument('-1', '--ex1', help='Execute Exercise 1', action='store_true', default=False)

    arguments = parser.parse_args()
    main()
