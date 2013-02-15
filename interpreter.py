#!/usr/bin/python2
import nltk

import cnet_client as cnet

try:
    import json
except:
    import simplejson as json

    
def process_line(line):
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    simp = [(word, nltk.tag.simplify.simplify_wsj_tag(tag)) for word, tag in tagged]
    print simp
    for tup in simp:
        (word, cat) = tup
        if cat == "N":
            print word+':'
            json_obj = query_word(word)
            relations = get_relations(json_obj)
            print relations

def get_relations(json_obj):
    result = ""
    for edge in json_obj["edges"]:
        result = result + edge["start"] + ' ' + edge["rel"] + ' ' + edge["end"] + "\n"
    return result

def query_word(word):
    json_document = json.dumps(cnet.lookup("c", "en", word, 5), indent=4, separators=(',', ': '))
    decoder = json.JSONDecoder()
    json_obj = decoder.decode(json_document)
    return json_obj
