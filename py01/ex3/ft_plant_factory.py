class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    # Yes, I wasn't allowed to put "Created: " into show()
    # They forced me. And for the sake of consistency across all exercises
    # I had no choice but to put it outside Plant class
    # forbidden functions + mypy prohibit me from looping as well
    rose = Plant("Rose", 25, 30)
    print("Created: ", end="")
    rose.show()
    oak = Plant("Oak", 200, 365)
    print("Created: ", end="")
    oak.show()
    cactus = Plant("Cactus", 5, 90)
    print("Created: ", end="")
    cactus.show()
    sunflower = Plant("Sunflower", 80, 45)
    print("Created: ", end="")
    sunflower.show()
    fern = Plant("Fern", 15, 120)
    print("Created: ", end="")
    fern.show()


if __name__ == "__main__":
    ft_plant_factory()
