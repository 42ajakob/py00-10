from random import randint


def ft_data_alchemist() -> None:
    player_list = ["Alice", "bob", "Charlie", "dylan",
                   "Emma", "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {player_list}")

    capitalize_list = [name.capitalize() for name in player_list]
    print(f"New list with all names capitalized: {capitalize_list}")

    capitalized_only = [name for name in player_list if name.istitle()]
    print(f"New list of capitalized names only: {capitalized_only}")

    scores = {name.capitalize(): randint(0, 1000) for name in player_list}

    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {avg:.2f}")

    above_avg = {name: score for name, score in scores.items() if score > avg}
    print(f"High scores: {above_avg}")


if __name__ == "__main__":
    ft_data_alchemist()
