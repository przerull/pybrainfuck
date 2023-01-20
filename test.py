#!/usr/bin/env python

#Name: test.py
#Author: Philip Zerull
#Date Created: Friday July 20, 2012


import os, sys
from brainfuck import Interpreter, interpret

def main():
    print('does it work:', interpret('+'*98 + '-.') == 'a')
    print('does it work:', interpret('+'*97 + '>' + '+' * 98 + '.<.') == 'ba')
    print('does it work:', interpret(',.[,.]', 'banana') == 'banana')
    print('does it work:', interpret('+[,.]', 'banana') == 'banana')

    return 0



if __name__ == '__main__':
    main()
