import nqa.grammar as gr
from nqa.error import *

class Zone():
    def __init__(self, name: str, line: int, type: str = "auto", parent = None):
        self.name = name
        self.line = line
        self.parent = parent

        if type == "auto":
            if name == gr.IF:
                self.type = "conditional"
            elif name in [gr.WHILE, gr.FOR]:
                self.type = "loop"
            elif name == "root":
                self.type = "root"
            else:
                ZoneError(line, f"Unknown zone type for zone '{name}'")
        else:
            self.type = type
        self.declaration = []
        self.statements = []

    def display(self, depth = 0):
        print(depth * "\t" + f"{self.name} ({self.type})")
        for d in self.declaration:
            if type(d) == Zone:
                d.display(depth + 1)
            else:
                print((depth + 1) * "\t" + f"{d}")
        for s in self.statements:
            if type(s) == Zone:
                s.display(depth + 1)
            else:
                print((depth + 1) * "\t" + f"{s}")