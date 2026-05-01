class Plant:
    def __init__(self, name: str, height: float, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, plant_age: int, color: str):
        super().__init__(name, height, plant_age)
        self.color = color
        self.blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.blooming is True:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, trunk_diameter: float):
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, harvest_season: str):
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self, age_rate: int) -> None:
        self.plant_age += age_rate

    def grow(self, growth_rate: float) -> None:
        self.height += growth_rate
        self.nutritional_value += 1


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age(1)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
