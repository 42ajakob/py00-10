from sys import argv


def ft_create_inventory() -> dict[str, int]:
    inv = {}

    for arg in argv[1:]:
        tmp = arg.split(":")

        if len(tmp) != 2:
            print(f"Error - invalid parameter '{tmp[0]}'")
            continue
        elif tmp[0] in inv:
            print(f"Redundant item '{tmp[0]}' - discarding")
            continue

        try:
            tmp_dict = {tmp[0]: int(tmp[1])}
        except ValueError as e:
            print(f"Quantity error for 'key': {e}")
            continue

        inv.update(tmp_dict)
    return inv


def ft_inventory_system() -> None:
    inv = ft_create_inventory()

    print(f"Got inventory: {inv}")
    print(f"Item list: {list(inv.keys())}")

    total = sum(inv.values())
    print(f"Total quantity of the {len(inv)} items: {total}")

    for item in inv:
        quant = inv[item]
        print(f"Item {item} represents {quant / total * 100}%")

    # Why is sum() allowed but not max(), min()?
    first_key = list(inv.keys())[0]
    highest_item = first_key
    lowest_item = first_key
    highest_quant = inv[first_key]
    lowest_quant = inv[first_key]

    for item in inv:
        quant = inv[item]
        if quant > highest_quant:
            highest_item = item
            highest_quant = quant
        if quant < lowest_quant:
            lowest_item = item
            lowest_quant = quant

    print(f"Item most abundant: {highest_item} with quantity {highest_quant}")
    print(f"Item least abundant: {lowest_item} with quantity {lowest_quant}")

    inv.update({"magic item": 1})
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    ft_inventory_system()
