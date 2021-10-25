import sys
from nqa.routines import routine

argv = sys.argv[1:]
argc = len(argv)

if argc < 1:
    print("Error")

command = argv[0];

if command == "compile":
    name = argv[1]
    routine(name)

elif command == "help":
    print("Welcome")

