def garden_operations() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()
    print("Testing ZeroDivisionError...")
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()
    print("Testing FileNotFoundError...")
    try:
        fd = open("missing.txt")
        fd.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()
    print("Testing KeyError...")
    try:
        plants = {'name': "Rose"}
        missing_plant = plants["missing_plant"]
        # flake8 complain.
        plants = missing_plant
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()
    print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
