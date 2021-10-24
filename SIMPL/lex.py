from grammar import *
from error import *

T, F = True, False

def scanner(text, command = None):
    tokens = []
    commentary, string, name, number, float, operator =  F, F, F, F, F, F
    lexema = ""
    line = 1
    errors = 0

    i = 0
    while i < len(text):
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
            i -= 1
        elif name and ch in alphanum:
            lexema += ch
        elif name and ch not in alphanum:
            name = F
            tokens.append([lexema, get_token_ID(lexema)])
            lexema = ""
            i -= 1
        elif operator and ch in operators:
            lexema += ch
        elif operator and ch not in operators:
            operator = F
            id = get_token_ID(lexema)
            if id == identifier:
                for lex in lexema:
                    tokens.append([lex, get_token_ID(lex)])
            else:
                tokens.append([lexema, id])
            lexema = ""
            i -= 1
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
        elif not name and not number and not operator and ch in operators:
            operator = T
            lexema += ch
        elif ch not in blanks:
            tokens.append([ch, ch])
        i += 1

    result = tokens + [f"Last line: {line}"]

    if errors > 0:
        print("Traceback:", result)
    elif command in ["-v", "-verbose"]:
        print(result)

    return tokens