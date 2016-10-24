#!/usr/bin/python -tt
# w3-01-FindCfgChg
# Claudia
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "10/23/16  6:12 AM"
__copyright__ = "Copyright (c) 2015 Claudia de Luna"
__license__ = "Python"

import sys
import os
import glob
import json
import snmp_helper
import time
import smtplib



def load_json(file):

    # Load the device or other information from the specified JSON file provided as the first argument to the script
    # Sample Format:
    # [{"ip":"10.1.10.100","a_user":"cisco","auth_key":"cisco123","encr_key":"cisco123","snmp_port":161}]
    # Data structure is a list of dictionaries so that multiple devices can be provided (future)

    with open(file) as json_data:
        data = json.load(json_data)
        #print(data)

    # Return list of dictionaries
    return data


def get_snmp3_info(dev_info):

    # Using the device information pulled out of a JSON file
    # and using the OIDs from JSON file oids.json
    # Use SNMPv3 to obtain the values of those oids and store them in a dictionary
    # whose keys are the oid name (keys from oids.json file)

    snmp_dict = {}

    #print dev_info
    #print type(dev_info)

    oids = load_json('oids.json')

    #print oids
    #print type(oids)
    #print '*' * 40

    ip = dev_info['ip']
    #print ip
    dev = [dev_info['ip'], dev_info['snmp_port']]
    #print dev
    user = [dev_info['a_user'], dev_info['auth_key'], dev_info['encr_key']]


    for o in oids.keys():
        snmp_data = snmp_helper.snmp_get_oid_v3(dev, user, oid=oids[o], auth_proto='sha', encrypt_proto='des')
        #print(snmp_data)

    # snmp_get_oid_v3(snmp_device, snmp_user, oid='.1.3.6.1.2.1.1.1.0', auth_proto='sha',
    #               encrypt_proto='aes128', display_errors=True):


        output = snmp_helper.snmp_extract(snmp_data)
        #print output

        snmp_dict[o] = output

    snmp_dict['time'] = time.time()
    #print snmp_dict

    # Return dictionary of key:value pairs
    return snmp_dict


def print_dict(dict):

    # Generic Print dictionary function
    for k,v in dict.items():
        print k + ": \t\t" + str(v)

    return None


def compare_ccmHistory(oid_list, base, curr):

    # This function takes in a list of oids, a baseline dictionary of oid values
    # and a current dictionary of oid values and performs a comparison of each value
    # it places the delta minutes (current - baseline) in a dictionary and returns
    # this "delta" dictionary
    # Note: This should be more generic so you have the delta of whaever you send

    # sysUpTime:              466541355
    # RunLastChanged:         465372359
    # RunLastSaved:           465372762
    # StartLastChanged:       63091204

    # Now this is passed to the function so that it can be used in the future for
    # for other comparisons
    #oid_list = ['sysUpTime', 'RunLastChanged', 'RunLastSaved', 'StartLastChanged']

    delta_dict = {}

    #print len(oid_list)

    for key in oid_list:

        #print "*************"
        #print key

        delta = int(curr[key]) - int(base[key])
        up_sec = delta/100
        up_min = up_sec/60

        # print "=========" + item + "========="
        # print delta
        # print up_sec
        # print up_min

        delta_dict.update({key: up_min})

    #print delta_dict

    return delta_dict


def compare_iods(oid_list, base, curr):

    # This function takes in a list of oids, a baseline dictionary of oid values
    # and a current dictionary of oid values and performs a comparison of each value
    # it places the delta minutes (current - baseline) in a dictionary and returns
    # this "delta" dictionary
    # Note: This should be more generic so you have the delta of whaever you send

    # Now this is passed to the function so that it can be used in the future for
    # for other comparisons
    #oid_list = ['sysUpTime', 'RunLastChanged', 'RunLastSaved', 'StartLastChanged']

    delta_dict = {}

    #print len(oid_list)

    # The items in the oid list will become keys in the returned dictionary
    for key in oid_list:

        #print "*************"
        #print key

        # This assumes that values increment up
        delta = int(curr[key]) - int(base[key])

        # print "=========" + item + "========="
        # print delta

        delta_dict.update({key: delta})

    #print delta_dict

    return delta_dict


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):

    # Script directly from Google to use Gmail
    # Note: "out of the box" this does not work because the SMTO server rejects the login
    # attemps as insecure.
    # You need to Turn ON "Access for less secur apps" which is probably not a good thing
    # to do in general.


    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems


# Provided main() calls the above functions
def main():
    """
    Description
    :return:
    """

    device_info_file = sys.argv[1]
    action = sys.argv[2]


    device_info_payload = load_json(device_info_file)
    #print device_info_payload
    #print len(device_info_payload)
    #print type(device_info_payload)

    # Current script only processes one device
    if len(device_info_payload) == 1:

        #print "proceed"

        if action.strip() == 'baseline':
            print "\nACTION IS BASELINE"
            baseline_info = get_snmp3_info(device_info_payload[0])

            # Establish the time in a string to append to the JSON file that wills ve the
            # data returned from get_snmp3_info
            timestr = time.strftime("%Y%m%d-%H%M%S")
            #print timestr

            # Build filename based on the name of the device, the fact that it is
            # generated as a bseline, and a timestamp
            filename = baseline_info['sysName'] + "-baseline-" + timestr + ".json"

            with open(filename, 'w') as outfile:
                json.dump(baseline_info, outfile)

            #print baseline_info
            msg = "\nBaseline Information for device " + baseline_info['sysName'] + " has been saved to file " + filename
            print msg


        else:
            print "\nACTION IS CHECK"

            msg0 = ''
            msg1 = ''
            msg2 = ''
            msg3 = ''
            changed = False

            # Find the most recent baseline file to use for comparison
            # Note: This needs some work..it should only look for files with the
            # workd baseline and a timestamp in them.  Should build RegEx for this
            newest = max(glob.iglob('*.[Jj]son'), key=os.path.getctime)
            #print newest

            # Load the baseline data
            baseline_data = load_json(newest)
            print "\nBASELINE DATA"
            print_dict(baseline_data)

            # Get the current data
            current_data = get_snmp3_info(device_info_payload[0])
            print "\nCURRENT DATA"
            print_dict(current_data)

            # Compare the OIDs send in the variable oid_list
            oid_list = ['sysUpTime', 'RunLastChanged', 'RunLastSaved', 'StartLastChanged']
            change_dict = compare_ccmHistory(oid_list, baseline_data, current_data)

            print_dict(change_dict)

            name = current_data['sysName']

            msg0 = "\nDevice " + name + " has baseline from " + str(change_dict['sysUpTime']) + " minutes ago at: " + time.ctime(baseline_data['time'])


            # Logic for determining change
            # If the change dict values are 0, there has been no change.
            # If the change dict values are >0, there has been a change to the config
            # Each possible type of change is checked and the boolean "changed" is ste to True in each check
            # so we know if we need to email
            if change_dict['RunLastChanged'] > 0:
                msg1 = "\nRunning Configuration changed.  Delta Value: " + str(change_dict['RunLastChanged'])
                #print msg1
                # print "++++++++++++"
                # print baseline_data['time']
                # print change_dict['sysUpTime']
                # Add the sysUptime delta to the time from the baseline to get approx time of change
                update_time_epoch = baseline_data['time'] + (60*change_dict['sysUpTime'])
                #print update_time_epoch

                # Convert epoch time to human readable time
                update_time = time.ctime(update_time_epoch)
                #print update_time

                msg1 = "\nRunning Configuration changed at approximately " + update_time + ".  Delta Value: " + str(change_dict['RunLastChanged'])
                changed = True

            else:
                msg1 = "\nRunning Configuration has not changed."


            if change_dict['RunLastSaved'] > 0:

                msg2 = "\nRunning Configuration was saved.  Delta Value: " + str(change_dict['RunLastSaved'])
                changed = True

            else:
                msg2 =  "\nRunning Configuration has not been saved."


            if change_dict['StartLastChanged'] > 0:

                msg3 =  "\nStartup Configuration changed. Delta Value: " + str(change_dict['StartLastChanged'])
                changed = True

            else:
                msg3 =  "\nStarupConfiguration has not changed."


            # This is clumsy
            print msg0
            print msg1
            print msg2
            print msg3
            print "\n"

            # Concatenate the messages into one variable to pass in the sendemail function
            msg = msg0 + msg1 + msg2 + msg3 + "\n\n" + sys.argv[0]

            # If thee comparison determined that the configuration changed send email
            if changed:
                print "Send Email"
                #sendemail('delunac@gmail.com', 'cldeluna@yahoo.com', 'cldeluna@yahoo.com', "Router Configuration Changed: " + name, msg , '*****', '*****')

    else:
        # Processing multiple devices not implemented yet
        print "Feature not implemented yet!"

# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '\nUsage: w3-01-FindConfChg.py <JSON file with device information> <Action "baseline" | "check">\nExample:  python w3-01-FindConfChg.py "device_info.json" "check"\n\n'
        sys.exit()
    else:
        main()

