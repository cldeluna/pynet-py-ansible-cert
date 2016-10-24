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

    return data


def get_snmp3_info(dev_info):

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

    return snmp_dict


def print_dict(dict):

    for k,v in dict.items():
        print k + ": \t\t" + str(v)

    return None


def compare_ccmHistory(base, curr):

    # sysUpTime:              466541355
    # RunLastChanged:         465372359
    # RunLastSaved:           465372762
    # StartLastChanged:       63091204

    oid_list = ['sysUpTime', 'RunLastChanged', 'RunLastSaved', 'StartLastChanged']

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

        delta_dict.update({key : up_min})

    print delta_dict

    return delta_dict


def send_mail(recipient, subject, message, sender):
    '''
    Simple function to help simplify sending SMTP email

    Assumes a mailserver is available on localhost
    '''

    import smtplib
    from email.mime.text import MIMEText

    message = MIMEText(message)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    # Create SMTP connection object to localhost
    smtp_conn = smtplib.SMTP('dedrelay.secureserver.net')


    # Send the email
    smtp_conn.sendmail(sender, recipient, message.as_string())

    # Close SMTP connection

    smtp_conn.quit()

    return True


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
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
    # Take path argument and list all text files
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

    if len(device_info_payload) == 1:
        #print "proceed"

        if action.strip() == 'baseline':
            print "\nACTION IS BASELINE"
            baseline_info = get_snmp3_info(device_info_payload[0])

            timestr = time.strftime("%Y%m%d-%H%M%S")
            #print timestr

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

            newest = max(glob.iglob('*.[Jj]son'), key=os.path.getctime)
            #print newest

            baseline_data = load_json(newest)
            print "\nBASELINE DATA"
            print_dict(baseline_data)

            current_data = get_snmp3_info(device_info_payload[0])
            print "\nCURRENT DATA"
            print_dict(current_data)

            change_dict = compare_ccmHistory(baseline_data, current_data)

            print_dict(change_dict)

            # sysUpTime:              466541355
            # RunLastChanged:         465372359
            # RunLastSaved:           465372762
            # StartLastChanged:       63091204

            name = current_data['sysName']

            msg0 = "\nDevice " + name + " has baseline from " + str(change_dict['sysUpTime']) + " minutes ago at: " + time.ctime(baseline_data['time'])

            if change_dict['RunLastChanged'] > 0:
                msg1 = "\nRunning Configuration changed.  Delta Value: " + str(change_dict['RunLastChanged'])
                #print msg1
                #print "Running Configuration changed.  Delta Value: " + str(change_dict['RunLastChanged'])
                # print "++++++++++++"
                # print baseline_data['time']
                # print change_dict['sysUpTime']
                update_time_epoch = baseline_data['time'] + (60*change_dict['sysUpTime'])
                #print update_time_epoch

                update_time = time.ctime(update_time_epoch)
                #print update_time

                msg1 = "\nRunning Configuration changed at approximately" + update_time + ".  Delta Value: " + str(change_dict['RunLastChanged'])

                changed = True

            else:
                msg1 = "\nRunning Configuration has not changed."
                #print msg1

            if change_dict['RunLastSaved'] > 0:

                msg2 = "\nRunning Configuration was saved.  Delta Value: " + str(change_dict['RunLastSaved'])
                #print msg2
                changed = True
            else:
                msg2 =  "\nRunning Configuration has not been saved."
                #print msg2

            if change_dict['StartLastChanged'] > 0:
                msg3 =  "\nStartup Configuration changed. Delta Value: " + str(change_dict['StartLastChanged'])
                #print msg3
                changed = True
            else:
                msg3 =  "\nStarupConfiguration has not changed."


            print msg0
            print msg1
            print msg2
            print msg3

            msg = msg0 + msg1 + msg2 + msg3 + "\n\n" + sys.argv[0]

            #send_mail(recipient, subject, message, sender):

            # #sendemail(from_addr, to_addr_list, cc_addr_list,
            #               subject, message,
            #               login, password,
            #               smtpserver='smtp.gmail.com:587'):
            if changed:
                print "Send Email"
                #sendemail('delunac@gmail.com', 'cldeluna@yahoo.com', 'cldeluna@yahoo.com', "Router Configuration Changed: " + name, msg , '*****', '*****')

    else:
        print "Feature not implemented yet!"

# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '\nUsage: w3-01-FindCfgChg.py <JSON file with device information> <Action "baseline" | "check">\nExample: python w3-01-FindCfgChg.py python w3-01-FindCfgChg.py "device_info.json" "check"\n\n'
        sys.exit()
    else:
        main()

