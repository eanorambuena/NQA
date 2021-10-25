from nqa.utils import tolist, tokenize

mayusc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alphabet = mayusc + mayusc.lower() + "_"
digits = "0123456789"
alphanum = alphabet + digits
blanks = "/t /n"
strings = "\"\'"
commentaries = "~"
floating = "."
one_char_symbols = "+-*/%=<>()[]{}#$@,"
two_char_symbols = ["//", "==", "<=", ">="]

FLOAT = "float"
INT = "int"
STRING = "string"
NULL = "none"

USE = "use"
INCLUDE, PASS = "import", "pass"
IF, ELIF, ELSE = "if", "elsif", "else"
WHILE, FOR, BREAK, CONTINUE = "while", "for", "break", "skip"
OPERATOR, RETURN = "operator", "return"
CLASS, SELF = "class", "self"
AND, OR, NOT = "and", "or", "not"

preprocess = [USE]
process = [INCLUDE, PASS]
conditionals = [IF, ELIF, ELSE]
loops = [WHILE, FOR, BREAK, CONTINUE]
functions = [OPERATOR, RETURN]
classes = [CLASS, SELF]
bools = [AND, OR, NOT]

primitives = [FLOAT, INT, STRING, NULL]
std_funcs = preprocess + conditionals + loops + functions + classes + bools
operators = tolist(one_char_symbols) + two_char_symbols

protected = primitives + std_funcs + operators

protected_tokens = tokenize(protected)

identifier = 300
eof = 400
codes = [identifier, eof]

ALL = primitives + codes