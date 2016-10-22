#!/usr/bin/python -tt
### #!/usr/bin/env python
# Project Name: PyNetA
# Project File: w1-08-ccp-crypto.py
# User: claud
__author__ = "Claudia de Luna (claudia@indigowire.net)"

import sys
import re
import os
import ciscoconfparse as ccp

# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    8. Write a Python program using ciscoconfparse that parses this config file, cisco_ipsec.txt.
    Note, this config file is not fully valid (i.e. parts of the configuration are missing).
    The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO')
    and for each crypto map entry print out its children.

    9. Find all of the crypto map entries that are using PFS group2

    10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name).
    Print these entries and their corresponding transform set name.

    """

    # Exercise 8

    srch_str = 'crypto map CRYPTO'
    #print(srch_str)

    cfg = ccp.CiscoConfParse("cisco_ipsec.txt")

    crpy = cfg.find_objects(r"^crypto map CRYPTO")


    #print("Children :",cryp_kids)

    print("\n====PARENT LEVEL ITEMS===")
    for item in crpy:
        print(item.text)
    print("\n\n")

    for item in crpy:
        print("===PARENT=== " + item.text)
        print("=======CHILD LEVEL ITEMS======")
        for i in item.children:
            print(i.text)
        print("\n")

    # Exercise 9

    crpy_kids = cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec="pfs group2")
    print("\n====PARENT LEVEL ITEMS in SEARCH for PFS Group2===")
    for item in crpy_kids:
        print(item.text)
        print("Parent: " + str(item.is_parent))
        print("Children: " + str(item.is_child))
        print("Children items: " + str(item.children))
    print("\n")


    crpy_kids_noaes = cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec="set transform-set AES")
    print("\n====PARENT LEVEL ITEMS in SEARCH for !AES===")
    for item in crpy_kids_noaes:
        print(item.text)
        print("Parent: " + str(item.is_parent))
        print("Children: " + str(item.is_child))
        print("Children items: " + str(item.children))

    print("\n")

# Standard call to the main() function.
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print '\nUsage: w1-08-ccp-crypto.py <what are the argumentsr>\nExample: python w1-08-ccp-crypto.py "arguments"\n\n'
        sys.exit()
    else:
        main()

