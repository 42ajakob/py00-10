from ex0 import FlameFactory, AquaFactory


def test_factory() -> None:
    factory_list = [FlameFactory(), AquaFactory()]

    for creatue in factory_list:
        print("Testing factory")
        base = creatue.create_base()
        evolved = creatue.create_evolved()

        print(base.describe())
        print(base.attack())
        print(evolved.describe())
        print(evolved.attack())
        print()

    print("Testing battle")

    flameling = factory_list[0].create_base()
    aquabub = factory_list[1].create_base()

    print(flameling.describe())
    print(" vs.")
    print(aquabub.describe())
    print(" fight!")
    print(flameling.attack())
    print(aquabub.attack())


if __name__ == "__main__":
    test_factory()
