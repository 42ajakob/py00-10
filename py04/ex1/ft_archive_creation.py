from sys import argv


def open_argv() -> str:
    print(f"Accessing file '{argv[1]}'")
    fd = open(argv[1])

    print("---")
    print()
    content = fd.read()
    print(f"{content}")
    print()
    print("---")

    fd.close()
    print(f"File '{argv[1]}' closed.")

    return content


def transform_data(content: str) -> str:
    print()
    print("Transform data:")

    content = "\n".join(f"{line}#" for line in content.split("\n"))

    print("---")
    print()
    print(f"{content}")
    print()
    print("---")

    return content


def write_to_newfile(user_input: str, content: str) -> None:
    if user_input == "":
        print("Not saving data")
    else:
        print(f"Saving data to '{user_input}'")
        new_file = open(user_input, "w")
        new_file.write(content)
        print(f"Data saved in file '{user_input}'")
        new_file.close()


def ft_archive_creation() -> None:
    if len(argv) == 1:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    try:
        content = open_argv()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{argv[1]}': {e}")
        return

    content = transform_data(content)

    try:
        user_input = input("Enter new file name (or empty): ")
        write_to_newfile(user_input, content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error writing file '{user_input}': {e}")


if __name__ == "__main__":
    ft_archive_creation()
