import random

MIN_NUM = 1
MAX_NUM = 100
OPERATIONS = ("+", "-", "*")


def generate_round() -> tuple[str, str]:
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    op = random.choice(OPERATIONS)

    match op:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2

    question = f"{num1} {op} {num2}"
    return question, str(result)
