import yaml


class Config:
    def __init__(self):
        self.input = None

        # Data YAML
        with open('src/config/data.yml', 'r') as data_file:
            self.input = yaml.safe_load(data_file)

        self.input_file_path = self.input['data']['input_file']

        self.row_count = None
        self.column_count = None
