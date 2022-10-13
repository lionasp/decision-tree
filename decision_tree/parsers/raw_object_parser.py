from decision_tree.step import Step


class ParsingError(Exception):
    pass


class SimpleParser:
    def __init__(self, raw_data: dict) -> None:
        self._parsed_items: dict[str, Step] = {}
        try:
            self._raw_tree = {item["name"]: item for item in raw_data["tree"]}
        except KeyError:
            raise ParsingError("Invalid data format.")

    def _get_step_by_name(self, step_name: str) -> Step:
        if step_name in self._parsed_items:
            return self._parsed_items[step_name]

        parsed_step = Step(
            text=self._raw_tree[step_name]["text"],
            options=self._parse_options(self._raw_tree[step_name].get("options", [])),
        )
        self._parsed_items[step_name] = parsed_step
        return parsed_step

    def _parse_options(self, options: list[dict]) -> dict[str, Step]:
        return {
            option["text"]: self._get_step_by_name(option["step"]) for option in options
        }

    def parse(self) -> Step:
        try:
            return self._get_step_by_name("ROOT")
        except KeyError as error:
            raise ParsingError(f"Key {error} not found in raw object.") from error
