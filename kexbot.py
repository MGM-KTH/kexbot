#!/usr/bin/python2

import nltk
import cmd


import interpreter as it
import cnet_client as cnet

class Kexbot(cmd.Cmd):

    prompt = ">"

    def do_EOF(self, line):
        return True

    def do_lookup(self, line):
        cnet.lookup(*line.split(' '))

    def default(self, line):
        it.processLine(line)

if __name__ == '__main__':
    Kexbot().cmdloop()
