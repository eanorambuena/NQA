import subprocess, os

def compile(file):
    if os.path.exists(file + ".exe"):
        os.remove(file + ".exe")
    subprocess.call(["g++", "-std=c++17", file + ".cpp" , "-o", file])

def execute(file, *args):
    commands = ["./" + file]
    for i in args:
        commands += [str(i)]
    subprocess.call(commands)

def run(file, *args):
    compile(file)
    execute(file, *args)

compile("core")

# from eggdriver import cpp
# cpp.run("core", "Emma")