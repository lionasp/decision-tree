from decision_tree.engines.simple_engine import SimpleEngine, SimpleEngineError


def play_game(engine: SimpleEngine) -> None:
    while True:
        print(f"*** {engine.get_current_step().text} ***")
        if not engine.get_current_step().options:
            break

        print("Options:")
        for option in engine.get_current_step().options:
            print(f"\t{option}")

        decision = input("What do you do? > ")
        try:
            engine.go_next(decision)
        except SimpleEngineError as error:
            print(f"Error: {error}. Try again.")

    print("Game over.")