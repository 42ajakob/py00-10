from math import sqrt


def get_player_pos() -> tuple:
    while True:
        try:
            coord_input = input("Enter new coordinates "
                                "as floats in format 'x,y,z': ")
            if ',' not in coord_input:
                print("Invalid syntax")
                continue
            coord_list = coord_input.split(",")

            # len() is forbidden. Because. Next exercise it's allowed again...
            count = 0
            for _ in coord_list:
                count += 1
            if count != 3:
                print("Invalid syntax")
                continue
            coords = tuple(float(coord.strip()) for coord in coord_list)
            return coords
        except ValueError as e:
            bad_value = str(e).split("'")[1]
            print(f"Error on parameter '{bad_value}': {e}")


def ft_coordinate_system() -> None:
    print("Get a first set of coordinates")
    set_one = get_player_pos()
    distance_to_center = sqrt((set_one[0] - 0.0) ** 2 +
                              (set_one[1] - 0.0) ** 2 +
                              (set_one[2] - 0.0) ** 2)
    print(f"Got a first tuple: {set_one}")
    print(f"It includes: X={set_one[0]}, Y={set_one[1]}, Z={set_one[2]}")
    print(f"Distance to center: {distance_to_center:.4f}")
    print()

    print("Get a second set of coordinates")
    set_two = get_player_pos()
    sets_distance = sqrt((set_one[0] - set_two[0]) ** 2 +
                         (set_one[1] - set_two[1]) ** 2 +
                         (set_one[2] - set_two[2]) ** 2)
    print(f"Distance between the 2 sets of coordinates: {sets_distance:.4f}")


if __name__ == "__main__":
    ft_coordinate_system()
