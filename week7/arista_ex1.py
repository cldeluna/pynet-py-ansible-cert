#!/usr/bin/python -tt
# Project Name: PyNetA
# Project File: arista_ex1
# User: claud
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "9 / 19 / 2016 6:14PM"
__copyright__ = "Copyright (c) 2016 Claudia de Luna"
__license__ = "Python"

import sys
import re
import os
import pyeapi
from pprint import pprint as pp


# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    Use Arista's eAPI to obtain 'show interfaces' from the switch.  Parse the 'show
    interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of
    the interfaces on the switch.  Accomplish this using Arista's pyeapi library.
    :return:
    """

    sw_node = sys.argv[1]
    print("\n****** Device is: " + sw_node + "******\n")

    node = pyeapi.connect_to(sw_node)

    #pp(node.enable('show version'))

    sh_int = node.enable('show interfaces')

    #pp(sh_int)
    #print type(sh_int)
    #print len(sh_int)
    #print "****************"

    sh_int_dict = sh_int[0]
    #print type(sh_int_dict)
    #print len(sh_int_dict)
    #print "----------------"

    #pp(sh_int_dict)

    sh_int_dict_keys = sh_int_dict.keys()

    #print sh_int_dict_keys

    sh_int_result = sh_int_dict['result']

    #print type(sh_int_result)
    #print len(sh_int_result)
    #print sh_int_result.keys()
    #pp(sh_int_result)

    sh_int_ints = sh_int_result['interfaces']
    #print type(sh_int_ints)
    #print sh_int_ints.keys()

    int_keys = sh_int_ints.keys()
    #print int_keys

    for key in int_keys:
        #print "++++++++++++++++++++"
        #print sh_int_ints[key]
        #print type(sh_int_ints[key])
        #print "+++++++----++++++++++"
        # Ethernet X
        print("==== " + str(sh_int_ints[key]['name'])+ " ===")
        #print sh_int_ints[key]['interfaceCounters']['inputErrorsDetail']
        #pp(sh_int_ints[key]['interfaceCounters']['inOctets'])
        #pp(sh_int_ints[key]['interfaceStatistics'])
        #print "--------------------"
        #print sh_int_ints[key].keys()
        #print sh_int_ints[key]['inOctets']
        #print sh_int_ints[key]['outOctets']

        print("=========================")
        print("inOctets: " + str(sh_int_ints[key]['interfaceCounters']['inOctets']))
        print("outOctets: " + str(sh_int_ints[key]['interfaceCounters']['outOctets']))
        print("=========================")

# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '\nUsage: arista_ex1.py <what are the argumentsr>\nExample: python arista_ex1.py "arguments"\n\n'
        sys.exit()
    else:
        main()

