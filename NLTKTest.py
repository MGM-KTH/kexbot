#!/usr/bin/python2

import sys
import nltk
import cmd
import argparse

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format 

class NLTKTest(cmd.Cmd):
	
	print "\n"
	cprint(figlet_format('kexbot!', font='starwars'),
	       'red', attrs=['bold'])
	print "\n"
	prompt = ">"
		
	def do_EOF(self, line):
		return True	
	
		s
	# Input: A string, A list of tags
	# Output: A list of words that matches any of the specified tags
	def get_word_tag_match(self,text,tags):
		found_words = []
		# Tokenize the text (put into tuples)
		tokenized_words = nltk.word_tokenize(text)
		# Get tags for each word
		tagged_words = nltk.pos_tag(tokenized_words)
		
		# Loop the tuples
		for word_tuple in tagged_words:
			(word, tag) = word_tuple
			# Convert tags to simple tags (a simplified tagset)
			simple_tag = nltk.tag.simplify.simplify_wsj_tag(tag)
			if(simple_tag in tags):
				found_words.append(word)
				
		return found_words		
					
					
		
	# Prints each item in a list
	def print_list(self,list):
		print "\n"
		
		# Check if list is empty
		if not list:
		  print "List is empty"
		
		# Else, print each item in the list
		else:
			for item in list:
				print item
			print "\n"					
		
		
	# Run the program
	def default(self, line):
		test = NLTKTest()
		# Find words with correct tags
		words = test.get_word_tag_match(line, ["N"])
		
		# Print the result
		test.print_list(words)
	
	'''	
	def do_classify(self,line):
		
		test = NLTKTest()
		# Find words with correct tags
		words = test.get_word_tag_match(line, tags)
		
		# Print the result
		test.print_list(words)
	'''
		
	 
	
	def parse_input():
		pass
			
	
if __name__ == '__main__':
	NLTKTest().cmdloop()
	