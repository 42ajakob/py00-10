from sys import argv


def open_argv() -> None:
    print(f"Accessing file '{argv[1]}'")
    fd = open(argv[1])

    print("---")
    print()
    print(f"{fd.read()}")
    print()
    print("---")

    fd.close()
    print(f"File '{argv[1]}' closed.")


def ft_ancient_text() -> None:
    if len(argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    try:
        open_argv()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{argv[1]}': {e}")


if __name__ == "__main__":
    ft_ancient_text()
