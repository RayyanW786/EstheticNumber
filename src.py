from typing import List, Sequence, Dict


class TooSmall(Exception):
    ...


def predicate(neighbour: int, adjacent: int) -> bool:
    return abs(neighbour - adjacent) == 1


def is_esthetic(numbers: Sequence[str], mapping: Dict[str, int]):
    preds: List[bool] = []
    for idx, num in enumerate(numbers, start=1):
        if idx == len(numbers):
            break
        preds.append(predicate(mapping[numbers[idx - 1]], mapping[numbers[idx]]))
    return all(preds)


while True:
    user_input = input("Enter a hexadecimal number: ")
    value_mappings: dict[str, int] = {}
    try:
        if len(user_input) < 2:
            raise TooSmall
        for value in user_input:
            value_mappings[value] = (int(value, base=16))
    except ValueError:
        print("Invalid Hexadecimal number!\n")
        continue
    except TooSmall:
        print("number should be at least the length of 2 digits.\n2")
        continue

    pred = is_esthetic(user_input, value_mappings)
    print(f"Your number is {'NOT ' if not pred else ''}an Esthetic number")
