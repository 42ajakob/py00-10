from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingr_list: list[str] = dark_spell_allowed_ingredients()
    for ingr in ingr_list:
        if ingr.lower() in ingredients.lower():
            return ingredients + " - VALID"
    return ingredients + " - INVALID"
