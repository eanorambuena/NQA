def tokenize(lexemas):
    tokens = []
    for i in range(len(lexemas)):
        tokens.append([lexemas[i], i])
    return tokens

def tolist(string):
    arr = []
    for i in string:
        arr.append(i)
    return arr