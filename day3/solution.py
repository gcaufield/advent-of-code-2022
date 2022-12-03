#!/usr/bin/env python3


def score_item(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1

    return ord(item) - ord("A") + 27


def score_bags(bags: list) -> int:
    score = 0
    for bag in bags:
        score += score_bag(bag)
    return score


def score_bag(bag: str) -> int:
    divide = int(len(bag) / 2)
    pouch1 = set(bag[:divide])
    pouch2 = set(bag[divide:])
    return score_item(list(pouch1.intersection(pouch2))[0])


def score_groups(bags: list, group_size: int) -> int:
    score = 0

    for i in range(0, len(bags), group_size):
        unique_items = set(bags[i])

        for j in range(1, group_size):
            unique_items = unique_items.intersection(set(bags[i + j]))

        score += score_item(list(unique_items)[0])

    return score


def main():
    bags = []
    with open("input.txt") as f:
        for line in f:
            bags.append(line.strip())

    print(score_bags(bags))
    print(score_groups(bags, 3))


main()
