import math
import random

MIN_NUM = 1
MAX_NUM = 100


def generate_round() -> tuple[str, str]:
    """Генерирует два числа и их НОД как строку."""
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    question = f"{num1} {num2}"
    answer = str(math.gcd(num1, num2))
    return question, answer
