from ex0.creatureFactory import CreatureFactory
from .capability import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling | Bloomelle:  # mypy error...
        return Sproutling()

    def create_evolved(self) -> Sproutling | Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling | Morphagon:
        return Shiftling()

    def create_evolved(self) -> Shiftling | Morphagon:
        return Morphagon()
