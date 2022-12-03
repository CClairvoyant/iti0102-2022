"""Day 2 part 1."""


def part_1(file_name: str):
    """Part 1."""
    with open(file_name, "r") as data:
        content = data.read()
    my_points = content.count("X") + content.count("Y") * 2 + content.count("Z") * 3
    matches = content.split("\n")
    for match in matches:
        if match in ["A Y", "B Z", "C X"]:
            my_points += 6
        elif match in ["A X", "B Y", "C Z"]:
            my_points += 3
    return my_points
