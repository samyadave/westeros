DEV = True


def print_slow(msg: str) -> None:
    from time import sleep

    for c in msg:
        print(c, end="", flush=True)
        if not DEV:
            sleep(0.05)


def print_sep(lines: int):
    for _ in range(lines):
        print("\n")


class QuestionType:
    y_n = 'Enter "yes" or "no": '
    mc = "Choose an option: "
