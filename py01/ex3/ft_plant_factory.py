class Plant:
    def __init__(self, name: str, height: int,
                 age: int):
        self.name = name
        self.height = height
        self.age = age

    # Flake8 complains. Otherwise this would be in __init__()
    def print_created(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    rose.print_created()
    oak = Plant("Oak", 200, 365)
    oak.print_created()
    cactus = Plant("Cactus", 5, 90)
    cactus.print_created()
    sunflower = Plant("Sunflower", 80, 45)
    sunflower.print_created()
    fern = Plant("Fern", 15, 120)
    fern.print_created()
    print()
    print("Total plants created: 5")


if __name__ == "__main__":
    ft_plant_factory()
