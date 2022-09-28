"""Example TK."""


def workday_count(days: int) -> int:
    """
    Given number of days.

    Return how many of these days are workdays.
    Workdays are first five days of the weeks, last two are not.
    Always start from the start of the week.

    workday_count(9) => 7
    workday_count(3) => 3
    workday_count(7) => 5
    workday_count(15) => 11

    :param days: given number of days
    :return: workdays in given days
    """
    if days < 6:
        return days
    elif days % 7 == 6:
        return days // 7 * 5 + days % 7 - 1
    else:
        return days // 7 * 5 + days % 7


def sorta_sum(a: int, b: int) -> int:
    """
    Given 2 ints, a and b, return their sum.

    However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

    sorta_sum(3, 4) → 7
    sorta_sum(9, 4) → 20
    sorta_sum(10, 11) → 21

    :param a: Integer
    :param b: Integer
    :return: Sum or 20
    """
    if a + b in range(10, 20):
        return 20
    else:
        return a + b


def extra_end(s: str) -> str:
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.

    The string length will be at least 2.

    extra_end('Hello') → 'lololo'
    extra_end('ab') → 'ababab'
    extra_end('Hi') → 'HiHiHi'

    :param s: Input string
    :return: 3 copies of last 2 chars.
    """
    return s[-2:] * 3


def last_indices_elements_sum(nums: list) -> int:
    """
    Return sum of elements at indices of last two elements.

    Take element at the index of the last element value
    and take element at the index of the previous element value.
    Return the sum of those two elements.

    If the index for an element is out of the list, use 0 instead.

    The list contains at least 2 elements.

    last_indices_elements_sum([0, 1, 2, 0]) => 2 (0 + 2)
    last_indices_elements_sum([0, 1, 1, 7]) => 1 (just 1)
    last_indices_elements_sum([0, 1, 7, 2]) => 7 (just 7)
    last_indices_elements_sum([0, 1, 7, 8]) => 0 (indices too large, 0 + 0)

    :param nums: List of non-negative integers.
    :return: Sum of elements at indices of last two elements.
    """

    if nums[-1] < len(nums) and nums[-2] < len(nums):
        return nums[nums[-1]] + nums[nums[-2]]
    elif nums[-1] < len(nums):
        return nums[nums[-1]]
    elif nums[-2] < len(nums):
        return nums[nums[-2]]
    else:
        return 0


def divisions(numbers: list) -> int:
    """
    You are given a list of unique integers.

    Find how many pairs of numbers there are in that list, such that for each pair, one of it's members is divisible by
    the other.

    Note that "n and m" is considered the same pair as "m and n".

    divisions([]) => 0
    divisions([5]) => 0

    divisions([3, 14, 12, 6]) => 3 (The pairs are {3, 12}, {3, 6} and {12, 6})
    divisions([2, 3, 8]) => 1 (The only valid pair is {2, 8})
    divisions([25, 22, 4, 400, 50]) => 4 (The pairs are {25, 400}, {25, 50}, {4, 400} and {400, 50})

    divisions([5, 7, 1]) => 2 (The pairs are {5, 1} and {7, 1})

    :param numbers: List of integers
    :return: Amount of pairs
    """
    amount_of_pairs = 0
    for i in numbers:
        for n in range(len(numbers)):
            if i != numbers[n] and i % numbers[n] == 0:
                amount_of_pairs += 1
    return amount_of_pairs
