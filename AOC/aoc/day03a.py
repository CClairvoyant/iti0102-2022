"""Day 3 part 1."""


def part_1(filename: str):
    """Part 1."""
    with open(filename) as file:
        content = file.read().split("\n")
    priority_sum = 0
    for row in content:
        half_1 = row[:len(row) // 2]
        half_2 = row[len(row) // 2:]
        common_letters = set(half_1).intersection(set(half_2))
        for letter in common_letters:
            if letter.isupper():
                priority_sum += ord(letter) - ord("A") + 27
            else:
                priority_sum += ord(letter) - ord("a") + 1
    return priority_sum
