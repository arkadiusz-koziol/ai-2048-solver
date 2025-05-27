import gym
from gym import spaces
import numpy as np
from domain.game_2048 import Game2048

class Simple2048Env(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super().__init__()
        self.game = Game2048()
        self.grid_size = 4
        self.action_space = spaces.Discrete(4)  # 0=Up, 1=Down, 2=Left, 3=Right
        self.observation_space = spaces.Box(
            low=0, high=2**16, shape=(self.grid_size, self.grid_size), dtype=np.int64
        )

    def reset(self):
        board = self.game.reset()
        return board.to_numpy()

    def step(self, action):
        board, reward, done = self.game.step(action)
        return board.to_numpy(), reward, done, {}

    def render(self, mode="human"):
        board = self.game.board.grid
        print("\n".join(["\t".join(map(str, row)) for row in board]))
        print(f"Max tile: {self.game.board.max_tile()}\n")
