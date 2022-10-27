from decision_tree.engines.simple_engine import SimpleEngine
from decision_tree.parsers.raw_object_parser import SimpleParser
from decision_tree.readers.yaml_reader import YamlReader
from decision_tree.step import Step
from examples.utils import play_game


def make_tree(filename: str) -> Step:
    raw_data = YamlReader(filename).read()
    return SimpleParser(raw_data).parse()


if __name__ == "__main__":
    tree = make_tree("config.yaml")
    engine = SimpleEngine(tree)
    play_game(engine)
