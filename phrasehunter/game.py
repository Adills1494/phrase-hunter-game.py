import os
import random
import sys



from .phrase import Phrase
from .character import Character
from .constants import phrases

class Game:
    def __init__(self, phrases):
        self.guesses = []
        self.phrases = [Phrase(phrase) for phrase in phrases.copy()]
        self.current_phrase = random.choice(self.phrases)
        self.lives = 5

    def get_guess(self):
        guess = ""
        while not guess:
            try:
                player_guess = input("Please guess a letter:  ")
                if player_guess.isdigit():
                    print("Sorry that is not a valid guess.")
                    continue
                elif len(player_guess) > 1:
                    print("Sorry that is not a valid guess.")
                    continue
                elif not player_guess.isalpha():
                    print("Sorry that is not a valid guess.")
                    continue
                elif player_guess.lower() in self.guesses:
                    print("OOPS! You have already guessed that letter! Please try again!")
                    continue
                else:
                    guess = player_guess
            except KeyboardInterrupt:
                self.clear_screen()
                self.welcome()
                print("Nice try, but you can't leave without finishing the game.")
        self.guesses.append(guess.lower())
        if guess.lower() not in [letter.original.lower() for letter in self.current_phrase]:
            self.lives -= 1
        return guess.lower()
    
    def game_won(self):
        if self.current_phrase.all_guessed():
            self.clear_screen()
            self.welcome()
            print("Congratulations!! You won the game!!")
            print()
            return True
        return False
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def welcome(self):
        welcome = "~~~~~~Tony's Phrase Hunter Game~~~~~~"
        print("=" * len(welcome))
        print(welcome)
        print("=" * len(welcome))
        print()
        print("Lives Left: {}".format(self.lives))
        print("Letters Guessed: {guesses}\n".format(guesses = self.guesses))
        print("Hint: {}".format(self.current_phrase.hint))
        print()
        self.current_phrase.display_phrase()

    def play_again(self, answer):
        self.answer = answer
        if self.answer.lower() == 'y':
            return Game(phrases).main_loop()
        else:
            self.clear_screen()
            self.welcome()
            print("\nThank you for playing! Have a great day!\n")
            sys.exit()

    def main_loop(self):
        while not self.game_won():
            self.clear_screen()
            self.welcome()
            print()
            player_guess = self.get_guess()
            for item in self.current_phrase:
                item.check_guess(player_guess)
            if self.lives == 0:
                self.clear_screen()
                self.welcome()
                self.play_again(input("Oh no! You ran out of lives. Would you like to play again? Y/n  "))
                print()
                break
        self.play_again(input("Would you like to play again? Y/n  "))
