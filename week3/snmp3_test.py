#!/usr/bin/python -tt
# snmp3_test
# Claudia
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "10/23/16  11:25 AM"
__copyright__ = "Copyright (c) 2015 Claudia de Luna"
__license__ = "Python"


#from __future__ import print_function
import sys
import snmp_helper



# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    Test SNMPv3 script utilizing Kirks snmp_helper module

    """

    ip = '10.1.10.100'
    a_user = 'cisco'
    auth_key = 'cisco123'
    encr_key = 'cisco123'
    snmp_user = (a_user, auth_key, encr_key)
    sw1 = (ip, 161)

    sysDescr = '1.3.6.1.2.1.1.1.0'
    sysObjectID = '1.3.6.1.2.1.1.2.0'
    sysUpTime = '1.3.6.1.2.1.1.3.0'
    sysContact = '1.3.6.1.2.1.1.4.0'
    sysNmae = '1.3.6.1.2.1.1.5.0'
    ifNumber = '1.3.6.1.2.1.2.1.0'


    # Uptime when running config last changed
    RunLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'

    # Uptime when running config last saved (note any 'write' constitutes a save)
    RunLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'

    # Uptime when startup config last saved
    StartLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

    ifAlias = '1.3.6.1.2.1.31.1.1.1.18.1'
    ifName = '1.3.6.1.2.1.31.1.1.1.1.1'

    snmp_data = snmp_helper.snmp_get_oid_v3(sw1, snmp_user, oid=ifName, auth_proto='sha', encrypt_proto='des')
    #print(snmp_data)

    # snmp_get_oid_v3(snmp_device, snmp_user, oid='.1.3.6.1.2.1.1.1.0', auth_proto='sha',
    #               encrypt_proto='aes128', display_errors=True):

    #snmp_extract(snmp_data):

    output = snmp_helper.snmp_extract(snmp_data)
    print output



# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 1:
        #print '\nUsage: snmp3_test.py \nExample: python snmp3_test.py\n\n'
        sys.exit()
    else:
        main()

