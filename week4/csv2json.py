#!/usr/bin/python -tt
# csv2json.py
# Claudia
# ACI_Configuration
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = "Revision: 1.0 $"
__date__ = "10/1/2016-5:43 PM"
__copyright__ = "Copyright (c) 2015 Claudia de Luna"
__license__ = "Python"

import sys
import re
import os
import csv
import json
import argparse



def debug_print_var(name,value):
    print("DEBUG==>  Variable: " + name + "\tValue = " + value )


# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    This script takes a CSV dump of a JSON OBJECTS tab in the ACI Object Naming Workbook and
    converts it to a json file that can be used by the aci_fabric_xxx scripts.

    """

    script = sys.argv[0]
    filename = arguments.csv_file

    top_level_list = []
    top_level_dict = {}
    temp_dict = {}
    interim_dict = {}
    temp_list = []
    after_start = False
    keys = []


    try:

        with open(filename) as csv_file:

            print("Converting CSV file " + filename + " to JSON.")

            reader = csv.reader(csv_file)
            for row in reader:
                # If not an empty row
                if row:
                    if row[0] and not re.search('^#',row[0].strip()):

                        if row[0] == "key_start":

                            top_level_key = row[1].strip()
                            top_level_dict[top_level_key] = {}

                            row.remove(top_level_key)
                            row.remove('key_start')

                            keys = row
                            after_start = True

                            continue
                        if after_start:
                            column_headings = row
                            after_start = False
                            continue
                        if row[0] == "key_end":

                            interim_dict[top_level_key.strip()]=temp_list

                            top_level_list.append(interim_dict.copy())

                            keys = ""
                            temp_dict = {}
                            temp_list = []
                            interim_dict = {}
                            continue
                        for i in range(0, len(keys)):

                            temp_dict[keys[i].strip()]=row[i].strip()

                        temp_list.append(temp_dict.copy())

        print("Total number of policy sections generated in file: " + str(len(top_level_list)))
        for line in top_level_list:
            print line.keys()


        # Save to JSON file of the same name
        filename_base = filename.split(".")[0]
        json_filename = filename_base + ".json"

        with open(json_filename, 'w') as jsonfile:
            json.dump(top_level_list, jsonfile)

        print("JSON Output has been saved to the file: " + json_filename)

    except IOError:
        # Problem opening the file
        print "There was a problem opening the file " + filename + "!"
        sys.exit('Aborting program Execution')




# Standard call to the main() function.
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Convert CSV file to JSON Payload for ACI Configuration", epilog='Usage: python csv2json.py.py "aci-constructs.csv"')
    parser.add_argument('csv_file', help='Name of the csv file to convert to JSON.')

    arguments = parser.parse_args()

    main()
