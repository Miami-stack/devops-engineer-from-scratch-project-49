from brain_games.engine import run_game
from brain_games.games.progression import generate_round

DESCRIPTION = "What number is missing in the progression?"


def main() -> None:
    run_game(DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()
