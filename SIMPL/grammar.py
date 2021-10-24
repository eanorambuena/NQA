from utils import *

mayusc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alphabet = mayusc + mayusc.lower() + "_"
digits = "0123456789"
alphanum = alphabet + digits
blanks = "/t /n"
strings = "\"\'"
commentaries = "~"
floating = "."

FLOAT = "float"
INT = "int"
STRING = "string"
BOOL = "bool"
NULL = "none"
identifier = 300

preprocess = ["use"]
process = ["import", "pass"]
conditionals = ["if", "elsif", "else"]
loops = ["while", "for", "break"]
functions = ["operator", "return"]
classes = ["class", "self"]

primitives = [FLOAT, INT, STRING, BOOL, NULL]
std_funcs = preprocess + conditionals + loops + functions + classes
operators = tolist("+-*/%=<>()[]{}#$@,") + ["//", "==", "<=", ">="]

protected = primitives + std_funcs + operators

protected_tokens = tokenize(protected)

def get_token_ID(lexema):
    for token in protected_tokens:
        if lexema == token[0]:
            return token[1]
    return identifier

def get_token_Symbol(lexema):
    for token in protected_tokens:
        if lexema == token[1]:
            return token[0]
    return str(identifier)

def get_names(tokens):
    names = []
    for token in tokens:
        if token[1] == identifier and token[0] not in names:
            names.append(token[0])
    return names