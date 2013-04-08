#!/usr/bin/python2

import sys
import nltk
import cmd


from termcolor import cprint 
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
import interpreter as interpreter
import cnet_client as cnet
from pyfiglet import figlet_format 

class Kexbot(cmd.Cmd):

    print "\n"
    cprint(figlet_format('kexbot!', font='starwars'),
	       'red', attrs=['bold'])
    print "\n"
    prompt = ">"
    
    global it
    it = interpreter.Interpreter()

    def do_EOF(self, line):
        return True

    def do_lookup(self, line):
        print it.get_relations(it.query_word(line))

    def do_search(self, line):
        args = line.split(' ')
        if not len(args) == 5:
            print "must have 5 arguments"
            return
        for i, arg in enumerate(args):
            if arg == "null":
                args[i] = None
            if i == 4:
                if arg == "True":
                    args[i] = True
                else:
                    args[i] = False
        print args

        print cnet.search(rel=args[0], start=args[1], end=args[2], limit=args[3], absolute=args[4])

    def do_assoc(self, line):
        args = line.split(' ')
        if not len(args) == 4:
            print "must have 4 arguments"
            return
        for i, arg in enumerate(args):
            if arg == "null":
                args[i] = None
            if i == 3:
                if arg == "True":
                    args[i] = True
                else:
                    args[i] = False

        print cnet.assoc(word=args[0], filt=args[1], limit=args[2], absolute=args[3])

    def default(self, line):
        it.process_line(line)

if __name__ == '__main__':
    Kexbot().cmdloop()
