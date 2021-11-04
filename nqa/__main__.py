from nqa.file import  read_module
from nqa.lex import scanner
from nqa.syntax import parser
from nqa.semantic import generator
from nqa.error import *
import sys

params = sys.argv[:]

if len(params) >= 2:
    if params[1] == "build":
        if len(params) >= 3:
            file = sys.argv[2]
            module = read_module(file)
            
            if len(params) == 3:
                tokens = scanner(module)
            elif len(params) == 4:
                arg = sys.argv[3]
                tokens, errors = scanner(module, arg)
                tree, tokens, errors = parser(tokens, errors)
                errors = generator(tree, tokens, errors)
            else:
                ArgumentError(None, "too arguments for build")
            
        else:
            FileError(None, "no file specified")
else:
    ArgumentError(None, "no arguments specified")