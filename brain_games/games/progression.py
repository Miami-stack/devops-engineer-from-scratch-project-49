import random

MIN_LEN = 5
MAX_LEN = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 5


def _generate_sequence(start: int, step: int, length: int) -> list[int]:
    """Создаёт арифметическую прогрессию по формуле из подсказки."""
    return [start + i * step for i in range(length)]


def generate_round() -> tuple[str, str]:
    """Генерирует прогрессию, скрывает случайный элемент и возвращает
    строку вопроса и правильный ответ."""
    length = random.randint(MIN_LEN, MAX_LEN)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    sequence = _generate_sequence(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = sequence[hidden_index]

    display = [
        str(num) if i != hidden_index else ".."
        for i, num in enumerate(sequence)
    ]
    question = " ".join(display)

    return question, str(correct_answer)
