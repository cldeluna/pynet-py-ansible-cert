#!/usr/bin/python -tt
# Project Name: PyNetA
# Project File: c1-6-yml-json-w.py
# User: claud
__author__ = "Claudia de Luna (claudia@indigowire.net)"


import sys
import re
import os
import ciscoconfparse as ccp
import yaml
import json



# Provided main() calls the above functions
def main():
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

    # YML/JSON Assignment

    #print(sys.argv[1])

    #cfile = "sin-nag1-shrunonly.txt"
    #cfile = "sin-nag1-mgmt0_2016-04-19_12-00-22.txt"
    cfile = sys.argv[1].strip()
    #print(cfile)

    cfg = ccp.CiscoConfParse(cfile)
    #print(cfg)

    vlans = cfg.find_objects(r"^vlan")
    #print(vlans)
    #print(type(vlans))

    vtot = 0
    for v in vlans:
        vtot += 1
        #print(v.text)
    #print("Total Vlans Found: ", str(vtot))

    list_of_dicts = []

    index = 0
    for v in vlans:

        str1 = v.text.split(' ')
        #print(str1)
        #print(type(str1))
        dict1 = {}
        dict1[str1[0]] = str1[1]
        #print("Dict1: ", dict1)
        str2 = v.children
        #print("String2: ",str2, type(str2))
        #
        for v2 in str2:
            str3 = v2.text.strip()
           # print("Str3: ", str3)
            str3 = str3.split(' ')
            dict1[str3[0]] = str3[1]
            #print("Dict1 again: ", dict1)

        #print("Dict1 out of subloop: ", dict1)
        #print("Index: ", index)
        list_of_dicts.append(dict1)
        #print("List of Dictionaries: ", list_of_dicts)
        index += 1

    print("\n\n**************List of Dictionaries*****************")
    print("Type is ",type(list_of_dicts))
    print("Total Vlans Found: ", str(vtot))
    print("\n")
    #print(list_of_dicts)
    for elem in list_of_dicts:
        print(elem),
        print(" Type = ",type(elem)),
        print(" Number of Elements = ",len(elem))


# Write to YAML
    with open("week1-yaml-output.yml", "w") as ymlfile:
        ymlfile.write("---\n")
        ymlfile.write("#******************Human Readable Format (False)********************\n\n")
        ymlfile.write(yaml.dump(list_of_dicts, default_flow_style=False))
        #ymlfile.write("\n\n******************Less Human Readable Format (True)*******************\n\n")
        #ymlfile.write(yaml.dump(list_of_dicts))


# Write to JSON
    with open("week1-json-output.json", "w") as jsonfile:
        jsonfile.write("\n\n******************JSON File Output********************\n\n")
        json.dump(list_of_dicts, jsonfile)




# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '\nUsage: c1-6-yml-json-w.py <what are the argumentsr>\nExample: python c1-6-yml-json-w.py "arguments"\n\n'
        sys.exit()
    else:
        main()

