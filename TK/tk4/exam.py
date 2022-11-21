"""TK4."""


def string_edges(first: str, second: str) -> str:
    """
    Given two strings return a string which consists of the last elements of input strings.

    The strings will have length 1 or more.

    string_edges("abc", "def") => "cf"
    string_edges("a", "b") => "ab"
    """
    return first[-1] + second[-1]


def is_sum_of_two(a: int, b: int, c: int) -> bool:
    """
    Whether one parameter is a sum of other two.

    is_sum_of_two(3, 2, 1) => True
    is_sum_of_two(3, 1, 1) => False
    is_sum_of_two(3, 2, 5) => True
    """
    return a + b == c or b + c == a or a + c == b


def middle_chars(s: str) -> str:
    """Return two chars in the middle of string.

    The length of the string is an even number.

    middle_chars("abcd") => "bc"
    middle_chars("bc") => "bc"
    middle_chars("aabbcc") => "bb"
    middle_chars("") => ""
    """
    return s[len(s) // 2 - 1] + s[len(s) // 2]


def index_index_value(nums: list) -> int:
    """
    Return value at index.

    Take the last element.
    Use the last element value as the index to get another value.
    Use this another value as the index of yet another value.
    Return this yet another value.

    If the last element points to out of list, return -1.
    If the element at the index of last element points out of the list, return -2.

    All elements in the list are non-negative.

    index_index_value([0]) => 0
    index_index_value([0, 2, 4, 1]) => 4
    index_index_value([0, 2, 6, 2]) => -2  (6 is too high)
    index_index_value([0, 2, 4, 5]) => -1  (5 is too high)

    :param nums: List of integer
    :return: Value at index of value at index of last element's value
    """
    if nums[-1] >= len(nums):
        return -1
    elif nums[nums[-1]] >= len(nums):
        return -2
    else:
        return nums[nums[-1]]


def count_clumps(nums: list) -> int:
    """
    Return the number of clumps in the given list.

    Say that a "clump" in a list is a series of 2 or more adjacent elements of the same value.

    count_clumps([1, 2, 2, 3, 4, 4]) → 2
    count_clumps([1, 1, 2, 1, 1]) → 2
    count_clumps([1, 1, 1, 1, 1]) → 1
    count_clumps([1, 2, 3]) → 0

    :param nums: List of integers.
    :return: Number of clumps.
    """
    clumps = 0
    other_list = nums[0:2]
    if other_list[0] == other_list[-1]:
        clumps += 1
    for num in nums[2:]:
        if num == other_list[-1]:
            if num == other_list[-2]:
                continue
            else:
                clumps += 1
        other_list.append(num)
    return clumps


if __name__ == '__main__':
    print(count_clumps([1, 2, 3]))
