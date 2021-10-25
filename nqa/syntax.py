import nqa.grammar as gr
import nqa.lex as lex
from nqa.error import *

def parser(tokens):
    n = len(tokens)
    protected_indexes = list(range(len(gr.protected)))
    expected_types = gr.ALL + protected_indexes
    chain = []

    last_line = tokens.last_line
    eof_token = lex.TokenType().EOF(last_line)
    tokens.append(eof_token)
    
    i = 0
    while i < n:
        token = tokens[i]
        if token == gr.USE:
            if token.is_expected(expected_types):
                chain.append(token)
            else: break
        else:
            pass
        i += 1
    
    print(tokens)
        