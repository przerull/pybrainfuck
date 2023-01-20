#!/usr/bin/env python

#Name: brainfuck.py
#Author: Philip Zerull
#Date Created: Friday December 16, 2011

import re
import sys
import os
import unittest


class Interpreter(object):
    def __init__(self):
        """
            Constructor method

            Returns an initialized interpreter object.
        """
        self.reset()

    def reset(self):
        """
            This method resets the interpreter's information to
            an initialized state.
        """
        self._data = {0:0}
        self._data_pointer = 0
        self._code = ''
        self._code_pointer = 0
        self._bracketcount = 0
        self._program_output = ''
        self._program_input = []
        self._debug = False

    def interpret(self, code, program_input, reset_on_finish=True):
        """
            This method takes the code of a brainfuck program, and any input
            to the program, then cleans the code, and interprets it using
            the provided input.   By default this method automatically resets
            the state of the interpreter once finished, but you can change
            that functionality by providing the reset_on_finish parameter.
        """
        self._code = code
        self._cleanse_code()
        self._program_input = list(program_input)
        self._code_traversal()
        outey = self._program_output
        if reset_on_finish:
            self.reset()
        return outey

    def _cleanse_code(self):
        """
            This method cleans the code by stripping out any characters
            invalid in a brainfuck program.
        """
        keepchars = r'[^\+\_\-\.\,\>\<\]\[]'
        outey = re.sub(keepchars, '', self._code)
        self._code = outey

    def _code_traversal(self):
        """
            This is the main loop of the interpreter.   It handles
            all code traversal (including normal processing, forward
            jumping caused by an open bracket, and backward jumping
            caused by a closed bracket)
        """
        while self._code_pointer < len(self._code):
            if self._debug:
                self._debug_output()
            if self._bracketcount == 0:
                self._normal_parsing()
            elif self._bracketcount > 0:
                self._forward_jump()
            else:
                self._backward_jump()

    def _debug_output(self):
        """
            This method provides a simple snapshot into the interpreter's
            state.   It's very handy while debugging brainfuck programs.
        """
        formattuple= (
            self._code_pointer,
            self._code[self._code_pointer],
            self._data,
            self._data_pointer,
            self._bracketcount,
            self._program_output,
            self._program_input
        )
        outey = '%s %s %s %s %s %s %s' % formattuple
        print(outey)

    def _normal_parsing(self):
        """
            This method handles the current brainfuck command and moves
            the code pointer appropriately.
        """
        self._handle_character()
        if self._bracketcount >= 0:
            self._code_pointer += 1
        else:
            self._code_pointer -= 1

    def _forward_jump(self):
        """
            This method handles forward jumping caused by open brackets.
            It checks to see if the current brainfuck command is a bracket,
            handles it appropriately, then moves the code pointer as needed.
        """
        self._bracket_checker()
        if self._bracketcount > 0:
            self._code_pointer += 1

    def _backward_jump(self):
        """
            This method handles backward jumping caused by closing brackets.
            It checks to see if the current brainfuck command is a bracket,
            handles it appropriately, then moves the code pointer as needed.
        """
        self._bracket_checker()
        if self._bracketcount < 0:
            self._code_pointer -= 1

    def _handle_character(self):
        """
            This method checks the current brainfuck command and executes
            that command.
        """
        curcode = self._code[self._code_pointer]
        if curcode == '+':
            self._handle_plus()
        elif curcode == '-':
            self._handle_minus()
        elif curcode == '>':
            self._handle_gt()
        elif curcode == '<':
            self._handle_lt()
        elif curcode == '.':
            self._handle_period()
        elif curcode == ',':
            self._handle_comma()
        elif curcode == '_':
            self._handle_underscore()
        else:
            self._bracket_checker()

    def _bracket_checker(self):
        """
            This method checks if the current brainfuck command is a bracket
            and executes the command if it is a bracket.

            This method is kept separately from the rest of the brainfuck
            commands in the _handle_character command because while jumping
            because of brackets we are only interested in doing something if
            we encounter a bracket.
        """
        curcode = self._code[self._code_pointer]
        if curcode == '[':
            self._handle_open_bracket()
        elif curcode == ']':
            self._handle_close_bracket()

    def _handle_underscore(self):
        """
            Performs the appropriate action for an underscore.

            I added this command to the brainfuck language to provide a
            debugging facility.
        """
        self._debug_output()

    def _handle_plus(self):
        """
            Performs the appropriate action for a plus sign
        """
        self._data[self._data_pointer] += 1

    def _handle_minus(self):
        """
            Performs the appropriate action for a minus sign
        """
        self._data[self._data_pointer] -= 1

    def _handle_period(self):
        """
            Performs the appropriate action for a period
        """
        theord = self._data[self._data_pointer] % 256
        thechar = chr(theord)
        if theord != 0:
            self._program_output += thechar

    def _handle_comma(self):
        """
            Performs the appropriate action for a comma
        """
        if len(self._program_input):
            thedata = ord(self._program_input.pop(0))
        else:
            thedata = 0
        self._data[self._data_pointer] = thedata

    def _sequester_data(self):
        """
            This method ensures that the interal dictionary self._dict
            has a key for the current data_pointer.  This prevents
            keyerrors during processing.
        """
        if self._data_pointer not in self._data:
            self._data[self._data_pointer] = 0

    def _handle_gt(self):
        """
            Performs the appropriate action for a minus sign
        """
        self._data_pointer += 1
        self._sequester_data()

    def _handle_lt(self):
        """
            Performs the appropriate action for a minus sign
        """
        self._data_pointer -= 1
        self._sequester_data()

    def _handle_open_bracket(self):
        """
            Performs the appropriate action for a minus sign
        """
        if self._data[self._data_pointer] == 0 or self._bracketcount != 0:
            self._bracketcount += 1

    def _handle_close_bracket(self):
        """
            Performs the appropriate action for a minus sign
        """
        if self._data[self._data_pointer] != 0 or self._bracketcount != 0:
            self._bracketcount -= 1

def interpret(code, standard_input=''):
    the_interpreter = Interpreter()
    outey = the_interpreter.interpret(code, standard_input)
    return outey

def main():
    if len(sys.argv) > 1:
        code = open(sys.argv[1], 'r').read()
        if ',' in code:
            print('Enter any input to the program here')
            print('-----------------------------------')
            theinput = input()
        else:
            theinput = ''
        outey = interpret(code, theinput)
        print(outey)

if __name__ == '__main__':
    main()


