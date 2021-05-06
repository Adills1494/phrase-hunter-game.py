# phrase-hunter-game.py
Project Overview:
- Create and run a command line game using only objects and method calls. 
- Was provided with blank class files for character, phrase, game, and a blank file to run the game - app.py
- There are intructions on each section

Requirments to run the game:
- Phrase Hunter only uses the python standard library
- Python 3.7.3

Understand the rules of the game:
- This game will be entirely console/terminal based.
- The player’s goal is to guess all the letters in a hidden, random phrase. A phrase is a group of words.
- At the beginning of the game, the player only sees the number of letters and words in the phrase, represented by an underscore character _ as a placeholder on the screen for a given letter for that phrase.
- The player inputs a guess for a letter in the phrase.
- Once a correct letter is guessed, a player cannot guess that letter again.
- If the guessed letter is in the phrase at least once, the phrase will replace all positions showing the underscore _ with the appropriate letter. All occurrences of that letter are made visible (so if there are 3 A's, all of the A's in the phrase appear at once).
- If the selected letter is not in the phrase, the number missed increases by one.
- The player keeps choosing letters until they reveal all the letters in the phrase, or until they make five incorrect guesses.

To Play the game:
- Clone the repo to your computer
- Run python3 app.py from the root of the cloned folder
