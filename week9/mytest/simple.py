#!/usr/bin/python -tt
# Project: PyNetACert
# Filename: simple
# claud
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2/9/2017"
__copyright__ = "Copyright (c) 2016 Claudia"
__license__ = "Python"

import argparse
import math
import sys

def func2():
    print "This is simple as " + str(math.pi)


def main():
    func2()


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple Module with function 2",
                                     epilog="Usage: ' python world' ")

    #parser.add_argument('all', help='TBD')
    #parser.add_argument('-a', '--all', help='TBD', action='store_true', default=False)
    arguments = parser.parse_args()
    print "This is the executable part of the code for module " + sys.argv[0] + "!"
    main()


