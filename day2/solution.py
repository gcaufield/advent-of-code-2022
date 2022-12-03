#! /usr/bin python3
def get_score_for_choice(choice: str) -> int:
    if choice == "A":
        return 1
    if choice == "B":
        return 2
    return 3


def get_win(opponent: str):
    if opponent == "A":
        return "B"
    if opponent == "B":
        return "C"
    return "A"


def get_loss(opponent: str):
    if opponent == "A":
        return "C"
    if opponent == "B":
        return "A"
    return "B"


def get_choice_for_result(opponent: str, result: str) -> str:
    if result == "X":
        return get_loss(opponent)
    if result == "Y":
        return opponent
    return get_win(opponent)


def convert_choice(choice: str) -> str:
    if choice == "X":
        return "A"
    if choice == "Y":
        return "B"
    return "C"


def is_winner(player_choice: str, opponent_choice: str) -> bool:
    if player_choice == "A" and opponent_choice == "C":
        return True
    if player_choice == "B" and opponent_choice == "A":
        return True
    if player_choice == "C" and opponent_choice == "B":
        return True
    return False


def get_score_for_result(opponent: str, player: str) -> int:
    if opponent == player:
        return 3
    elif is_winner(player, opponent):
        return 6
    else:
        return 0


def get_score_part1(line: str) -> int:
    score = 0
    options = line.strip().split(" ")
    opponent = options[0]
    player = convert_choice(options[1])

    score += get_score_for_choice(player)
    score += get_score_for_result(opponent, player)

    return score


def get_score_part2(line: str) -> int:
    score = 0
    options = line.strip().split(" ")
    opponent = options[0]
    result = options[1]

    player = get_choice_for_result(opponent, result)

    score += get_score_for_choice(player)
    score += get_score_for_result(opponent, player)

    return score


def read():
    p1score = 0
    p2score = 0
    with open("input.txt") as f:
        for line in f:
            p1score += get_score_part1(line)
            p2score += get_score_part2(line)

    print(p1score)
    print(p2score)


read()
