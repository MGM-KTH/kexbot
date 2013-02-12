#!/usr/bin/python

import sys,nltk

class NLTKTest:
	
	text_input = ""
	
	def __init__(self): # Empty constructor
		pass
	
	def read_input():
		text = sys.stdin.readline() # Read one line of text
		return text
		
	
		
	def print_nouns(text):
			tokenized_words = nltk.word_tokenize(text)
			tagged_words = nltk.pos_tag(tokenized_words)
			print "\nNouns:"
			for word_tuple in tagged_words:
				(word,tag) = word_tuple
				if(tag == ('NN' or 'NNP')):
					print word
					
			print "\n"	
		
		
		
	text_input = read_input()
	print_nouns(text_input)