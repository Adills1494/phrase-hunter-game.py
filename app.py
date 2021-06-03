from phrasehuntergame.game import Game

if __name__ == '__main__':
    try:
        game = Game()
        game.start()
    except EOFError:
        print('\n\nSee yah Later! ')
        quit()
    except KeyboardInterrupt:
        print('\n\nSee yah Later! ')
        quit()
