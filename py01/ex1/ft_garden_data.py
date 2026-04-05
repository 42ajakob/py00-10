class Plant:
    # 42 subject describes this exercise without using __init__()
    # But the __init__() route is not forbidden
    # Therefore ex3/ feels like a dejavu
    # At least that's what a french guy would say
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    rose.show()

    sunflower = Plant("Sunflower", 80, 45)
    sunflower.show()

    cactus = Plant("Cactus", 15, 120)
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()
