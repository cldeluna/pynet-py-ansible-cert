#!/usr/bin/python -tt
# Project: PyNetACert
# Filename: love_the_smell
# claud
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2/10/2017"
__copyright__ = "Copyright (c) 2016 Claudia"
__license__ = "Python"

import argparse


def some_function():
    pass


def main():
    pass


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python love_the_smell' ")

    #parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',
                        default=False)
    arguments = parser.parse_args()
    main()


