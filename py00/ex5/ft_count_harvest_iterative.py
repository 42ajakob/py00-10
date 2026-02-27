def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for past_days in range(days):
        print("Day", past_days + 1)
    print("Harvest time!")
