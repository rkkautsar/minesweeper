class GameInterface:
    @staticmethod
    def print_board(board):
        for row in range(board.height):
            row_str = " ".join(
                [str(board.get_cell(row, col)) for col in range(board.width)]
            )
            print(row_str)
        print()

    @staticmethod
    def __inquire(message):
        print(f"{message}:")
        answer = input("> ")
        return answer

    @staticmethod
    def inquire_turn():
        coordinate = GameInterface.__inquire("Masukkan koordinat dalam format (x,y)")
        x, y = map(int, coordinate.split(","))
        return (x, y)

    @staticmethod
    def inquire_game_properties():
        board_size = GameInterface.__inquire("Masukkan besar board (n)")
        num_bomb = GameInterface.__inquire("Masukkan banyak bomb (b)")
        return (int(board_size), int(num_bomb))
