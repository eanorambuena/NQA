import nqa.grammar as gr
import nqa.lex as lex
from nqa.error import *

def parser(tokens, errors):
    n = len(tokens)
    expected_types = gr.ALL
    tree, chain = [], []
    expecting = False
    errors = 0

    last_line = tokens.last_line
    eof_token = lex.TokenType().EOF(last_line)
    tokens.append(eof_token)
    
    if errors > 0:
        return tree, tokens, errors

    i = 0
    while i < n:
        token = tokens[i]
        
        # SyntaxError
        if token.is_expected(expected_types):
            chain.append(token)
            expecting = False
        else:
            errors += 1
            break

        # Set expected_types
        if token.equal(gr.USE) or token.equal(gr.INCLUDE):
            expected_types = gr.STRING
            expecting = True
        
        elif token.equal(gr.PASS):
            expected_types = gr.protected_IDs + gr.codes
            expecting = False
        else:
            pass
        if not expecting and len(chain) > 0:
            tree.append(chain)
            chain = []
        i += 1
    
    return tree, tokens, errors
        