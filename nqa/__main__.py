from nqa.file import  read_module
from nqa.lex import scanner
from nqa.syntax import parser
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
                tokens = scanner(module, arg)
                tree = parser(tokens)
            else:
                print("Error: too arguments for build")
            
        else:
            print("Error: No file specified")
else:
    print("Error: No arguments specified")