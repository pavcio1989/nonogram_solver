from src.config.config import Config
from src.entities.block import Block
from src.entities.board import Board


class BaseNonogramSolver:
    solved = False

    def __init__(self, config: Config):
        self.tasks = config.task
        self.board = Board(config=config)

    def solve(self):

        if self.board.check_completeness():
            self.solved = True
