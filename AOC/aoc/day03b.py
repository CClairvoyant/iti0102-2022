"""Day 3 part 2."""


def part_2(filename: str):
    """Part 2."""
    with open(filename) as file:
        content = file.read().split("\n")
    priority_sum = 0
    for i in range(2, len(content), 3):
        badge = set(content[i]).intersection(set(content[i - 1])).intersection(set(content[i - 2])).pop()
        if badge.isupper():
            priority_sum += ord(badge) - ord("A") + 27
        else:
            priority_sum += ord(badge) - ord("a") + 1
    return priority_sum
