import yaml


class YamlReaderError(Exception):
    pass


class YamlReader:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def _read(self) -> str:
        try:
            with open(self.filename, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise YamlReaderError(f'File {self.filename} not found.')
        except yaml.YAMLError as exc:
            raise YamlReaderError(f'Cannot read the file {self.filename}. Error: {exc}.')
