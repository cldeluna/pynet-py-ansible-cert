#!/usr/bin/python -tt
# Project: PyNetACert
# Filename: whatever
# claud
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2/9/2017"
__copyright__ = "Copyright (c) 2016 Claudia"
__license__ = "Python"

import argparse
import sys
from cowpy import cow
import random


def func3():
    s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie",
               "This cool guy my gardener met yesterday", "Superman"]
    p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats",
               "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people",
               "Supermen"]
    s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on",
               "retards", "meows on", "flees from", "tries to automate", "explodes"]
    p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard",
               "meow on", "flee from", "try to automate", "explode"]
    infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.",
                   "to be able to make toast explode.", "to know more about archeology."]

    if raw_input("Would you like to add a new word? ").lower() == "yes":
        new_word = raw_input("Please enter a singular noun.")
        s_nouns.append(new_word)
        msg = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(
            p_nouns).lower(), random.choice(infinitives)
    else:
        msg = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(
            p_nouns).lower(), random.choice(infinitives)

    cheese = cow.Moose(thoughts=True)
    cheese_msg = cheese.milk(str(msg))
    print(cheese_msg)


    return msg

def main():
    cow_msg = func3()

    cheese = cow.Moose(thoughts=True)
    msg = cheese.milk(str(cow_msg))
    print(msg)


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Whatever Module with function 3",
                                     epilog="Usage: ' python world' ")

    #parser.add_argument('all', help='TBD')
    #parser.add_argument('-a', '--all', help='TBD', action='store_true', default=False)
    arguments = parser.parse_args()
    print "This is the executable part of the code for module " + sys.argv[0] + "!"
    main()


