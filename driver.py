import subprocess, os, nqs

#from eggdriver import cpp
# cpp.compile("core", "Emma")

def compile(file):
    if os.path.exists(file + ".exe"):
        os.remove(file + ".exe")
    subprocess.call(["g++", "-std=c++17", file + ".cpp" , "-o", file])

#compile("nqs")

