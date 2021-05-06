class Character:
    # Create an attribute to store the original
    # Create an attribute to store a bool of whether this letter has had a guess tried against it
    def __init__(self, original):
        self.original = original
        if self.original == " ":
            self.was_guessed = True
        else:
            self.was_guessed = False
    
    # Make a single string character name guess as an arg
    # If 
    def check_guess(self, guess):
        self.guess = guess
        if self.guess.lower() == self.original.lower():
            self.was_guessed = True
            
    def __str__(self):
        return "{self.original}".format(self = self)
    
    
