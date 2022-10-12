from decision_tree.engines.simple_engine import SimpleEngine
from decision_tree.step import Step


def make_tree() -> Step:
    return Step(
        text="You are in a dark room. There is a door to your left and right, which one do you take?",
        options={
            "left": Step(
                text="You opened the left door. However, it was a trap door and you fell into a pit of snakes. "
                "You died."
            ),
            "right": Step(
                text="You opened the right door. You come in and see a strange painting on the wall. Besides this, "
                "you can see something small in the far corner.",
                options={
                    "Check the painting": Step(
                        "You see three rectangles of different sizes",
                        options={
                            "Check the small rectangle": Step("TBD"),
                            "Check the medium rectangle": Step("TBD"),
                            "Check the large rectangle": Step("TBD"),
                        },
                    ),
                    "Check the corner": Step("TBD"),
                },
            ),
            "do nothing": Step("The monster comes and eats you. You died."),
        },
    )


if __name__ == "__main__":
    tree = make_tree()
    engine = SimpleEngine(tree)
    while True:
        print(f"*** {engine.get_current_step().text} ***")
        if not engine.get_current_step().options:
            break

        print("Options:")
        for option in engine.get_current_step().options:
            print(f"\t{option}")

        decision = input("What do you do? > ")
        engine.go_next(decision)
    print("Game over.")
