import alchemy.grimoire


def ft() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(
        "Testing record light spell: "
        f"{alchemy.grimoire.light_spell_record(
            'Fantasy', 'Earth, wind and fire'
          )}"
    )
    print()


if __name__ == "__main__":
    ft()
