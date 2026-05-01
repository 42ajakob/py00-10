from sys import argv


def stats(score_list: list[int]) -> None:
    print(f"Scores processed: {score_list}")
    print(f"Total players: {len(score_list)}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list) / len(score_list)}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    print(f"Score range: {max(score_list) - min(score_list)}")


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")

    score_list: list[int] = []
    for arg in argv[1:]:
        try:
            score_list.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if score_list:
        stats(score_list)
    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    ft_score_analytics()
