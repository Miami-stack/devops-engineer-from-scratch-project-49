from brain_games.engine import run_game
from brain_games.games.calc import generate_round

DESCRIPTION = "What is the result of the expression?"


def main() -> None:
    run_game(DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()
