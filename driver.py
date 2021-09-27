import subprocess
file = "core"
subprocess.run(["g++", "-std=c++17", file + ".cpp", "-o", file])