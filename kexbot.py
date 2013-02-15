#!/usr/bin/python2

import sys
import nltk
import cmd


from termcolor import cprint 
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
import interpreter as it
import cnet_client as cnet
from pyfiglet import figlet_format 

class Kexbot(cmd.Cmd):

    print "\n"
    cprint(figlet_format('kexbot!', font='starwars'),
	       'red', attrs=['bold'])
    print "\n"
    prompt = ">"

    def do_EOF(self, line):
        return True

    def do_lookup(self, line):
        cnet.lookup(*line.split(' '))

    def default(self, line):
        it.process_line(line)

if __name__ == '__main__':
    Kexbot().cmdloop()
