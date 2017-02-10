#!/usr/bin/python -tt
# Project: PyNetACert
# Filename: test
# claud
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2/10/2017"
__copyright__ = "Copyright (c) 2016 Claudia"
__license__ = "Python"

import argparse
import mytest


def main():

    print "Function 1 from mytest package"
    print mytest.func1()

    print "Function 2 from mytest package"
    print mytest.func2()

    print "Function 3 from mytest package"
    print mytest.func3()



# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python test' ")

    #parser.add_argument('all', help='TBD')
    #parser.add_argument('-a', '--all', help='TBD', action='store_true', default=False)
    arguments = parser.parse_args()
    main()


