class SecurePlant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def set_height(self, height: float) -> None:
        if (height >= 0):
            self._height = height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if (age >= 0):
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}:  Error, age can't be negative")
            print("Age updated rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-5)
    print()
    print("Current State: ", end="")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
