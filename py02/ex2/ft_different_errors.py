def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
        # close() is a forbidden function in 42 subject!
        # Too bad!
    elif operation_number == 3:
        "abc" + 1
    elif operation_number == 4:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    num = 0
    while num != 5:
        print(f"Testing operation {num}...")
        try:
            garden_operations(num)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        num += 1

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
