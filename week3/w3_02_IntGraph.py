#!/usr/bin/python -tt
# w3-02-intgraph
# Claudia
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "10/24/16  6:23 AM"
__copyright__ = "Copyright (c) 2015 Claudia de Luna"
__license__ = "Python"

import sys
import re
import os
import time
import w3_01_FindConfChg
import pygal
import json


# - load_json(file)
# - get_snmp3_info(dev_info)
# - print_dict(dict)
# - compare_ccmHistory(oid_list,base, curr)
# - compare_iods(oid_list, base, curr)

def pygal_plot(dict_of_lists, title, x_labels,output_filename):

    # Function is passed a dictionary of lists which contains a key per line, and a value
    # that is a list of data for the line.

    # fa4_in_octets = [5269, 5011, 6705, 5987, 5011, 5071, 6451, 5011,
    #                                 5011, 6181, 5281, 5011]
    # fa4_out_octets =[5725, 5783, 7670, 6783, 5398, 5783, 9219, 3402,
    #                                 5783, 6953, 5668, 5783]
    #
    # fa4_in_packets = [24, 21, 40, 32, 21, 21, 49, 9, 21, 34, 24, 21]
    # fa4_out_packets = [24, 21, 40, 32, 21, 21, 49, 9, 21, 34, 24, 21]

    # Create a Chart of type Line
    line_chart = pygal.Line()

    # Title
    line_chart.title = title

    # X-axis labels (samples were every five minutes)
    line_chart.x_labels = x_labels

    # Add each one of the above lists into the graph as a line with corresponding label
    #
    for line, values in dict_of_lists.items():
        print line
        print values
        line_chart.add(line, values)

    # Create an output image file from this
    line_chart.render_to_file(output_filename)


def save2json(payload):

    # Establish the time in a string to append to the JSON file that wills ve the
    # data returned from get_snmp3_info
    timestr = time.strftime("%Y%m%d-%H%M%S")
    # print timestr

    # Build filename based on the name of the device, the fact that it is
    # generated as a bseline, and a timestamp
    filename = payload[0]['sysName'] + "-ChartData-" + timestr + ".json"

    with open(filename, 'w') as outfile:
        json.dump(payload, outfile)

    # print baseline_info
    msg = "\nBaseline Information for device " + payload[0]['sysName'] + " has been saved to file " + filename
    print msg


def get_list():
    print "temp"


# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    Description
    :return:
    """
    # JSON file with device login information
    device_info_file = sys.argv[1]
    # Interface Index Number
    int_index = sys.argv[2]
    # polling interval in seconds
    time_interval = float(sys.argv[3])
    # Maximum Monitor Time in seconds
    # One hour 3600 seconds
    max_monitor_interval = 3600
    DEBUG = True



    # Establish the time in a string to append to the JSON file that wills ve the
    # data returned from get_snmp3_info
    timestr = time.strftime("%Y%m%d-%H%M%S")
    #print timestr


    t = 0
    oid_list = ["ifDescr", "ifInOctets", "ifInUcastPkts", "ifOutOctets", "ifOutUcastPkts"]

    device_info_payload = w3_01_FindConfChg.load_json(device_info_file)

    list_of_all_gets = []

    inOct = []
    outOct = []


    while t <= max_monitor_interval:

        print "============= Data at: " + time.ctime()

        # Get the current data
        current_data = w3_01_FindConfChg.get_snmp3_info(device_info_payload[0])
        #w3_01_FindConfChg.print_dict(current_data)
        #print current_data
        time.sleep(time_interval)
        t = t + time_interval
        graph_dict = {}

        list_of_all_gets.append(current_data)

    # print list_of_all_gets
    # print len(list_of_all_gets)

    save2json(list_of_all_gets)

    # In minutes if time interval > 60
    if time_interval < 60.0:
        xlabels = range(0, int(max_monitor_interval + time_interval), int(time_interval))
    else:
        xlabels = range(0, int((max_monitor_interval + time_interval)/60), int(time_interval/60))


    #  Graph of input and output octets
    # "ifInOctets": "1.3.6.1.2.1.2.2.1.10.9",
    # "ifOutOctets": "1.3.6.1.2.1.2.2.1.16.9",


    graph_dict.clear()

    title = "In/Out Octets for " + list_of_all_gets[0]['sysName'] + " interface " + list_of_all_gets[0]['ifDescr']
    filename = "In-Out-Octets-" + list_of_all_gets[0]['sysName'] + "-intindx" + int_index + ".svg"

    for get in list_of_all_gets:
        for key, value in get.items():
            if key.strip() == 'ifInOctets':
                inOct.append(int(value))

    for get in list_of_all_gets:
        for key, value in get.items():
            if key.strip() == 'ifOutOctets':
                outOct.append(int(value))


    graph_dict['ifInOctets'] = inOct
    graph_dict['ifOutOctets'] = outOct


    if DEBUG:
        print xlabels
        print inOct
        print outOct
        print graph_dict
        print title
        print filename

    #pygal_plot(dict_of_lists, title, x_labels, output_filename)
    pygal_plot(graph_dict, title, xlabels, filename)

    #  Graph of input and output uncast packets
    # ifInUcastPkts
    # ifOutUcastPkts

    graph_dict.clear()

    title = "In/Out Packets for " + list_of_all_gets[0]['sysName'] + " interface " + list_of_all_gets[0]['ifDescr']
    filename = "In-Out-Packets-" + list_of_all_gets[0]['sysName'] + "-intindx" + int_index + ".svg"

    for get in list_of_all_gets:
        for key, value in get.items():
            if key.strip() == 'ifInUcastPkts':
                inOct.append(int(value))

    for get in list_of_all_gets:
        for key, value in get.items():
            if key.strip() == 'ifOutUcastPkts':
                outOct.append(int(value))

    graph_dict['ifInUcastPkts'] = inOct
    graph_dict['ifOutUcastPkts'] = outOct

    if DEBUG:
        print xlabels
        print inOct
        print outOct
        print graph_dict
        print title
        print filename

    # pygal_plot(dict_of_lists, title, x_labels, output_filename)
    pygal_plot(graph_dict, title, xlabels, filename)

# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print '\nUsage: w3-02-intgraph.py <JSON file with device information> <SNMP Interface Index Number> <time interval in seconds>\nExample: python w3-02-intgraph.py "device_info.json" "9" "300"\n\n'
        sys.exit()
    else:
        main()

