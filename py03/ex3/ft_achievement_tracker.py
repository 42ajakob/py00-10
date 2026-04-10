from random import randint, sample


def gen_player_achievements() -> set:
    ach_list = ['Boss Slayer', 'Collector Supreme', 'Crafting Genius',
                'First Steps', 'Master Explorer', 'Sharp Mind', 'Speed Runner',
                'Strategist', 'Survivor', 'Treasure Hunter', 'Unstoppable',
                'Untouchable', 'World Savior']

    # 42 subject on it's example either has
    # sphagetti code, cheats, or impossible rng
    # Analyzed this excerise way to much...
    return set(sample(ach_list, randint(5, 10)))


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
    print(f"All distinct achievements: "
          f"{set().union(alice, bob, charlie, dylan)}")
    print()
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")
    print()
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print()
    print(f"Alice is missing: {bob.union(charlie, dylan) - alice}")
    print(f"Bob is missing: {alice.union(charlie, dylan) - bob}")
    print(f"Alice is missing: {alice.union(bob, dylan) - charlie}")
    print(f"Alice is missing: {alice.union(bob, charlie) - dylan}")


if __name__ == "__main__":
    ft_achievement_tracker()
