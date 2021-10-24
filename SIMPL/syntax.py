def syntaxer(tokens):
    for token in tokens:
        pass
    return tokens


from lex import *
from file import  *
syntaxer(scanner(read_module("main.nqa")))

print("\n", protected_tokens)

       
                