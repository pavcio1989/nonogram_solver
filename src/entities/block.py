class Block:
    id: tuple
    value: int
    start: int = 0
    end: int = 0
    completed: bool = False

    minimum_start: int = 0
    maximum_end: int = 0
    current_length: int = 0

    def __init__(self, value, id_line, id_elem):
        self.value = value
        self.id = (id_line, id_elem)

    def complete_block(self):
        self.completed = True

    def check_if_completed(self):
        if self.current_length == self.value:
            self.complete_block()

    def __str__(self):
        return f"Block id: {self.id} value {self.value}\n"
