def ft_recursive_function(days):
    if (days != 0):
        ft_recursive_function(days - 1)
        print("Day", days)

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_recursive_function(days)
    print("Harvest time!")