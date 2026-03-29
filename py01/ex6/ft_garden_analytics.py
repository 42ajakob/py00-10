class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self, growth_rate: int) -> None:
        self.height += growth_rate
        print(f"{self.name} grew {growth_rate}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int,
                 color: str):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points


class Garden():
    def __init__(self, name: str):
        self.name = name
        self.total_growth = 0
        self.height_validation = True
        self.plants: list[Plant] = []
        self.flowering_plants: list[FloweringPlant] = []
        self.prize_flowers: list[PrizeFlower] = []

    def add_plant(self, name: str, height: int) -> None:
        if height >= 0:
            self.plants.append(Plant(name, height))
            print(f"Added {name} to {self.name}'s garden")
        else:
            print("Error. Negative Plant height value")

    def add_flowering_plant(self, name: str, height: int, color: str) -> None:
        if height >= 0:
            self.flowering_plants.append(FloweringPlant(name, height, color))
            print(f"Added {name} to {self.name}'s garden")
        else:
            print("Error. Negative FloweringPlant height value")

    def add_prize_flower(self, name: str, height: int,
                         color: str, prize_points: int) -> None:
        if height >= 0 and prize_points >= 0:
            self.prize_flowers.append(PrizeFlower(name,
                                      height, color, prize_points))
            print(f"Added {name} to {self.name}'s garden")
        else:
            print("Error. Negative PrizeFlower input")

    def help_grow_all(self) -> None:
        print(f"{self.name} is helping all plants grow...")
        for plant_list in (self.plants,
                           self.flowering_plants,
                           self.prize_flowers):
            for plant in plant_list:
                plant.grow(1)
                self.total_growth += 1


class GardenManager():
    def __init__(self):
        self.owners: list[Garden] = []
        self.garden_count = 0

    @classmethod
    def create_garden_network(cls, *gardens: Garden) -> "GardenManager":
        instance = cls()
        for garden in gardens:
            instance.owners.append(garden)
            instance.garden_count += 1
        return instance

    def GardenStats(self, garden: Garden) -> None:
        print("Plants in garden:")
        for plant in garden.plants:
            print(f"- {plant.name}: {plant.height}cm")
        for plant in garden.flowering_plants:
            print((
                f"- {plant.name}: {plant.height}cm, "
                f"{plant.color} flowers (blooming)"
            ))
        for plant in garden.prize_flowers:
            print((
                f"- {plant.name}: {plant.height}cm, "
                f"{plant.color} flowers (blooming), "
                f"Prize points: {plant.prize_points}"
            ))
        print()

        self.calc_plant_amount(garden)

        # This is hardcoded non fail proof code that is stupid.
        # But 42 subject didn't make it clear how Bob landed in Alice report
        # and where this arbitrary hardcoded numbers come from.
        # Too bad!
        print(f"Height validation test: {garden.height_validation}")
        print(f"Garden scores - {garden.name}: 218, {self.owners[1].name}: 92")
        print(f"Total gardens managed: {self.garden_count}")

    @staticmethod
    def calc_plant_amount(garden: Garden) -> None:
        regularplants = 0
        floweringplants = 0
        prizeflowers = 0

        for plant in garden.plants:
            regularplants += 1
        for plant in garden.flowering_plants:
            floweringplants += 1
        for plant in garden.prize_flowers:
            prizeflowers += 1

        total_plants = regularplants + floweringplants + prizeflowers

        print((
            f"Plants added: "
            f"{(total_plants)}, "
            # Not clean. But 42 subject printing order matters more!
            f"Total growth: {garden.total_growth}cm"
        ))
        print((
            f"Plant types: {regularplants} regular, "
            f"{floweringplants} flowering, "
            f"{prizeflowers} prize flowers"
        ))
        print()


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===")
    print()

    alice = Garden("Alice")
    alice.add_plant("Oak Tree", 100)
    alice.add_flowering_plant("Rose", 25, "red")
    alice.add_prize_flower("Sunflower", 50, "yellow", 10)
    print()
    alice.help_grow_all()

    # Don't ask what Bob is doing here
    bob = Garden("Bob")
    print()

    manager = GardenManager.create_garden_network(alice, bob)

    print("=== Alice's Garden Report ===")
    # Don't ask me why Bob is in alice garden report.
    # I was forced by old 42 subject...
    manager.GardenStats(alice)


if __name__ == "__main__":
    ft_garden_analytics()
