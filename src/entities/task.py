from src.entities.block import Block


class Task:
    row_wise: list[list[Block]]
    column_wise: list[list[Block]]

    def __init__(self, row_task: list, column_task: list):
        self.row_wise = row_task
        self.column_wise = column_task

    def __str__(self):
        response = "Task row-wise: \n"
        for x in self.row_wise:
            for y in x:
                response = response + str(y)
            response = response + "\n"

        response = response + "Task column-wise: \n"
        for x in self.column_wise:
            for y in x:
                response = response + str(y)
            response = response + "\n"

        return response
