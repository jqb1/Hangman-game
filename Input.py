import random
from Draw import Draw


class Input:
    def __init__(self, level,file_name):
        self.level = level
        if not file_name:
            line = self.level_picker(level)
        else:
            line=self.file_picker(file_name)

        Draw(line)

    def level_picker(self, level):
        if level == "hard":
            line = self.pick_word("hard_words.txt")
        else:
            line = self.pick_word("words.txt")

        return line

    def file_picker(self, name):
        line = self.pick_word(name)
        return line

    def pick_word(self, name):
        try:
            file = open(name)
            lines = file.read().splitlines()
            line = random.choice(lines)
            return line
        except IOError:
            print("Can't open file!")
