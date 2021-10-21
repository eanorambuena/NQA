_FILENOTFOUNT = "File not fount on {}"

def read_module(path):
    src = None
    try:
        with open(path, mode='r', encoding='utf-8') as fin:
            lines = fin.readlines()
        src = '\n'.join([str(line) for line in lines])
    except FileNotFoundError:
        print('\n[Error] ' + _FILENOTFOUNT.format(path) + '\n')
    return src

