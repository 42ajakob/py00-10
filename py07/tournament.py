from ex0 import FlameFactory, AquaFactory
from ex0.creatureFactory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy, AggressiveStrategy,
    DefensiveStrategy, BattleStrategy, InvalidStrategyError
)


def battle(
    tournament_name: str,
    label: str,
    opponents: list[tuple[CreatureFactory, BattleStrategy, str]],
) -> None:
    parts = [
        f"({lbl}+{strat.__class__.__name__.removesuffix('Strategy')})"
        for _, strat, lbl in opponents
    ]
    print(f"Tournament {tournament_name} ({label})")
    print(f" [ {', '.join(parts)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    for i, (factory1, strategy1, _) in enumerate(opponents):
        for factory2, strategy2, _ in opponents[i + 1:]:
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print("* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                print()
                return
            print()


if __name__ == "__main__":
    battle("0", "basic", [
        (FlameFactory(), NormalStrategy(), "Flameling"),
        (HealingCreatureFactory(), DefensiveStrategy(), "Healing"),
    ])
    battle("1", "error", [
        (FlameFactory(), AggressiveStrategy(), "Flameling"),
        (HealingCreatureFactory(), DefensiveStrategy(), "Healing"),
    ])
    battle("2", "multiple", [
        (AquaFactory(), NormalStrategy(), "Aquabub"),
        (HealingCreatureFactory(), DefensiveStrategy(), "Healing"),
        (TransformCreatureFactory(), AggressiveStrategy(), "Transform"),
    ])
