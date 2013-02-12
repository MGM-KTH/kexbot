#!/usr/bin/python2

import nltk
import cmd

from cnet_client import *

class kexbot(cmd.Cmd):

    prompt = ">"

    def do_EOF(self, line):
        return True

    def do_lookup(self, line):
        jsondocument = json.dumps(lookup(*line.split(' ')), indent=4, separators=(',', ': '))
        decoder = json.JSONDecoder()
        jsonobj = decoder.decode(jsondocument)
        for edge in jsonobj["edges"]:
            print edge["start"] + ' ' + edge["rel"] + ' ' + edge["end"]

    def default(self, line):
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        simp = [(word, nltk.tag.simplify.simplify_wsj_tag(tag)) for word, tag in tagged]
        print simp

if __name__ == '__main__':
    kexbot().cmdloop()
