def ft_recursive(days: int = None) -> None:
    if (days == None):
        return
    elif (days != 0):
        ft_recursive(days - 1)
        print("Day", days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    
    ft_recursive(days)
    print("Harvest time!")
