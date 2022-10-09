from decision_tree.engines.simple_engine import SimpleEngine
from decision_tree.parsers.raw_object_parser import parse
from decision_tree.readers.yaml_reader import YamlReader
from decision_tree.step import Step


def make_tree(filename: str) -> Step:
    raw_data = YamlReader(filename).read()
    return parse(raw_data)


if __name__ == '__main__':
    tree = make_tree("config.yaml")
    engine = SimpleEngine(tree)
    while True:
        print(f'*** {engine.get_current_step().text} ***')
        if not engine.get_current_step().options:
            break

        print('Options:')
        for option in engine.get_current_step().options:
            print(f'\t{option}')

        decision = input('What do you do? > ')
        engine.go_next(decision)
    print('Game over.')
