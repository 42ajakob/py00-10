class SecurePlant:
    def __init__(self, name: str = None) -> None:
        self.name = name
        self.height = 0
        self.age = 0
        print(f"Plant created: {name}")

    def set_height(self, user_height: int) -> None:
        if (user_height < 0):
            print(f"Invalid operation attempted: height {user_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = user_height
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, user_age: int) -> None:
        if (user_age < 0):
            print(f"Invalid operation attempted: age {user_age}cm [REJECTED]")
            print(f"Security: Negative age rejected")
        else:
            self.age = user_age
            print(f"Age updated: {self.age}cm [OK]")

    def get_height(self) -> int:
        return self.height
    def get_age(self) -> int:
        return self.age
    
    def get_info(self) -> None:
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")

def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    rose.get_info()

if __name__ == "__main__":
    ft_garden_security()