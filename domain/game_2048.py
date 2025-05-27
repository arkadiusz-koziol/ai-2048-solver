# file: domain/game_2048.py
import random
import numpy as np
from domain.value_objects import Board

class Game2048:
    def __init__(self):
        self.board = Board()
        self._add_tile()
        self._add_tile()

    def reset(self) -> Board:
        self.board = Board()
        self._add_tile()
        self._add_tile()
        return self.board

    def step(self, action: int) -> tuple[Board, int, bool]:
        old_board = self.board.copy()
        reward = self._move(action)
        if not old_board.is_equal(self.board):
            self._add_tile()
        done = not self._can_move()
        return self.board, reward, done

    def _add_tile(self):
        empty = self.board.empty_positions()
        if empty:
            y, x = random.choice(empty)
            self.board.set_tile(y, x, 2 if random.random() < 0.9 else 4)

    def _move(self, direction: int) -> int:
        total_reward = 0

        def slide_and_merge(row):
            nonlocal total_reward
            row = row[row != 0]
            new_row = []
            i = 0
            while i < len(row):
                if i + 1 < len(row) and row[i] == row[i + 1]:
                    merged = row[i] * 2
                    new_row.append(merged)
                    total_reward += merged
                    i += 2
                else:
                    new_row.append(row[i])
                    i += 1
            return np.array(new_row + [0] * (self.board.size - len(new_row)))

        self.board.rotate(direction)
        for i in range(self.board.size):
            new_row = slide_and_merge(self.board.get_row(i))
            self.board.set_row(i, new_row)
        self.board.rotate((4 - direction) % 4)

        return total_reward

    def _can_move(self) -> bool:
        grid = self.board.grid
        if np.any(grid == 0):
            return True
        for i in range(self.board.size):
            for j in range(self.board.size - 1):
                if grid[i][j] == grid[i][j + 1] or grid[j][i] == grid[j + 1][i]:
                    return True
        return False
