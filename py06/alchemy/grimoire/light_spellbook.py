from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validated = validate_ingredients(ingredients)
    if "INVALID" in validated:
        return f"Spell rejected: {spell_name} ({validated})"
    return f"Spell recorded: {spell_name} ({validated})"
