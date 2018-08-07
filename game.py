from models import Board
from utils import get_random_placement
from interface import GameInterface
from constants import BOMB


class Game:
    def __init__(self, size, num_bomb):
        self.board = Board(size, size)
        self.bombs = get_random_placement(size, size, num_bomb)
        self.has_revealed_bomb = False
        self.init_bombs()

    def init_bombs(self):
        for bomb_x, bomb_y in self.bombs:
            self.board.set_cell(bomb_x, bomb_y, BOMB)

    def reveal_bombs(self):
        for bomb_x, bomb_y in self.bombs:
            self.board.reveal_cell(bomb_x, bomb_y)

    def hide_bombs(self):
        for bomb_x, bomb_y in self.bombs:
            self.board.hide_cell(bomb_x, bomb_y)

    def print_board(self):
        GameInterface.print_board(self.board)

    def turn(self):
        self.print_board()
        x, y = GameInterface.inquire_turn()
        is_bomb_revealed = self.board.reveal_cell(x, y)
        if is_bomb_revealed:
            self.has_revealed_bomb = True

    def has_lost(self):
        return self.has_revealed_bomb

    def has_won(self):
        cells_revealed_state = [
            cell.is_revealed for cell in self.board.cells.values() if not cell.is_bomb()
        ]
        return not self.has_lost() and all(cells_revealed_state)
