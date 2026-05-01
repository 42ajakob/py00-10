def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    ingr_list: list[str] = light_spell_allowed_ingredients()
    for ingr in ingr_list:
        if ingr.lower() in ingredients.lower():
            return ingredients + " - VALID"
    return ingredients + " - INVALID"
