import subprocess, os

#from eggdriver import cpp
# cpp.compile("core", "Emma")

def cpp_compile(file):
    if os.path.exists(file + ".exe"):
        os.remove(file + ".exe")
    subprocess.call(["g++", "-std=c++17", file + ".cpp" , "-o", file])

cpp_compile("nqa\\py_compiler")
