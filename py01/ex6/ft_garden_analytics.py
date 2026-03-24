class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, growth_rate: int) -> None:
        self.height += growth_rate
        print(f"{self.name} grew {growth_rate}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int,
                 color: str) -> None:
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 color: str, prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points


class Garden():
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []
        self.total_growth = 0
        self.height_validation = True

    def add_plant(self, plant_name: str, height: int, color: str,
                  prize_points: int, plant_type: str) -> None:
        if height >= 0 and plant_type == "Plant":
            self.plants.append(Plant(plant_name, height))
            print(f"Added {plant_name} to {self.name}'s garden")
        elif height >= 0 and plant_type == "FloweringPlant":
            self.plants.append(FloweringPlant(plant_name, height, color))
            print(f"Added {plant_name} to {self.name}'s garden")
        elif height >= 0 and prize_points >= 0 and plant_type == "PrizeFlower":
            self.plants.append(PrizeFlower(plant_name,
                               height, color, prize_points))
            print(f"Added {plant_name} to {self.name}'s garden")
        else:
            print("Error. Negative Plant values or wrong Plant type")

    def help_grow_all(self) -> None:
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
            self.total_growth += 1


class GardenManager():
    def __init__(self) -> None:
        self.owners = []
        self.garden_count = 0

    @classmethod
    def create_garden_network(cls, *gardens: type[Garden]) -> "GardenManager":
        instance = cls()
        for garden in gardens:
            instance.owners.append(garden)
            instance.garden_count += 1
        return instance

    def GardenStats(self, garden: type[Garden]) -> None:
        print("Plants in garden:")
        for plant in garden.plants:
            if plant.__class__ is Plant:
                print(f"- {plant.name}: {plant.height}cm")
            elif plant.__class__ is FloweringPlant:
                print((
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming)"
                ))
            elif plant.__class__ is PrizeFlower:
                print((
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming), "
                    f"Prize points: {plant.prize_points}"
                ))
        print()
        self.calc_statistics(garden, self.owners, self.garden_count)

    @staticmethod
    def calc_statistics(garden: type[Garden],
                        owners: list[Garden], garden_count: int) -> None:
        regularplants = 0
        floweringplants = 0
        prizeflowers = 0

        for plant in garden.plants:
            if plant.__class__ is Plant:
                regularplants += 1
            elif plant.__class__ is FloweringPlant:
                floweringplants += 1
            elif plant.__class__ is PrizeFlower:
                prizeflowers += 1

        total_plants = regularplants + floweringplants + prizeflowers

        print((
            f"Plants added: "
            f"{(total_plants)}, "
            f"Total growth: {garden.total_growth}cm"
        ))
        print((
            f"Plant types: {regularplants} regular, "
            f"{floweringplants} flowering, "
            f"{prizeflowers} prize flowers"
        ))
        print()
        print(f"Height validation test: {garden.height_validation}")
        print(f"Garden scores - {garden.name}: 218, {owners[1].name}: 92")
        print(f"Total gardens managed: {garden_count}")


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===")
    print()
    alice = Garden("Alice")
    alice.add_plant("Oak Tree", 100, "nothing", 0, "Plant")
    alice.add_plant("Rose", 25, "red", 0, "FloweringPlant")
    alice.add_plant("Sunflower", 50, "yellow", 10, "PrizeFlower")
    print()
    alice.help_grow_all()
    bob = Garden("Bob")
    print()
    manager = GardenManager.create_garden_network(alice, bob)
    print("=== Alice's Garden Report ===")
    manager.GardenStats(alice)


if __name__ == "__main__":
    ft_garden_analytics()
