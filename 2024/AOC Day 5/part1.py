# https://adventofcode.com/2024/day/5


def parse_input(input_text):
    sections = input_text.strip().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in sections[0].split("\n")]
    updates = [list(map(int, line.split(","))) for line in sections[1].split("\n")]
    return rules, updates


def is_valid_ordering(update, rules):
    position = {page: i for i, page in enumerate(update)}

    for before, after in rules:
        if before in position and after in position:
            if position[before] > position[after]:
                return False

    return True


def find_middle_page(update):
    return update[len(update) // 2]


def sum_of_middle_pages(input_text):
    rules, updates = parse_input(input_text)
    valid_updates = [update for update in updates if is_valid_ordering(update, rules)]
    return sum(find_middle_page(update) for update in valid_updates)


with open("input.txt", "r") as file:
    input_text = file.read()

print(sum_of_middle_pages(input_text))
