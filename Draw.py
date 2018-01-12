import os
from Paint import Paint


class Draw:
    word_list = None
    underscore_list = []
    underscore_string=str
    indexes_list = []
    wrong_answer = 0
    guess = bool
    game_over = bool
    paint= Paint()

    def __init__(self, word):
        self.word = word
        self.draw_lines(word)

        self.start_game()

    def draw_lines(self, word):
        print("Zagadnij słowo:")
        self.word_list = list(word)
        word_length = len(self.word_list)
        for i in range(word_length):
            self.underscore_list.append("_")
        underscore_string = " ".join(self.underscore_list)
        print(underscore_string)

    def start_game(self):
        # list of chars to guess
        guess_char_list = self.word_list

        while True:
            input_char = input()
            if input_char in guess_char_list:
                self.guess=True
            else:
                self.guess=False

            # Clearing window
            os.system('cls' if os.name == 'nt' else 'clear')

            for i, char in enumerate(guess_char_list, start=0):
                if char == input_char:
                    self.indexes_list.append(i)
                    # changing guessed char to 0 so it can't be guessed anymore
                    guess_char_list[i] = 0
                    self.underscore_list[i] = input_char

                else:
                    pass
            underscore_string = " ".join(self.underscore_list)
            print(underscore_string)
            self.repaint(self.guess)

    def repaint(self, guess):
        print(guess)
        if guess:
            self.paint.draw(self.wrong_answer)
        else:
            self.wrong_answer += 1
            self.paint.draw(self.wrong_answer)
