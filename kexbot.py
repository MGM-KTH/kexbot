#!/usr/bin/python2

import nltk
import cmd


import interpreter
from cnet_client import *

class Kexbot(cmd.Cmd):

    prompt = ">"

    def do_EOF(self, line):
        return True

    def do_lookup(self, line):
        i.lookup(line)

    def default(self, line):
        i.process(line)

if __name__ == '__main__':
    i = interpreter.Interpreter()
    Kexbot().cmdloop()
