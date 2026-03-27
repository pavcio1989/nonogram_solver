import logging

from src import solvers
from src.config.config import Config
from src.pipelines.names import MSTSolver
from src.utils.visuals import visualize_minimum_spanning_tree


logger = logging.getLogger('nonogram')


class Pipeline:
    def __init__(self, config: Config):
        self.config = config

    def run(self):
        pass
