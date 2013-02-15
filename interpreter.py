#!/usr/bin/python2
import nltk

import cnet_client as cnet

try:
    import json
except:
    import simplejson as json

    
def process_line(line):
    matched_words = get_word_tag_match(line,["N","NP"])
    print_relations(matched_words)

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

# Input: A string, A list of tags
# Output: A list of words that matches any of the specified tags
def get_word_tag_match(text,tags):
    found_words = []
    # Tokenize the text (put into tuples)
    tokenized_words = nltk.word_tokenize(text)
    # Get tags for each word
    nltk_tagged_words = nltk.pos_tag(tokenized_words)
    # Convert tags to simple tags (a simplified tagset)
    tagged_words = [(word, nltk.tag.simplify.simplify_wsj_tag(tag)) for word, tag in nltk_tagged_words]
    #Print tuple array to see how the words were tagged
    print tagged_words
    # Loop the tuples
    for word_tuple in tagged_words:
        (word, tag) = word_tuple
        if(tag in tags):
            found_words.append(word)
                
    return found_words
    
    
def print_relations(list):
    if not list:
        print "List is empty in print_relations"
    for word in list:
        print word+':'
        json_obj = query_word(word)
        relations = get_relations(json_obj)
        print relations
    
    
# Prints each item in a list
def print_list(list):
    print "\n"
    # Check if list is empty
    if not list:
        print "List is empty in print_list"
        
    # Else, print each item in the list
    else:
        for item in list:
            print item
        print "\n"                
