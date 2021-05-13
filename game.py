# Create your Game class logic in here.
import random
import sys
import os


from .constants import PHRASES
from .phrase import Phrase
from .character import Character

class Game:
    def __init__(self, phrases):
        self.guesses = []
        self.phrases = [Phrase(phrase) for phrase in phrases.copy()]
        self.current_phrase = random.choice(self.phrases)
        self.lives = 6
        
    def get_guess(self):
        guess = ""
        while not guess:
            try:
                player_guess = input("\n Please guess a Letter:  ")
                if player_guess.isdigit():
                    print("\n That is not a valid guess. Please guess a Letter.")
                    continue
                elif len(player_guess > 1:
                    print("\n That is not a valid guess. Please guess one Letter.")
                    continue
                elif not player_guess.isalpha():
                    print("\n That is not a valid guess.")
                    continue
                elif player_guess.lower() in self.guess:
                    print("\n You have already guessed that letter. Please try again.")
                    continue
                else:
                     guess = player_guess
            except KeyboardInterrupt:
                self.clear_screen()
                self.welcome()
                print("\n Nice try, but you can't leave without finishing the game.")
        self.guesses.append(guess.lower())
        if guess.lower() not in [letter.original.lower() for letter in self.current_phrase]:
            self.lives -= 1
        return guess.lower()
    
    def game_won(self):
        if self.current_phrase.all_guessed():
            self.clear_screen()
            self.welcome()
            print("\n Congratulations! You won the game!!")
            print()
            return True
        return False
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def welcome(self):
        welcome = "~~~~~ Tony's Phrase Hunter ~~~~~"
        print("=" * len(welcome))
        print(welcome)
        print("=" * len(welcome))
        print()
        print("\n Lives Left: {}".format(self.lives))
        print("\n Letters Guessed: {guesses}\n".format(guesses = self.guesses))
        print("\n Hint: {}".format(self.current_phrase.hint))
        print()
        self.current_phrase.display_phrase()

    def play_again(self, answer):
        self.answer = answer
        if self.answer.lower() == 'y':
            return Game(PHRASES).main_loop()
        else:
            self.clear_screen()
            self.welcome()
            print("\nThank you for playing Tony's Phrase Hunter. Have a great day!\n")
            sys.exit()

    def main_loop(self):
        # While game isn't won
        while not self.game_won():
            self.clear_screen()
            self.welcome()
            print()
            # prompt the user for a guess
            player_guess = self.get_guess()
            # check the guess against phrase
            for item in self.current_phrase:
                item.check_guess(player_guess)
            if self.lives == 0:
                self.clear_screen()
                self.welcome()
                self.play_again(input("\n Oh no! You ran out of lives. Would you like to play again? Y/n  "))
                print()
                break
        self.play_again(input("\n Would you like to play again? Y/n  "))
                         
                         
