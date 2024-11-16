from westeros.art import welcome_art
from typing import List

DEV = True


class QuestionType:
    y_n = 'Enter "yes" or "no": '
    mc = "Choose an option: "


class Westeros:
    welcome_msg = (
        "Welcome travelors to Felicia Inn.\n"
        "We hope you are not too weary from your travels as our "
        "King requires immediate service.\n"
    )

    background = """

"""

    def display_welcome(self):
        print(welcome_art)

        print_slow("".join(self.welcome_msg))

    def ask(
        self,
        question: str,
        type: "QuestionType",
        cont: List[str] = None,
        cont_msg: str = None,
    ) -> str:
        print_slow(question + "\n")

        print_slow(type)

        res = input().lower().rstrip()

        if cont:
            while res not in cont:
                print_slow(cont_msg + "\n")
                print_slow(question + "\n")

                print_slow(type)
                res = input().lower().rstrip()

        return res

    def exclaim(msg: str):
        print_slow(msg)

    def run(self):
        self.display_welcome()

        self.ask(
            "Are you ready to begin?",
            QuestionType.y_n,
            ["yes", "y"],
            cont_msg="Incorrect answer. King needs attention now. Lets try again",
        )

        self.exclaim("Great! Lets begin with some background")


def print_slow(msg: str) -> None:
    from time import sleep

    for c in msg:
        print(c, end="", flush=True)
        if not DEV:
            sleep(0.05)
