def ft() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(
        "Testing record dark spell: "
        f"{dark_spell_record(
            "Fantasy", "Bats, frogs and arsenic"
          )}"
    )
    print()


if __name__ == "__main__":
    ft()
