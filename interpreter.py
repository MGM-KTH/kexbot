#!/usr/bin/python2
import nltk

import cnet_client as cnet

try:
    import json
except:
    import simplejson as json

    
def processLine(line):
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    simp = [(word, nltk.tag.simplify.simplify_wsj_tag(tag)) for word, tag in tagged]
    for tup in simp:
        (word, cat) = tup
        if cat == "N":
            processJson(word)
    print simp

def processJson(word):
    jsondocument = json.dumps(cnet.lookup("c", "en", word), indent=4, separators=(',', ': '))
    decoder = json.JSONDecoder()
    jsonobj = decoder.decode(jsondocument)
    for edge in jsonobj["edges"]:
        print edge["start"] + ' ' + edge["rel"] + ' ' + edge["end"]
