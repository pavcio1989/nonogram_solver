from src.config.config import Config


class Board:
    row_count: int = 0
    column_count: int = 0

    def __init__(self, config: Config):
        self.row_count = config.row_count
        self.column_count = config.column_count

        # Create an empty board
