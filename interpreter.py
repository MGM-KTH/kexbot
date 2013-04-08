#!/usr/bin/python2
import nltk

import cnet_client as cnet
import context as ctx

try:
    import json
except:
    import simplejson as json

class Interpreter():    
        
    def __init__(self):
        global context
        context = ctx.Context()    
        
    def process_line(self, line):
        matched_words = self.get_word_tag_match(line,["N","NP"])
        self.print_relations(matched_words)
        context.expand_graph(matched_words)
    
    def get_relations(self, json_obj):
        result = ""
        if not json_obj == "{}":
            for edge in json_obj["edges"]:
                result = result + edge["start"] + ' ' + edge["rel"] + ' ' + edge["end"] + "\n"
            return result
        return "{}"
    
    def query_word(self, word):
        json_document = json.dumps(cnet.lookup(word, limit=5), indent=4, separators=(',', ': '))
        decoder = json.JSONDecoder()
        json_obj = decoder.decode(json_document)
        return json_obj
    
    # Input: A string, A list of tags
    # Output: A list of words that matches any of the specified tags
    def get_word_tag_match(self, text,tags):
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
        
        
    def print_relations(self, list):
        global context
        if not list:
            print "List is empty in print_relations"
        wnl = nltk.stem.wordnet.WordNetLemmatizer()
        for word in list:
            print word+':'
            json_obj = self.query_word(wnl.lemmatize(word))
            relations = self.get_relations(json_obj)
            print relations
        print "\n"
        
        
    # Prints each item in a list
    def print_list(self, list):
        print "\n"
        # Check if list is empty
        if not list:
            print "List is empty in print_list"
            
        # Else, print each item in the list
        else:
            for item in list:
                print item
            print "\n"                
