def check_temperature(temp_str: str) -> int | None:
    try:
        int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        if int(temp_str) >= 0 and int(temp_str) <= 40:
            print(f"Temperature {temp_str}°C is perfect for plants!")
            return int(temp_str)
        elif int(temp_str) > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        elif int(temp_str) < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    temps = [25, "abc", 100, -50]
    for temp in temps:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
