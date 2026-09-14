import numpy as np

from src.config.config import Config
from src.entities.block import Block
from src.entities.cell import CellState


class Board:
    row_count: int = 0
    column_count: int = 0

    grid = None

    def __init__(self, config: Config):
        self.row_count = config.row_count
        self.column_count = config.column_count

        self.grid = [
            [CellState.UNKNOWN for _ in range(self.row_count)]
            for _ in range(self.column_count)
        ]

    def set_cell(self, r, c, state):
        self.grid[r][c] = state

    def get_row(self, r):
        return self.grid[r]

    def get_col(self, c):
        return [row[c] for row in self.grid]

    def check_completeness(self):
        for row in self.grid:
            for cell in i:
                if cell == CellState.UNKNOWN:
                    return False
        return True
