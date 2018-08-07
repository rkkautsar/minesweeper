from constants import EIGHT_DIR_MODIFIER, BOMB, EMPTY


class Cell:
    def __init__(self, value=0):
        self.value = value
        self.is_revealed = False

    def is_bomb(self):
        return self.value == BOMB

    def reveal(self):
        self.is_revealed = True

    def hide(self):
        self.is_revealed = False

    def __str__(self):
        if not self.is_revealed:
            return "_"
        if self.is_bomb():
            return "*"
        return str(self.value)


class Board:
    def __init__(self, height, width):
        self.cells = {}
        self.height = height
        self.width = width

    def __is_out_of_bound(self, x, y):
        return x < 0 or x >= self.height or y < 0 or y >= self.width

    def get_cell(self, x, y):
        if self.__is_out_of_bound(x, y):
            return None

        if (x, y) not in self.cells:
            self.cells[x, y] = Cell()

        return self.cells[x, y]

    def set_cell(self, x, y, value):
        if (x, y) not in self.cells:
            self.cells[x, y] = Cell(value=value)
        else:
            self.cells[x, y].value = value

        if value == BOMB:
            for neighbor_x, neighbor_y in self.get_neighbors(x, y):
                neighbor = self.get_cell(neighbor_x, neighbor_y)
                neighbor.value += 1

    def reveal_cell(self, x, y):
        cell = self.get_cell(x, y)
        cell.reveal()

        if cell.value == EMPTY:
            revealed = set()
            self.__inner_reveal(x, y, revealed)

        return cell.is_bomb()

    def __inner_reveal(self, x, y, revealed):
        cell = self.get_cell(x, y)
        cell.reveal()
        revealed.add((x, y))

        if cell.value == EMPTY:
            for neighbor_x, neighbor_y in self.get_neighbors(x, y):
                if (neighbor_x, neighbor_y) not in revealed:
                    self.__inner_reveal(neighbor_x, neighbor_y, revealed)

    def hide_cell(self, x, y):
        cell = self.get_cell(x, y)
        cell.hide()

    def get_neighbors(self, x, y):
        all_possible_neighbor = [
            (x + mod_x, y + mod_y) for (mod_x, mod_y) in EIGHT_DIR_MODIFIER
        ]
        return [
            (x, y)
            for (x, y) in all_possible_neighbor
            if self.get_cell(x, y) is not None and not self.get_cell(x, y).is_bomb()
        ]
