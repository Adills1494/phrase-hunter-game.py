# Import your Game class
from phrasehuntergame import constants
from phrasehuntergame import Game
# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
if __name__ == '__main__':
    game = Game(constants.PHRASES)
    game.main_loop()
