from brain_games.engine import run_game
from brain_games.games.gcd import generate_round

DESCRIPTION = "Find the greatest common divisor of given numbers."


def main() -> None:
    run_game(DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()
