class GardenError(Exception):
    pass


class WaterTankError(GardenError):
    pass


class Plant():
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self) -> None:
        self.plant_list = []

    def add_plant(self, name: str, water_level: int,
                  sunlight_hours: int) -> None:
        if not name:
            raise ValueError("Plant name cannot be empty!")
        self.plant_list.append(Plant(name, water_level, sunlight_hours))
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        for plant in self.plant_list:
            print(f"Watering {plant.name} - success")
            plant.water_level += 1

    @staticmethod
    def check_plant_health(plant: Plant) -> None:
        if plant.water_level < 1:
            raise ValueError((
                f"{plant.name}: Water level "
                f"{plant.water_level} is too low (min 1)"
            ))
        elif plant.water_level > 10:
            raise ValueError((
                f"{plant.name}: Water level "
                f"{plant.water_level} is too high (max 10)"
            ))
        elif (plant.sunlight_hours < 2):
            raise ValueError((
                f"{plant.name}: Sunlight hours "
                f"{plant.sunlight_hours} is too low (min 2)"
            ))
        elif (plant.sunlight_hours > 12):
            raise ValueError((
                f"{plant.name}: Sunlight hours "
                f"{plant.sunlight_hours} is too high (max 12)"
            ))
        else:
            print((
                f"{plant.name}: healthy (water: "
                f"{plant.water_level}, sun: {plant.sunlight_hours})"
            ))


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()
    garden = GardenManager()
    try:
        print("Adding plants to garden...")
        garden.add_plant("tomato", 4, 8)
        garden.add_plant("lettuce", 14, 8)
        garden.add_plant("", 4, 8)
    except ValueError as e:
        print(f"Error adding plant: {e}")
    print()
    try:
        print("Watering plants...")
        print("Opening watering system")
        garden.water_plants()
    finally:
        print("Closing watering system (cleanup)")
    print()
    try:
        print("Checking plant health...")
        garden.check_plant_health(garden.plant_list[0])
        garden.check_plant_health(garden.plant_list[1])
    except ValueError as e:
        print(f"Error checking {e}")
    print()
    try:
        print("Testing error recovery...")
        raise WaterTankError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
