class Plant:
    def __init__(self, name: str, height: int,
                 plant_age: int, growth_speed: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.growth_speed = growth_speed

    def age(self) -> int:
        self.plant_age += 1

    def grow(self) -> int:
        self.height += self.growth_speed

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25, 30, 1)
    sunflower = Plant("Sunflower", 80, 45, 3)
    cactus = Plant("Cactus", 15, 120, 2)

    print("=== Day 1 ===")
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()

    for day in range(6):
        rose.age()
        rose.grow()
        sunflower.age()
        sunflower.grow()
        cactus.age()
        cactus.grow()

    print()
    print("=== Day 7 ===")
    rose.get_info()
    print("Growth this week: +6cm")
    print()
    sunflower.get_info()
    print("Growth this week: +18cm")
    print()
    cactus.get_info()
    print("Growth this week: +12cm")


if __name__ == "__main__":
    ft_plant_growth()
