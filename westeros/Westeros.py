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

    background = """\n\nThe kingdom of Felicia has been thrown into disarray by a cunning band of criminals known as The Shadowpaws Syndicate (SPS).
These rascals, led by four raccoons, a sneaky possum, and three nimble cats, have 
raided the royal granary, stolen precious gems from the treasury, and even snuck 
into the kitchens to pilfer the King's favorite pies! Their antics have left the 
kingdom on edge, and it's up to you to investigate and find our bandits!\n\n"""

    task_1 = """\n
A grave concern has arisen from the castle's residents! They speak of a foul and ominous stink wafting from the King's garden (AKA backyard).  
Could it be the work of our mischievous bandits, or perhaps something far more sinister?  
The King implores you to investigate this unsavory matter and restore a breath of fresh air to his beloved domain! 
        
Before we embark on our quest, a matter of royal urgency must be attended to.  
A grand shipment of the finest silken scrolls—known in simpler terms as toilet paper—has arrived at the castle gates.  
The King requests your aid in unloading this precious cargo and delivering a portion to his private chambers.  
Do not tarry, for the King's comfort is of utmost importance!\n\n"""

    task_2 = """\n\n
Hmmm... Missing?

It must be the dastardly SPS! I am certain of it! Such vile cruelty knows no bounds.  
Make haste, brave traveler, and venture to the King's grand garden—known to some as the backyard.  
The foul stench is surely their doing, and it demands swift action. Find how they broke in! 
Investigate the source of this odious offense and return posthaste!\n\n
"""

    task_3 = """\n\n
Poop, you say? By the King's crown, even the foulest of creatures could not conjure waste of such hideous stench!  
The Shadowpaws Syndicate has plagued our kingdom for years, yet never have their misdeeds led to such an overwhelming outcry. Why now?  

My loyal subjects, the truth must be uncovered! Venture into the garden with haste and investigate what the SPS may have feasted upon.  
Search the trees, plants, and all manner of foliage for anything unusual.\n\n"""

    task_4 = """\n\n
Tree you say? Perhaps the SPS do not know what is food and what is not. Eating this gold
has caused them to poop themselves silly! 

Yet still...   A tree?

Take to royal tree and look around for anything of interest. Report back quick!
\n\n"""

    task_5 = """\n\n
A faberge egg from the royal treasury (AKA pantry)! How could it have been breached!

Whispers from the Kingsguard speak of a green creature lurking near the treasury.

Go to the treasury at once and see what you find!
\n\n"""

    congrats_msg = """\n\n
A green dragon, you say? Preposterous! Surely, this reeks of the Shadowpaws Syndicate's handiwork.  
Their cunning ways and expanding network of accomplices grow bolder by the day!  

The King rises from his throne, his robes shimmering in the torchlight. With a gracious nod, he declares:  

"You have served me well, my loyal subjects. Mmm, yes... I shall award you the gold you so valiantly reclaimed."  

Congratulations, brave travelers. You have saved the treasury and earned your reward.  

But beware—this battle is far from over. The Shadowpaws Syndicate remains a threat,  
and we may call upon your courage and wit again in the future. Until then, enjoy your well-deserved rest!" 

"""

    def display_welcome(self):
        print(welcome_art)

        print_slow("".join(self.welcome_msg))

    def print_sep(self, lines: int):
        for _ in range(lines):
            print("\n")

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

        self.print_sep(2)

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
            self.print_sep(2)

        return res

    def exclaim(self, msg: str):
        print_slow(msg)

    def run(self):
        self.print_sep(50)
        self.display_welcome()

        self.ask(
            "Are you ready to begin?",
            QuestionType.y_n,
            ["yes", "y"],
            cont_msg=["Incorrect answer. King needs attention now. Lets try again"],
        )

        self.exclaim("Great! Lets begin with some background")
        self.exclaim(self.background)
        self.exclaim(self.task_1)

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

        self.exclaim(self.task_2)

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

        self.exclaim(self.task_3)

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

        self.exclaim(self.task_4)

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

        self.exclaim(self.task_5)

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

        self.exclaim(self.congrats_msg)

        while True:
            ...


def print_slow(msg: str) -> None:
    from time import sleep

    for c in msg:
        print(c, end="", flush=True)
        if not DEV:
            sleep(0.05)
