from decision_tree.step import Step


class ParsingError(Exception):
    pass


def _get_step_by_name(step_name: str, raw_tree: dict, parsed_items: set[str]) -> Step:
    if step_name in parsed_items:
        raise ParsingError(f'Loop detected in raw object. Step {step_name} already parsed.')

    parsed_items.add(step_name)
    return Step(
        text=raw_tree[step_name]['text'],
        options=_parse_options(raw_tree[step_name]['options'], raw_tree, parsed_items)
    )


def _parse_options(options: list[dict], raw_tree: dict, parsed_items: set[str]) -> dict[str, Step]:
    result = {}
    for option in options:
        result[option['text']] = _get_step_by_name(option['link'], raw_tree, parsed_items)
    return result


def parse(raw_obj: dict) -> Step:
    parsed_items = set()
    try:
        raw_tree = raw_obj['tree']
        return _get_step_by_name(raw_tree['ROOT'], raw_tree, parsed_items)
    except KeyError as error:
        raise ParsingError(f'Key {error} not found in raw object.') from error

