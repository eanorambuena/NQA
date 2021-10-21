import datetime
import subprocess

now = "2021"

def routine(name):
    f = open(name + ".eggroutine")
    content = f.read()
    f.close()
    lines = content.split("\n")
    text = ""
    indents = []
    for line in lines:
        i, indent = interpretate(line)
        text += antiSplit(indents) + i
        if indent < 0:
            try:
                indents = indents[:-1 + indent]
            except:
                pass
        elif indent > 0:
            [indents.append("\t") for i in range(indent)]
    f = open(name + ".eggroutine.py", "w")
    f.write(text)
    f.close()
    subprocess.call(["py", name + ".eggroutine.py"])

def interpretate(line):
    c = line.split()
    w = c[0]
    if w == "com": # commentary
        result = "#"
        for i in c[1:]:
            result += " " + i
        return (result + "\n", 0)
    elif w == "imp": # import
        result = "import"
        for i in c[1:]:
            result += " " + i
        return (result + "\n", 0)
    elif w == "var":
        return (f"{c[1]} = {c[2]}({antiSplit(c[3:])})\n", 0)
    elif w == "def": # def
        result = f"def {c[1]}("
        for i in range(2, len(c)):
            result += c[i]
            if i != len(c) - 1:
                result += ", "
        return (result + "):\n", 1)
    elif w == "ret": # return
        return (f"return {antiSplit(c[1:])}\n", 0)
    elif w == "end": # end
        return ("\n", -1)
    elif w == "iff": # if
        return (f"if {antiSplit(c[1:])}:\n", 1)
    elif w == "els": # else
        return ("else:\n", 1)
    elif w == "whi": # while
        return (f"while {antiSplit(c[1:])}:\n", 1)
    elif w == "for": # for
        return (f"for {c[1]} in {antiSplit(c[2:])}:\n", 1)
    elif w == "inp": # input
        return (f"{c[1]} = input({antiSplit(c[2:])})\n", 0)
    elif w == "out": # output
        return (f"print({antiSplit(c[1:])})\n", 0)
    elif w == "asf": # asign following
        sep = ","
        return (f"{c[1]} = {c[2]}({antiSplit(c[3:], sep)})\n", 0)
    elif w == "sto": # store it
        f = open(".eggstorage", "a")
        f.write(antiSplit(c[1:] + [now]) + "\n")
        f.close()
        return ("", 0)
    elif w == "use": # import from storage
        f = open(".eggstorage", "r")
        text = f.read()
        f.close()
        lines = text.split("\n")
        result = ""
        for line in lines:
            l = line.split()
            try:
                if c[1] == l[1]:
                    result = f"{l[1]} = {l[2]}({antiSplit(l[3:-1])})\n"
            except:
                pass
        return (result, 0)
    else:
        return ("", 0)

def antiSplit(L, sep = ""):
    sum = ""
    for i in range(len(L)):
        if i != 0:
            sum += " "
        sum += L[i]
        if i != len(L) - 1:
            sum += sep
    return sum
