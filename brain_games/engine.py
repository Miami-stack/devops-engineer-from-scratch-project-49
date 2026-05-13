import prompt

ROUNDS_TO_WIN = 3


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run_game(description: str, generate_round) -> None:
    name = welcome_user()
    print(description)

    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
