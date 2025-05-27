import numpy as np

class Board:
    def __init__(self, size: int = 4):
        self.size = size
        self.grid = np.zeros((self.size, self.size), dtype=int)

    def copy(self) -> 'Board':
        new_board = Board(self.size)
        new_board.grid = self.grid.copy()
        return new_board

    def max_tile(self) -> int:
        return int(np.max(self.grid))

    def empty_positions(self):
        return list(zip(*np.where(self.grid == 0)))

    def set_tile(self, y: int, x: int, value: int):
        self.grid[y][x] = value

    def rotate(self, k: int = 1):
        self.grid = np.rot90(self.grid, k)

    def get_row(self, idx: int):
        return self.grid[idx]

    def set_row(self, idx: int, row):
        self.grid[idx] = row

    def to_numpy(self):
        return self.grid.copy()

    def is_equal(self, other: 'Board') -> bool:
        return np.array_equal(self.grid, other.grid)
