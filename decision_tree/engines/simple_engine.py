from decision_tree.step import Step


class SimpleEngineError(Exception):
    pass


class SimpleEngine:
    def __init__(self, tree: Step) -> None:
        self._tree = tree

    def go_next(self, decision: str) -> None:
        next_step = self._tree.options.get(decision)
        if next_step is None:
            raise SimpleEngineError(f"Invalid decision.")
        self._tree = next_step

    def get_current_step(self) -> Step:
        return self._tree
