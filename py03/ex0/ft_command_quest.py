from sys import argv


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")
    count = 0

    if len(argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(argv) - 1}")
        for arg in argv[1:]:
            count += 1
            print(f"Argument {count}: {arg}")

    print(f"Total arguments: {len(argv)}")
    print()


if __name__ == "__main__":
    ft_command_quest()
