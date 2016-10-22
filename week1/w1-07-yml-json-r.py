#!/usr/bin/python -tt
###!/usr/bin/env python
# Project Name: PyNetA
# Project File: w1-07-yml-json-r.py
# User: claud
__author__ = "Claudia de Luna (claudia@indigowire.net)"


import sys
import re
import os
import yaml
import json
import pprint


# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    # Take path argument and list all text files
    """
    YAML/JSON
    6. Write a Python program that creates a list. One of the elements of the list should be a dictionary with at
       least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be
       in the expanded form.
    7. Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty
       prints the data structure that is returned.
    :return:
    """

    # Exercise 7 - Read and Pretty Print YAML and JSON

    dir = sys.argv[1]

    fnames = ([file for root, dirs, files in os.walk(dir)
        for file in files
        if file.endswith('.json') or file.endswith('.yml') #or file.endswith('.pdf')
        ])
    for fname in fnames: print(fname)

    for fname in fnames:
        #if '.yml' in fname:
        #print("fname is ", fname)
        if fname.endswith('.yml'):
            with open(fname) as y:
                yml_contents = yaml.load(y)
            print("\n\n************** Printing YAML File Contents ************** \n")
            print("File name: ", fname)
            pprint.pprint(yml_contents)
        if fname.endswith('.json'):
            #print("In JSON Statement")
            #print("fname in JSON Statement", fname)
        #if '.json' in fname:
            with open(fname) as j:
                #print("file handle in JSON: ", j)
                json_contents = json.load(j)
            print("\n\n************** Printing JSON File Contents ************** \n")
            print("File name: ", fname)
            pprint.pprint(json_contents)



# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '\nUsage: w1-07-yml-json-r.py <path to directory in which to look for JSON or YML files> \nThis script will find all files with a .yml or .json file extension and Pretty Print each file.\nExample: python w1-07-yml-json-r.py "."\n\n'
        sys.exit()
    else:
        main()

