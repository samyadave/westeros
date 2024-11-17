from westeros.art import welcome_art
from typing import List

from westeros.story import Misc, Task
from westeros.utils import QuestionType, print_sep, print_slow


class Westeros:
    def display_welcome(self):
        print(welcome_art)

        print_slow("".join(Misc.welcome_msg))

    def ask(
        self,
        question: str,
        type: "QuestionType",
        cont: List[str] = None,
        cont_msg: List[str] = None,
        options: List[str] = None,
        pop: bool = False,
        reprompt: bool = True,
    ) -> str:
        print_slow(question + "\n")

        if options:
            options_dict = {f"{i + 1}": msg for i, msg in enumerate(options)}
            print_slow(f"{i}: {msg}\n" for i, msg in options_dict.items())

        print_slow(type)

        res = input().lower().rstrip()

        print_sep(2)

        while cont and not res in cont:
            idx = int(res) - 1
            if pop:
                options_dict.pop(res)
            print_slow(cont_msg[idx if pop else 0] + "\n")
            if reprompt:
                print_slow(question + "\n")
            if options:
                print_slow(f"{i}: {msg}\n" for i, msg in options_dict.items())
            print_slow(type)
            res = input().lower().rstrip()
            print_sep(2)

        return res

    def exclaim(self, msg: str):
        print_slow(msg)

    def run(self):
        print_sep(50)
        self.display_welcome()

        self.ask(
            "Are you ready to begin?",
            QuestionType.y_n,
            ["yes", "y"],
            cont_msg=["Incorrect answer. King needs attention now. Lets try again"],
        )

        self.exclaim("Great! Lets begin with some background")
        self.exclaim(Misc.background)
        self.exclaim(Task.task_1)

        self.ask(
            "Let us know when you have finished your task.",
            QuestionType.mc,
            options=["We need more time", "Somethings off..."],
            cont=["2"],
            cont_msg=["Come back once you have finished your task."],
        )

        self.ask(
            "What is it?",
            QuestionType.mc,
            options=[
                "We couldn't help it and we some of the royal tp!",
                "There was some toilet paper missing when we found it!",
            ],
            cont=["2"],
            cont_msg=[
                "Are you so proud of your insolence that you'd exclaim it to the king! If there's anything of importance state it now!",
                "",
            ],
            pop=True,
        )

        self.exclaim(Task.task_2)

        self.ask(
            question="Have you completed your task?",
            type=QuestionType.mc,
            options=[
                "We found something!",
                "We need more time.",
            ],
            cont=["1"],
            cont_msg=[
                "Return to the garden at once! Come back with evidence.",
            ],
        )

        self.ask(
            "What did you find?",
            QuestionType.mc,
            options=[
                "One of us must have farted passing by the garden on the way to the castle",
                "The Eastern fence shows signs of deterioration, that's where they must enter.",
                "There appears to be some hazardly waste in the shape of poo!",
            ],
            cont=["3"],
            cont_msg=[
                "Ha! Certainly you jest! Otherwise that would be treason and I shall have to jail you!",
                "Ah! Indeed this is a good finding! How about the smell?",
                "",
            ],
            pop=True,
            reprompt=False,
        )

        self.exclaim(Task.task_3)

        self.ask(
            question="Have you completed your task?",
            type=QuestionType.mc,
            options=[
                "We found something!",
                "We need more time.",
            ],
            cont=["1"],
            cont_msg=[
                "Return to the garden at once! Come back with evidence.",
            ],
        )

        self.ask(
            "What have you found?",
            QuestionType.mc,
            options=[
                "There was some rotten pizza there! It was definitely rotten and we definitely did not eat it and try to cover it up by saying it's rotten!",
                "We found traces of bird feathers. Perhaps the smell is linked to their diet as well.",
                "We found this golden replica of the kingdom's decorative tree!",
            ],
            cont=["3"],
            cont_msg=[
                "You dare say that pizza was left out to rot? Who would commit such a heinous act of leaving a delicacy out in the wild!",
                "Hmmm...\n Interesting. This may be so however I am sure they have been eating birds for many moons. Find anything else?",
                "",
            ],
            pop=True,
            reprompt=False,
        )

        self.exclaim(Task.task_4)

        self.ask(
            question="Have you completed your task?",
            type=QuestionType.mc,
            options=[
                "We found something!",
                "We need more time.",
            ],
            cont=["1"],
            cont_msg=[
                "Return to the garden at once! Come back with evidence.",
            ],
        )

        self.ask(
            "What have you found?",
            QuestionType.mc,
            options=[
                "Perhaps we found more pizza, perhaps we did not! Maybe even a burger!",
                "A great egg!",
                "We found lights on the tree! So strange, they even flash sometimes!",
            ],
            cont=["2"],
            cont_msg=[
                "Enough! The king shall jail you now!\nHmmm...\nWell perhaps after these pressing matters have been attended to.",
                "",
                "Silly subjects, of course the kingdoms grand tree has lights!",
            ],
            pop=True,
            reprompt=False,
        )

        self.exclaim(Task.task_5)

        self.ask(
            question="Have you completed your task?",
            type=QuestionType.mc,
            options=[
                "We found something!",
                "We need more time.",
            ],
            cont=["1"],
            cont_msg=[
                "Return to the garden at once! Come back with evidence.",
            ],
        )

        self.ask(
            "What have you found?",
            QuestionType.mc,
            options=[
                "We found the culprit! A green dragon was hoarding your gold!",
                "Macaroni!",
            ],
            cont=["1"],
            cont_msg=[
                "",
                "Hmm, you must have found something of interest? What else?",
            ],
            pop=True,
            reprompt=False,
        )

        self.exclaim(Misc.congrats_msg)

        while True:
            ...
