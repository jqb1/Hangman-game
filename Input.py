import random
from Draw import Draw


class Input:
    def __init__(self, level):
        self.level = level
        line = self.level_picker(level)
        Draw(line)

    def level_picker(self, level):
        if level == "hard":
            try:
                file = open("hard_words.txt")
                lines = file.read().splitlines()
                line = random.choice(lines)
                return line
            except IOError:
                print("Can't read a hard words file")

        else:
            try:
                file = open("words.txt")
                lines = file.read().splitlines()
                line = random.choice(lines)
                return line
            except IOError:
                print("Cant read words file")
