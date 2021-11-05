import time
start = time.time()

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
                arg = None
                
            elif len(params) >= 4:
                arg = sys.argv[3]

            start_compilation = time.time()

            tokens, errors, lex_log = scanner(module, arg)
            tree, tokens, errors = parser(tokens, errors)
            errors = generator(tree, tokens, errors)

            log = lex_log

            if errors != 0:
                stat = -1
            else:
                stat = 0

            print(f"Compilation finished with status {stat}")
            
            print(log, end = "")

            now = time.time()
            runtime = now - start
            compilation_time = now - start_compilation

            print(f"Runtime: {1000 * runtime} miliseconds")
            print(f"Compilation time: {1000 * compilation_time} miliseconds")
            
        else:
            FileError(None, "no file specified")
else:
    ArgumentError(None, "no arguments specified")