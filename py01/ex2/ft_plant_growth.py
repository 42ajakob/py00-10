class Plant:
    def __init__(self, name: str, height: float, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")

    def grow(self, growth_rate: float) -> None:
        self.height += growth_rate

    def age(self, age_rate: int) -> None:
        self.plant_age += age_rate


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)

    for day in range(7):
        print(f"=== Day {day + 1} ===")
        rose.show()
        rose.grow(0.8)
        rose.age(1)
    # Prints by 4.8cm, grows by 5.6cm, rounds up to 6cm
    # There is no logic here.
    # It's how the 42 code example snippet in the subject does it
    # I am not responsible for the brain damage it causes :)
    print(f"Growth this week: {round(rose.height - 25)}cm")


if __name__ == "__main__":
    ft_plant_growth()
