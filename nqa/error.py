def Error(line, message, type):
    print(f"{type}Error in line {line}: {message}")
    return 1

def LexicalError(line, message):
    return Error(line, message, "Lexical")

def SyntaxError(line, message):
    return Error(line, message, "Syntax")