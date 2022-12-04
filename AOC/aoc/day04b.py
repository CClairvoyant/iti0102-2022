"""Day 4 part 2."""


def part_2(filename: str):
    """Part 2."""
    with open(filename) as file:
        content = file.read().split("\n")
    count = 0
    for row in content:
        section = row.split(",")
        if int(section[1].split("-")[1]) >= int(section[0].split("-")[1]) >= int(section[1].split("-")[0]) or \
                int(section[0].split("-")[1]) >= int(section[1].split("-")[1]) >= int(section[0].split("-")[0]):
            count += 1
    return count
