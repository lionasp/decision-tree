from step import Step


class SimpleEngine:
    def __init__(self, tree: Step) -> None:
        self._tree = tree

    def go_next(self, decision: str) -> None:
        next_step = self._tree.options.get(decision)
        if next_step is None:
            print('Invalid decision.')
        else:
            self._tree = next_step

    def get_current_step(self) -> Step:
        return self._tree
