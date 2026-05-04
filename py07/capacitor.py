from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    for label, creature in zip(
        [" base:", " evolved:"],
        [factory.create_base(), factory.create_evolved()]
    ):
        print(label)
        print(creature.describe())
        print(creature.attack())
        print(creature.heal())
    print()


def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    for label, creature in zip(
        [" base:", " evolved:"],
        [factory.create_base(), factory.create_evolved()]
    ):
        print(label)
        print(creature.describe())
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
    print()


if __name__ == "__main__":
    test_healing(HealingCreatureFactory())
    test_transform(TransformCreatureFactory())
