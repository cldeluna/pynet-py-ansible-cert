#!/usr/bin/python -tt
# Project Name: PyNetA
# Project File: argparse_action.py
# User: claud
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "9 / 20 / 2016 9:57 AM"
__copyright__ = "Copyright (c) 2016 Claudia de Luna"
__license__ = "Python"

import sys
import re
import os
import argparse


# Provided main() calls the above functions
def main():
    # Take path argument and list all text files
    """
    https://pymotw.com/2/argparse/

    :return:
    """

    parser = argparse.ArgumentParser()
    print("parser: " + str(parser))

    parser.add_argument('-s', action='store', dest='simple_value',
                        help='Store a simple value')

    parser.add_argument('-c', action='store_const', dest='constant_value',
                        const='value-to-store',
                        help='Store a constant value')

    parser.add_argument('-t', action='store_true', default=False,
                        dest='boolean_switch',
                        help='Set a switch to true')
    parser.add_argument('-f', action='store_false', default=False,
                        dest='boolean_switch',
                        help='Set a switch to false')

    parser.add_argument('-a', action='append', dest='collection',
                        default=[],
                        help='Add repeated values to a list',
                        )

    parser.add_argument('-A', action='append_const', dest='const_collection',
                        const='value-1-to-append',
                        default=[],
                        help='Add different values to list')
    parser.add_argument('-B', action='append_const', dest='const_collection',
                        const='value-2-to-append',
                        help='Add different values to list')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    results = parser.parse_args()
    print("results: " + str(results))
    print 'simple_value     =', results.simple_value
    print 'constant_value   =', results.constant_value
    print 'boolean_switch   =', results.boolean_switch
    print 'collection       =', results.collection
    print 'const_collection =', results.const_collection


# Standard call to the main() function.
if __name__ == '__main__':
    #if len(sys.argv) >= 2:
        #print '\nUsage: argparse_action.py <what are the argumentsr>\nExample: python argparse_action.py "arguments"\n\n'
        #sys.exit()
    #else:
    main()

