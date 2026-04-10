from random import randint, sample


def gen_player_achievements():
    # ach_list = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
    #             'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps',
    #             'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']
    ach_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    num_of_ach = randint(5, 10)

    indexes = []
    i = 0
    while i < len(ach_list):
        indexes.append(i)
        i += 1

    random_indexes = sample(indexes, num_of_ach)

    new_list = []
    i = 0
    while i < len(random_indexes):
        new_list.append(ach_list[random_indexes[i]])
        i += 1

    # manual sort
    i = 0
    while i < len(new_list):
        j = i + 1
        while j < len(new_list):
            if new_list[j] < new_list[i]:
                new_list[i], new_list[j] = new_list[j], new_list[i]
            j += 1
        i += 1

    return set(new_list)

# def gen_player_achievements() -> set:
#     ach_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

#     num_of_ach = randint(5, 10)
#     random_indexes = sample(len(ach_list), num_of_ach)

#     new_list = [ach_list[i] for i in random_indexes]
#     sort = sorted(new_list)
#     result_set = set(sort)
#     return result_set


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievements()
    print(f"Player Alice: {alice}")
    bob = gen_player_achievements()
    print(f"Player Bob: {bob}")
    charlie = gen_player_achievements()
    print(f"Player Charlie: {charlie}")
    dylan = gen_player_achievements()
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {set().union(alice, bob, charlie, dylan)}")
    print()
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")
    print()
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print()
    print(f"Alice is missing: {bob.union(charlie, dylan) - alice}")
    print(f"Bob is missing: {alice.union(charlie, dylan) - bob }")
    print(f"Alice is missing: {alice.union(bob, dylan) - charlie}")
    print(f"Alice is missing: {alice.union(bob, charlie) - dylan}")


if __name__ == "__main__":
    ft_achievement_tracker()
