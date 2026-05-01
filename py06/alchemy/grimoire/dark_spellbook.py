from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validated = validate_ingredients(ingredients)
    if "INVALID" in validated:
        return f"Spell rejected: {spell_name} ({validated})"
    return f"Spell recorded: {spell_name} ({validated})"
