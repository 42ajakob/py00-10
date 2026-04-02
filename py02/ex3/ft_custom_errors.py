class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        GardenError.__init__(self, message)


def ft_raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def ft_raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_exceptions() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")

    try:
        ft_raise_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")

    try:
        ft_raise_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")

    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_exceptions()
