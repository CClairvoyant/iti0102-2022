"""Day 1 part 1."""


def part_1(filename: str):
    """Sum list."""
    with open(filename, "r") as data:
        content = data.read()
    content_list = content.split("\n\n")
    content_list = list(map(lambda x: x.split("\n"), content_list))
    for i in range(len(content_list)):
        content_list[i] = sum(list(map(int, content_list[i])))
    content_list.sort(reverse=True)
    return content_list[0]
