import random

MIN_NUM = 1
MAX_NUM = 100


def generate_round() -> tuple[str, str]:
    number = random.randint(MIN_NUM, MAX_NUM)
    answer = "yes" if number % 2 == 0 else "no"
    return str(number), answer
