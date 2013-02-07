#!/usr/bin/python2

import nltk
import cmd


class kexbot(cmd.Cmd):

    prompt = ">"

    def do_EOF(self, line):
        return True

    def default(self, line):
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        simp = [(word, nltk.tag.simplify.simplify_wsj_tag(tag)) for word, tag in tagged]
        print simp

if __name__ == '__main__':
    kexbot().cmdloop()
