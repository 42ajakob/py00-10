from random import choice
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    names = ["alice", "bob", "charlie", "dylan"]
    actions = ["grab", "eat", "move", "run", "swim",
               "climb", "release", "sleep"]
    while True:
        name = choice(names)
        action = choice(actions)
        yield (name, action)


def consume_event(tuple_list: list[tuple[str, str]]) \
                  -> Generator[tuple[str, str], None, None]:
    while tuple_list:
        tuple_pair = choice(tuple_list)
        tuple_list.remove(tuple_pair)
        yield tuple_pair


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    i = 0

    while i < 1000:
        tuple_pair = next(gen_event())
        print(f"Event {i}: Player {tuple_pair[0]} did action {tuple_pair[1]}")
        i += 1

    tuple_list = [next(gen_event()) for _ in range(10)]
    print(f"Built list of 10 events: {tuple_list}")

    for event in consume_event(tuple_list):
        print(f"Got event from list: {event}")
        print(f" Remains in list: {tuple_list}")


if __name__ == "__main__":
    ft_data_stream()
