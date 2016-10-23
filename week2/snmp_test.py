#!/usr/bin/python -tt
# snmp_test.py
# Claudia
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "8/13/16  6:17 PM"
__copyright__ = "Copyright (c) 2015 Claudia de Luna"
__license__ = "Python"

import sys
import re
import os
from pysnmp.entity.rfc3413.oneliner import cmdgen
import time
import yaml

def readyml(file):

    with open(file, 'r') as stream:
        try:
            yml_data = yaml.load(stream)
            print yml_data
        except yaml.YAMLError as exc:
            print(exc)
            yml_data = exc

    return yml_data


def snmpget(oid, SNMP_HOST, SNMP_PORT, SNMP_COMMUNITY):
    from pysnmp.entity.rfc3413.oneliner import cmdgen

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                #print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                return val


# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    Description
    :return:
    """

    # commstr = 'cisco'
    # snmp_port = 161
    # ip = '10.1.10.100'

    oid_sysdesc = '1.3.6.1.2.1.1.1.0'
    oid_sysname = '1.3.6.1.2.1.1.5.0'

    # Read the device information to query from YAML file provided on command line
    data = readyml(sys.argv[1])

    print("Number of devices to query: " + str(len(data)))
    print("Top level data structure from YAML File: " + str(type(data)))


    for element in data:
        print("########################################################\n")
        print("\tElement level data structure from YAML File: " +  str(type(element)))

        answer5 = snmpget(oid_sysname, element['ip'], element['snmp_port'], element['commstr'])
        print("\t\tOID for sysName: " + oid_sysname + "   " + answer5 + "\n")

        answer1 = snmpget(oid_sysdesc, element['ip'], element['snmp_port'], element['commstr'])
        print("\t\t" + answer1 + "\n")
        #print("\t\tOID for sysDesc: " + oid_sysdesc + "   " + answer1 + "\n")




# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '\nUsage: snmp_test.py <YAML File to import with device information>\nExample: python snmp_test.py dataFalse.yml\n\n'
        sys.exit()
    else:
        main()

