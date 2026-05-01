from elements import create_fire
from ..potions import healing_potion, strength_potion


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew '{healing_potion()}' and '{strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )
