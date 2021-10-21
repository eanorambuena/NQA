from grammar import *
from error import *

T, F = True, False

def scanner(text, command = None):
    tokens = []
    commentary, string, name, number, float =  F, F, F, F, F
    lexema = ""
    line = 1
    errors = 0

    for i in range(len(text)):
        ch = text[i]

        if ch == "\n":
            line += 1

        elif commentary and ch not in commentaries:
            pass
        elif commentary and ch in commentaries:
            commentary = F
        
        elif string and ch not in strings:
            lexema += ch
        elif string and ch in strings:
            tokens.append([lexema, STRING])
            lexema = ""
            string = F
        
        elif float and ch in digits:
            lexema += ch
        elif float and ch in floating:
            errors += Error(line, f"Error, two {floating} in float definition")
            break
        elif number and not float and ch in (digits + floating):
            lexema += ch
            if ch in floating:
                float = T
        elif number and ch not in (digits + floating):
            if float:
                tokens.append([lexema + "0", FLOAT])
            else:
                tokens.append([lexema, INT])
            lexema = ""
            number, float = F, F
        
        elif name and ch in alphanum:
            lexema += ch
        elif name and ch not in alphanum:
            name = F
            tokens.append([lexema, get_token_ID(lexema)])
            lexema = ""
        
        elif not commentary and ch in commentaries:
            commentary = True
        elif not string and ch in strings:
            string = T
        elif not name and ch in alphabet:
            name = T
            lexema += ch
        elif not name and not number and ch in digits:
            number = T
            lexema += ch
        elif ch not in blanks:
            tokens.append([ch, ch])

    result = tokens + [f"Last line: {line}"]

    if errors > 0:
        print("Traceback:", result)
    elif command in ["-v", "-verbose"]:
        print(result)

    return tokens