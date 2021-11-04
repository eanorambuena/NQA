import nqa.grammar as gr
import nqa.lex as lex
from nqa.error import *

def generator(tree, tokens, errors):

    file_name = "NQA_middle_code.py"
    file = open(file_name, "w")

    if errors > 0:
        file.close()
        return errors

    code = ""

    file.write(code)

    file.close()
    return errors

"""
cd nqa
./py_Compiler
cd ..
nqa/dist/nqa build main.nqa -v
"""
