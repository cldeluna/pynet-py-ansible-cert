#!/usr/bin/python -tt
# Project: PyNetACert
# Filename: world
# claud
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2/9/2017"
__copyright__ = "Copyright (c) 2016 Claudia"
__license__ = "Python"

import argparse
import random
import sys
from cowpy import cow


def func1():
    print "This is the importable part of the code!"
    num = random.randrange(0,1000000)
    print "Today your number is " + str(num)

    return num

class MyClass(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def hello(self):
        hello_text = "Hello " + self.a + " " + self.b + " " + self.c + "!"

        msg = cow.milk_random_cow(hello_text)
        print(msg)

    def not_hello(self):
        gby_text = "Goodbye " + self.a + " " + self.b + " " + self.c + "!"

        cheese = cow.Moose(eyes='dead')
        msg = cheese.milk(gby_text)
        print(msg)

class NewClass(MyClass):

    # Exercise 6 adding r
    def __init__(self, r, a, b, c):
        self.r = r
        super(NewClass, self).__init__(a, b, c)

    def new_hello(self):
        choice = [self.a,  self.b,  self.c]

        new_hello_text = "Hello " + random.choice(choice) + "!"
        msg = cow.milk_random_cow(new_hello_text)

        print(msg)

    def new_random(self):
        print self.r

def main():

    # Excercise 1
    print func1()

    # Exercise 4
    input_a = raw_input("Enter value for variable a: ")
    input_b = raw_input("Enter value for variable b: ")
    input_c = raw_input("Enter value for variable c: ")

    mc1 = MyClass(input_a, input_b, input_c)

    print mc1.hello()
    print mc1.not_hello()

    # Exercise 5
    num = random.randrange(0, 100)
    nmc1 = NewClass(num, input_a, input_b, input_c)

    print "Printing new_hello method"
    print nmc1.new_hello()

    # Exercise 6
    print "Printing new_random method"
    print nmc1.new_random()


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="World Module with function 1",
                                     epilog="Usage: ' python world' ")

    #parser.add_argument('all', help='TBD')
    #parser.add_argument('-a', '--all', help='TBD', action='store_true', default=False)
    arguments = parser.parse_args()
    print "This is the executable part of the code for module " + sys.argv[0] + "!"
    main()


