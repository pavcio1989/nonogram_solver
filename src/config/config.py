import yaml

from src.entities.task import Task
from src.entities.block import Block


class Config:
    def __init__(self):
        self.input = None

        # Data YAML
        with open('src/config/data.yml', 'r') as data_file:
            self.input = yaml.safe_load(data_file)

        self.input_file_path = self.input['data']['input_file']

        self.row_count = None
        self.column_count = None

        row_task = []
        column_task = []

        with open(self.input_file_path) as input_file:
            flag = None
            i_line = 0
            i_elem = 0

            for line in input_file:
                if line.strip() == "Rows":
                    flag = 0
                    i_line = 0
                    i_elem = 0
                    continue
                if line.strip() == "Columns":
                    flag = 1
                    i_line = 0
                    i_elem = 0
                    continue
                if flag is not None:
                    task = []
                    i_line += 1
                    _tasks = line.split(',')
                    for _task in _tasks:
                        i_elem += 1
                        task.append(Block(_task, i_line, i_elem))
                    i_elem = 0
                    if flag == 0:
                        row_task.append(task)
                    elif flag == 1:
                        column_task.append(task)

        self.task = Task(row_task, column_task)


