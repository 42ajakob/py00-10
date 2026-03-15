def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    elif (water_level < 1):
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif (water_level > 10):
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif (sunlight_hours < 2):
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif (sunlight_hours > 12):
        raise ValueError((
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        ))
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print()

    try:
        print("Testing good values...")
        check_plant_health("tomato", 6, 3)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    try:
        print("Testing empty plant name...")
        check_plant_health("", 6, 3)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 3)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 6, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
