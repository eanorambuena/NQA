import nqa.grammar as gr
import nqa.lex as lex
from nqa.error import *
from nqa.zones import Zone

def parser(tokens, errors):
    n = len(tokens)
    expected_types = gr.ALL
    expecting = False
    errors = 0
    function_declaration = False
    class_declaration = False

    last_line = tokens.last_line
    eof_token = lex.TokenType().EOF(last_line[0], last_line[1])
    tokens.append(eof_token)

    #Initialize the tree
    tree = Zone("root", 0, "function")
    tk = [lex.Token('(', 30, -1, 2, 1), lex.Token(')', 31, -1, 3, 1), lex.Token(':', ':', -1, 1, 1)]
    
    for t in tk:
        tree.declaration.append(t)
    
    zone = tree
    declaration, statements = False, True

    if errors > 0:
        return tree, tokens, errors

    i = 0
    while i < n:
        token = tokens[i]

        # SyntaxError
        if expecting:
            if token.is_expected(expected_types):
                expecting = False
            else:
                errors += 1
                break
        else:
            expected_types = gr.ALL

        # Set expected_types
        if token.equal(gr.USE) or token.equal(gr.INSTALL):
            expected_types = [gr.STRING]
            expecting = True
        elif token.equal(gr.WAIT):
            expected_types = [gr.INT, gr.FLOAT]
            expecting = True
        
        assert len(token) > 3

        if function_declaration:
            declaration = True
            statements = False
            zone = Zone(token.symbol, token.line, type = "function", parent = zone)
            function_declaration = False
        elif class_declaration:
            declaration = True
            statements = False
            zone = Zone(token.symbol, token.line, type = "class", parent = zone)
            class_declaration = False
        
        if token.symbol in [gr.IF, gr.WHILE, gr.FOR]:
            zone = Zone(token.symbol, token.line, parent = zone)
            declaration = True
            statements = False
        elif token.symbol == gr.OPERATOR:
            function_declaration = True
        elif token.symbol == gr.CLASS:
            class_declaration = True
        
        elif declaration:
            if token.symbol != zone.name:
                zone.declaration.append(token) # It includes ":"
            if token.symbol == ":":
                declaration = False
                statements = True
        elif statements:
            if token.symbol == "{":
                pass
            elif token.symbol == "}":
                closed_zone = zone
                zone = zone.parent
                zone.statements.append(closed_zone) # closed_zone.name added to zone.name
            else:
                zone.statements.append(token)
        
        i += 1
    
    return tree, tokens, errors
        