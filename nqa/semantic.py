import nqa.grammar as gr
import sys
from nqa.error import *
from nqa.zones import Zone

def navigator(zone, depth = 0, line = 1, file = sys.stdout, errors = 0):
    last_line = line
    code_line = []
    tab = "    "

    if zone.name != "root":
        if zone.type == "function":
            code_line += [gr.OPERATOR]
        elif zone.type == "class":
            code_line += [gr.CLASS]
        code_line += [zone.name]

    for dec in range(len(zone.declaration)):
        d = zone.declaration[dec]
        
        if d.relative_line != last_line:
            print(depth * tab + " ".join(code_line), file = file)
            last_line = d.relative_line
            code_line = []
        
        if type(d) == Zone:
            errors += SemanticError(d.line, "Declaring a zone into another a declaration")
            break
        else:
            if d.ID == gr.STRING:
                code_line += [f"'{d.symbol}'"]
            else:
                code_line += [f"{d.symbol}"]
                if d.name == ":":
                    break
    
    if zone.name != "root":
        depth += 1

    for stat in range(len(zone.statements)):
        s = zone.statements[stat]

        if s.relative_line != last_line:
            print(depth * tab + " ".join(code_line), file = file)
            
            last_line = s.relative_line
            code_line = []

        if type(s) == Zone:
            errors = navigator(s, depth - 1, last_line, file, errors)
        else:
            if s.ID == "string":
                code_line += [f"'{s.symbol}'"]
            else:
                code_line += [f"{s.symbol}"]

    return errors

def generator(tree, file_name, errors):

    file_name = file_name + ".py"
    file = open(file_name, "w")

    if errors > 0:
        file.close()
        return errors

    errors = navigator(tree, 0, 1, file, errors)

    file.close()
    return errors

"""
py -m cpp_compiler.py

cd nqa
./py_compiler
cd ..

nqa/dist/nqa build main.nqa -v
"""
