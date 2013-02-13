#!/usr/bin/python2
import nltk

from cnet_client import *

class Interpreter():
    
    def process(self, line):
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        simp = [(word, nltk.tag.simplify.simplify_wsj_tag(tag)) for word, tag in tagged]
        for tup in simp:
            (word, cat) = tup
            if cat == "N":
                jsondocument = json.dumps(lookup("c", "en", word), indent=4, separators=(',', ': '))
                decoder = json.JSONDecoder()
                jsonobj = decoder.decode(jsondocument)
                for edge in jsonobj["edges"]:
                    print edge["start"] + ' ' + edge["rel"] + ' ' + edge["end"]
        print simp

    def lookup(self, line):
        jsondocument = json.dumps(lookup(*line.split(' ')), indent=4, separators=(',', ': '))
        decoder = json.JSONDecoder()
        jsonobj = decoder.decode(jsondocument)
        for edge in jsonobj["edges"]:
            print edge["start"] + ' ' + edge["rel"] + ' ' + edge["end"]
