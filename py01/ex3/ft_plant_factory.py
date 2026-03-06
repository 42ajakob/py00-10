class Plant:
    def __init__(self, name: str = None, height: int = None, age: int = None) -> None:
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {name} ({height}cm, {age} days)")

def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    print()
    print("Total plants created: 5")

if __name__ == "__main__":
    ft_plant_factory()