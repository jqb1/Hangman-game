import os
from Paint import Paint


class Draw:
    word_list = None
    underscore_list = []
    underscore_string = str
    wrong_answer = 0
    game_won = False
    guess = bool
    game_over = bool
    paint = Paint()
    win_stage = 9

    game_over = False

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

        while not self.game_over:
            input_char = input()
            if input_char in guess_char_list:
                self.guess = True
            else:
                self.guess = False

            self.clear_window()

            for i, char in enumerate(guess_char_list, start=0):
                if char == input_char:
                    # changing guessed char to 0 so it can't be guessed anymore
                    guess_char_list[i] = 0
                    self.underscore_list[i] = input_char
                    if '_' not in self.underscore_list:
                        self.game_won = True
                else:
                    pass

            underscore_string = " ".join(self.underscore_list)
            print(underscore_string)
            # painting man
            self.repaint(self.guess)

    def repaint(self, guess):
        print(guess)
        if guess:
            self.paint.draw(self.wrong_answer)
            if self.game_won:
                self.paint.draw(self.win_stage)
                self.game_over = True
        else:
            self.wrong_answer += 1
            self.paint.draw(self.wrong_answer)
            if self.wrong_answer >= 8:
                self.game_over = True

    def clear_window(self):
        # Clearing window
        os.system('cls' if os.name == 'nt' else 'clear')
