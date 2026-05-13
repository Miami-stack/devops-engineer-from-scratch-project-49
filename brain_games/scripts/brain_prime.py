from brain_games.engine import run_game
from brain_games.games.prime import generate_round

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main() -> None:
    run_game(DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()
