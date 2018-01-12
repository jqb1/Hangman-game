from Draw import Draw
from Input import Input
import argparse


def Main():
    print("Hello in a simple hangman game")

    level_parser = argparse.ArgumentParser(description="Choosing level")

    level_parser.add_argument('lvl',default=1, help="1-easy, other-hard , default - easy",type=int)

    arg = level_parser.parse_args()
    if arg.lvl == 1:
        level = "easy"
    else:
        level = "hard"

    Input(level)
    # draw = Draw()

Main()
