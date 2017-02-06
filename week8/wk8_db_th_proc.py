#!/usr/bin/python -tt
# Project: PyNetACert
# Filename: wk8_db_th_proc.py
# claud
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2/5/2017"
__copyright__ = "Copyright (c) 2016 Claudia"
__license__ = "Python"

# For all exercises
import argparse
from net_system.models import NetworkDevice, Credentials
import django

# For exercises 4 onward
from netmiko import ConnectHandler
from datetime import datetime

# For exercise 6
import threading
import time

# For Exercise 7 and 8 (Queue)
from multiprocessing import Process, current_process, Queue


def show_command_queue(dev, cmd, q):

    output_dict = {}
    creds = dev.credentials
    dev_conn = ConnectHandler(device_type=dev.device_type, ip=dev.ip_address, username=creds.username,
                              password=creds.password, port=dev.port, verbose=False)

    msg = "Executing command <" + cmd + "> on device " + dev.device_name + "\n"
    output = ("=" * len(msg)) + "\n"
    output += msg
    output += ("=" * len(msg)) + "\n"

    output += dev_conn.send_command(cmd)
    output_dict[dev.device_name] = output
    q.put(output_dict)


def show_command_single(dev, cmd):

    creds = dev.credentials
    dev_conn = ConnectHandler(device_type=dev.device_type, ip=dev.ip_address, username=creds.username,
                              password=creds.password, port=dev.port)

    msg = "Executing command <" + cmd + "> on device " + dev.device_name

    print ("=" * len(msg)) + "\n"
    print msg
    print ("=" * len(msg)) + "\n"

    print dev_conn.send_command(cmd)


def list_db(msg):

    print "-" * len(msg)
    print msg
    print "-" * len(msg)
    print "\nNetwork Devices"
    net_devs = NetworkDevice.objects.all()
    net_creds = Credentials.objects.all()

    for dev in net_devs:
        print dev
    print "\nNetwork Device Credentials"
    for cred in net_creds:
        print cred
    print "-" * len(msg)
    print "\n"

def main():

    django.setup()

    if arguments.list:
        list_db("Database Object Listing from Command Line Option -l | --list")


    #3. Create two new test NetworkDevices in the database. Use both direct object creation
    # and the .get_or_create() method to create the devices.
    if arguments.adddev:
        list_db("Database Objects prior to ADD")
        check_first = True
        check_first_raw = raw_input("Check for device in DB prior to add (default = Y)? Y|N: ").strip()
        dev_name = raw_input("ADD Device Name: ").strip()
        dev_type = raw_input("Device Type cisco_ios | cisco_nxos etc.: ").strip()
        dev_ip = raw_input("Device IP: ").strip()
        dev_creds = raw_input("Device Credentials pyclass | admin1: ").strip()

        cred = Credentials.objects.get(username=dev_creds)

        if check_first_raw.upper() == "N":
            check_first = False

        if check_first:
            print "CHECKING DB prior to add!"
            my_new_dev = NetworkDevice.objects.get_or_create(
                device_name=dev_name,
                device_type=dev_type,
                ip_address=dev_ip,
                port=22,
                credentials=cred,
            )
            my_new_dev.save()

        else:
            print "NOT checking DB prior to add!"
            my_new_dev = NetworkDevice(
                device_name=dev_name,
                device_type=dev_type,
                ip_address=dev_ip,
                port=22,
                credentials=cred,
            )
            print type(my_new_dev)
            print dir(my_new_dev)
            my_new_dev.save()

        print my_new_dev

        list_db("Database Objects after ADD")


    #4. Remove the two objects created in the previous exercise from the database.
    if arguments.deldev:
        list_db("Database Objects prior to DELETE")

        dev_name = raw_input("DELETE Device Name: ").strip()

        dev2delete = NetworkDevice.objects.get(device_name=dev_name)

        dev2delete.delete()

        list_db("Database Objects after DELETE")


    #5. Use Netmiko to connect to each of the devices in the database. Execute 'show version' on each device.
    # Calculate the amount of time required to do this.
    if arguments.connect:

        start_time = datetime.now()
        list_db("Database Objects to Connect to.")
        show_cmd = "show version"
        show_cmd_raw = raw_input("Show command to execute on each device (default is show version): ").strip()

        if len(show_cmd_raw) > 1:
            show_cmd = show_cmd_raw

        devices = NetworkDevice.objects.all()

        for a_dev in devices:

            show_command_single(a_dev,show_cmd)

        elapsed_time = datetime.now() - start_time
        print "Elapsed time: {}".format(elapsed_time)


    #6. Use threads and Netmiko to execute 'show version' on each device in the database.
    # Calculate the amount of time required to do this.
    # What is the difference in time between executing 'show version' sequentially versus using threads?
    if arguments.threadconnect:

        start_time = datetime.now()
        list_db("Database Objects to Connect to.")
        show_cmd = "show version"
        show_cmd_raw = raw_input("Show command to execute on each device (default is show version): ").strip()

        if len(show_cmd_raw) > 1:
            show_cmd = show_cmd_raw

        devices = NetworkDevice.objects.all()

        for a_dev in devices:

            dev_thread = threading.Thread(target=show_command_single, args=(a_dev, show_cmd))
            dev_thread.start()

        main_thread = threading.currentThread()
        for a_thread in threading.enumerate():
            if a_thread != main_thread:
                print a_thread
                a_thread.join()

        elapsed_time = datetime.now() - start_time
        print "Elapsed time: {}".format(elapsed_time)

        single_thread_time = "0:00:45.968365"
        print "Single Threaded Time: " + single_thread_time


    #7. Use processes and Netmiko to execute 'show version' on each device in the database.
    # Calculate the amount of time required to do this.
    # What is the difference in time between executing 'show version' sequentially versus using processes?
    if arguments.procconnect or arguments.procconq:

        start_time = datetime.now()
        q = Queue(maxsize=20)
        list_db("Database Objects to Connect to.")
        show_cmd = "show version"
        show_cmd_raw = raw_input("Show command to execute on each device (default is show version): ").strip()

        if len(show_cmd_raw) > 1:
            show_cmd = show_cmd_raw

        devices = NetworkDevice.objects.all()

        procs = []
        for a_dev in devices:

            if arguments.procconq:
                dev_proc = Process(target=show_command_queue, args=(a_dev, show_cmd, q))
            else:
                dev_proc = Process(target=show_command_single, args=(a_dev, show_cmd))
            dev_proc.start()
            procs.append(dev_proc)

        for a_proc in procs:
            print a_proc
            a_proc.join()

        if arguments.procconq:
            while not q.empty():
                my_dict = q.get()
                for k,v in my_dict.iteritems():
                    print k
                    print v

        elapsed_time = datetime.now() - start_time
        print "Multi Process (with Queue) Elapsed time: {}".format(elapsed_time)

        single_thread_time = "0:00:45.968365"
        print "Single Threaded Time: " + single_thread_time

        multi_thread_time = "0:00:10.987360"
        print "Multi Threaded Time: " + multi_thread_time

# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="[PyNet Python + Ansible] - Class8 / Integrating to a Database and Concurrency",
                                     epilog="Usage: ' python wk8_db_th_proc.py' ")

    #parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    #parser.add_argument('--device', action='store_true', default=False, dest='display_device_value',
    #                    help='Set to True to display the device that is being worked on')


    parser.add_argument('-3', '--adddev', action='store_true', default=False, help='Week8 Ex3 add device to DB.')
    parser.add_argument('-4', '--deldev', action='store_true', default=False, help='Week8 Ex4 Remove device from DB.')
    parser.add_argument('-5', '--connect', action='store_true', default=False, help='Week8 Ex5 Connect to devices in DB and execute show command')
    parser.add_argument('-6', '--threadconnect', action='store_true', default=False, help='Week8 Ex6 Connect to devices in DB and execute show command using threads')
    parser.add_argument('-7', '--procconnect', action='store_true', default=False, help='Week8 Ex7 Connect to devices in DB and execute show command using processes.')
    parser.add_argument('-8', '--procconq', action='store_true', default=False, help='Week8 Ex8 Connect to devices in DB and execute show command using processes and queue.')

    parser.add_argument('-l', '--list', action='store_true', default=False, help='Week8 - List DB')

    arguments = parser.parse_args()

    main()


