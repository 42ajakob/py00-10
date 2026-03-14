class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print(f"{name} (Flower): {height}cm, {age} days, {color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print((
            f"{name} (Tree): {height}cm, "
            f"{age} days, {trunk_diameter} diameter"
        ))

    def produce_shade(self) -> None:
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print((
            f"{name} (Vegetable): {height}cm, "
            f"{age} days, {harvest_season} harvest"
        ))

    # Flake8 complains. Otherwise this would be in __init__()
    def nutritions(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.nutritions()
    print()
    print()
    sunflower = Flower("Sunflower", 80, 45, "yellow")
    sunflower.bloom()
    print()
    birke = Tree("Birke", 600, 2000, 60)
    birke.produce_shade()
    print()
    carrot = Vegetable("Carrot", 200, 30, "Spring", "vitamin A")
    carrot.nutritions()


if __name__ == "__main__":
    ft_plant_types()
