import nqa.grammar as gr
from nqa.utils import tostring
from nqa.error import *

T, F, e = True, False, ""

class Token(list):
    def __init__(self, lexema, ID, line, position):
        self.append(lexema)
        self.append(ID)
        self.append(line)
        self.append(position)
    
    @property
    def symbol(self):
        return self[0]
    
    @property
    def ID(self):
        return self[1]
    
    @property
    def line(self):
        return self[2]

    @property
    def position(self):
        return self[3]

    def is_expected(self, expected_types):
        if self.ID in expected_types:
            return True
        else:
            SyntaxError(next.line, f"{tostring(expected_types)} expected")
            return False
    
    def is_protected(self):
        return (self.symbol in gr.protected) and (self.ID in gr.protected_indexes)

    def equal(self, symbol):
        return self.ID == get_token_ID(symbol)

class Tokens(list):
    def __init__(self):
        super().__init__()
    
    def add(self, token, id, line, position):
        self.append(Token(token, id, line, position))
    
    def get_names(self):
        names = []
        for token in self:
            assert len(token) >= 2 
            if token[1] == gr.identifier and token[0] not in names:
                names.append(token[0])
        return names

    @property
    def last_line(self):
        assert self._last_line
        return self._last_line
    
    def set_last_line(self, line):
        self._last_line = line

class TokenType:
    def EOF(self, line, i):
        return Token("@EOF@", gr.eof, line, i)

def scanner(text, command = None):
    verbose = command in ["-v"]

    tokens = Tokens()
    commentary, string, name, number, float, operator =  F, F, F, F, F, F
    lexema = e
    line = 1
    errors = 0
    pos = 0

    i = 0
    while i < len(text):
        ch = text[i]

        if ch == "\n":
            line += 1
            pos = 0

        elif commentary and ch not in gr.commentaries:
            pass
        elif commentary and ch in gr.commentaries:
            commentary = F
        
        elif string and ch not in gr.strings:
            lexema += ch
        elif string and ch in gr.strings:
            tokens.add(lexema, gr.STRING, line, pos)
            lexema = ""
            string = F
        
        elif float and ch in gr.digits:
            lexema += ch
        elif float and ch in gr.floating:
            errors += LexicalError(line, f"two {gr.floating} in float definition")
            break
        elif number and not float and ch in (gr.digits + gr.floating):
            lexema += ch
            if ch in gr.floating:
                float = T
        elif number and ch not in (gr.digits + gr.floating):
            if float:
                tokens.add(lexema + "0", gr.FLOAT, line, pos)
            else:
                tokens.add(lexema, gr.INT, line, pos)
            lexema = ""
            number, float = F, F
            i -= 1
            pos -= 1
        elif name and ch in gr.alphanum:
            lexema += ch
        elif name and ch not in gr.alphanum:
            name = F
            tokens.add(lexema, get_token_ID(lexema), line, pos)
            lexema = ""
            i -= 1
            pos -= 1
        elif operator and ch in gr.operators:
            lexema += ch
        elif operator and ch not in gr.operators:
            operator = F
            id = get_token_ID(lexema)
            if id == gr.identifier:
                for lex in lexema:
                    tokens.add(lex, get_token_ID(lex), line, pos)
            else:
                tokens.add(lexema, id, line, pos)
            lexema = ""
            i -= 1
            pos -= 1
        elif not commentary and ch in gr.commentaries:
            commentary = True
        elif not string and ch in gr.strings:
            string = T
        elif not name and ch in gr.alphabet:
            name = T
            lexema += ch
        elif not name and not number and ch in gr.digits:
            number = T
            lexema += ch
        elif not name and not number and not operator and ch in gr.operators:
            operator = T
            lexema += ch
        elif ch not in gr.blanks:
            tokens.add(ch, ch, line, pos)
        i += 1
        pos += 1

    if errors > 0:
        print("Traceback:", tokens)
    elif verbose:
        print(tokens)

    tokens.set_last_line(line)
    
    if verbose:
        print(f"Last line: {line} Last char position: {i}")
        print(f"Tokens detected: {len(tokens)}")
        names = tokens.get_names()
        string_of_names = tostring(names, ", ")
        print(f"Names defined ({len(names)}): {string_of_names}")

    return tokens, errors

def get_token_ID(lexema):
    for token in gr.protected_tokens:
        if lexema == token[0]:
            return token[1]
    return gr.identifier

def get_token_Symbol(lexema):
    for token in gr.protected_tokens:
        if lexema == token[1]:
            return token[0]
    return str(gr.identifier)
