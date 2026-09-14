import sys
import logging

# Add content root to your path
sys.path.append('C:/Users/pawel/Desktop/Learning/nonogram_solver')

if __name__ == "__main__":
    from src.config.config import Config
    from src.loggers.nonogram_logger import NonogramLogger
    # from src.pipelines.pipeline import Pipeline

    logger = NonogramLogger(__name__, level=logging.INFO)

    config = Config()

    print(f"Task: {config.task}")

    # pipeline = Pipeline(config)

    # pipeline.run()
