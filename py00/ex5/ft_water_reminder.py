def ft_water_reminder() -> None:
    days_since_watering = int(input("Days since last watering: "))
    if (days_since_watering > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
