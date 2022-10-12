from decision_tree.step import Step


class ParsingError(Exception):
    pass


def _get_step_by_name(step_name: str, raw_tree: dict, parsed_items: dict[str, Step]) -> Step:
    if step_name in parsed_items:
        return parsed_items[step_name]

    parsed_step = Step(
        text=raw_tree[step_name]['text'],
        options=_parse_options(raw_tree[step_name].get('options', []), raw_tree, parsed_items)
    )
    parsed_items[step_name] = parsed_step
    return parsed_step


def _parse_options(options: list[dict], raw_tree: dict, parsed_items: dict[str, Step]) -> dict[str, Step]:
    result = {}
    for option in options:
        result[option['text']] = _get_step_by_name(option['link'], raw_tree, parsed_items)
    return result


def parse(raw_obj: dict) -> Step:
    parsed_items = {}
    try:
        raw_tree = {item['name']: item for item in raw_obj['tree']}
        return _get_step_by_name('ROOT', raw_tree, parsed_items)
    except KeyError as error:
        raise ParsingError(f'Key {error} not found in raw object.') from error

