import random

MIN_NUM = 1
MAX_NUM = 100


def is_prime(n: int) -> bool:
    """Возвращает True, если число простое."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_round() -> tuple[str, str]:
    """Генерирует случайное число и правильный ответ."""
    number = random.randint(MIN_NUM, MAX_NUM)
    answer = "yes" if is_prime(number) else "no"
    return str(number), answer