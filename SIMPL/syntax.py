def syntaxer(tokens):
    for token in tokens:
        pass
    return tokens


from lex import *
from file import  *
tokens = scanner(read_module("main.nqa"), "-v")
syntaxer(tokens)

       
                