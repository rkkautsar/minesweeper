from game import Game
from interface import GameInterface

if __name__ == "__main__":
    print("""

                     dP                           dP
                     88                           88
                     88d888b. .d8888b. 88d8b.d8b. 88d888b.
                     88'  `88 88'  `88 88'`88'`88 88'  `88
                     88.  .88 88.  .88 88  88  88 88.  .88
                     88Y8888' `88888P' dP  dP  dP 88Y8888'




       .d8888b. dP  dP  dP .d8888b. .d8888b. 88d888b. .d8888b. 88d888b.
       Y8ooooo. 88  88  88 88ooood8 88ooood8 88'  `88 88ooood8 88'  `88
             88 88.88b.88' 88.  ... 88.  ... 88.  .88 88.  ... 88
       `88888P' 8888P Y8P  `88888P' `88888P' 88Y888P' `88888P' dP
                                             88
                                             dP

    """)

    board_size, num_bomb = GameInterface.inquire_game_properties()
    game = Game(board_size, num_bomb)

    # # Uncomment to cheat
    # game.reveal_bombs()
    # game.print_board()
    # game.hide_bombs()

    turn = 1
    while not (game.has_won() or game.has_lost()):
        print(f"[ Turn #{turn} ]")
        game.turn()
        turn += 1

    if game.has_won():
        print("Selamat!")
    else:
        game.reveal_bombs()
        print("Coba lagi :(")

    game.print_board()
