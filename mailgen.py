#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random
import sys
import signal
import os

def GetArguments():
    # Get some commandline arguments:
    argParser=argparse.ArgumentParser(description='Use mailgen to generate bogus e-mail addresses.')
    argParser.add_argument('-names', metavar="<filename>", help='Enter a file which contains names that contains names to construct e-mail addresses from')
    argParser.add_argument('-char', metavar="<character>", help='Supply a character between two names, defaults to a hyphen \'-\'.', default = '-')
    argParser.add_argument('-domain', metavar="<domainname>", help='Supply a domain name, defaults to a <randomname>.com.')
    argParser.add_argument('-timeout', metavar="<seconds>", help='Supply an interval for the script to wait between e-mail addresses.')
    return argParser.parse_args()

__version__ = '0.1'

def SignalHandler(sig, frame):
    # Create a break routine:
    sys.stderr.write("\nCtrl-C detected, exiting...\n")
    sys.exit(1)

lArgs = GetArguments()
    
def main():
    signal.signal(signal.SIGINT, SignalHandler)

    if lArgs.names:
        fOut = open(lArgs.names, 'r')
    else:
        fOut = open(os.path.dirname(os.path.realpath(__file__)) + "/firstnames.txt", 'r')
        
        

    lNames = fOut.read().splitlines()
    
    while True:

        if lArgs.domain:
            domain = lArgs.domain
        else:
            domain = lNames[random.randint (0, len(lNames))-1] + ".com"
            #print(len(lNames))
            #print(lNames[random.randint (0, len(lNames))-1])
            
        name1 = lNames[random.randint (0, len(lNames))-1]
        name2 = lNames[random.randint (0, len(lNames))-1]
        
        print ((name1 + lArgs.char + name2 + "@" + domain).lower())

if __name__ == '__main__':
    main()