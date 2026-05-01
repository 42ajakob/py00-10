class Plant:
    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} "
                  f"age, {self._show_calls} show")

    def __init__(self, name: str, height: float, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.stats = self.Stats()

    @classmethod
    def init_unknown_plant(cls) -> Plant:
        return cls("Unknown plant", 0, 0)

    @staticmethod
    def check_year_old(days: int) -> None:
        if days / 365 >= 1:
            print("True")
        else:
            print("False")

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")
        self.stats._show_calls += 1

    def grow(self, growth_rate: float) -> None:
        self.height += growth_rate
        self.stats._grow_calls += 1

    def age(self, age_rate: int) -> None:
        self.plant_age += age_rate
        self.stats._age_calls += 1


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


class Seed(Flower):
    def __init__(self, name: str, height: float, plant_age: int, color: str):
        super().__init__(name, height, plant_age, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, trunk_diameter: float):
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter
        self.produce_shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def display(self) -> None:
        self.stats.display()
        print(f" {self.produce_shade_calls} shade")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")
        self.produce_shade_calls += 1


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    unknown = Plant.init_unknown_plant()
    print("Is 30 days more then a year? -> ", end="")
    unknown.check_year_old(30)
    print("Is 400 days more then a year? -> ", end="")
    unknown.check_year_old(400)
    print()

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    rose.stats.display()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose.stats.display()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[statistics for Oak]")
    oak.display()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.display()
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower.stats.display()
    print()

    print("=== Anonymous")
    unknown.show()
    print("[statistics for Unknown plant]")
    unknown.stats.display()


if __name__ == "__main__":
    ft_garden_analytics()
