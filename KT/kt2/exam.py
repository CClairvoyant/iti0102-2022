"""KT2."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    return s[-2:] + s[2:-2] + s[:2] if len(s) >= 4 else s[::-1]


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    take_partial("Hello world", 3, 3) => "lo ld"
    """
    if text:
        return text[leave_count:][:take_count] + take_partial(text[leave_count + take_count:], leave_count, take_count)
    return ""


def min_diff(nums: list) -> int:
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    nums.sort()
    smallest_diff = abs(nums[0] - nums[-1])
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) < smallest_diff:
            smallest_diff = abs(nums[i] - nums[i - 1])
    return smallest_diff


def get_symbols_by_occurrences(text: str) -> dict:
    """
    Return dict where key is the occurrence count and value is a list of corresponding symbols.

    The order of the counts and the symbols is not important.

    get_symbols_by_occurrences("hello") => {1: ['e', 'o', 'h'], 2: ['l']}
    get_symbols_by_occurrences("abcaba") => {2: ['b'], 1: ['c'], 3: ['a']}
    """
    occurrences = {}
    for letter in set(text):
        if text.count(letter) in occurrences:
            occurrences[text.count(letter)].append(letter)
        else:
            occurrences[text.count(letter)] = [letter]
    return occurrences


if __name__ == '__main__':
    print(switch_lasts_and_firsts("ambulance"))  # => "cebulanam"
    print(switch_lasts_and_firsts("firetruck"))  # => "ckretrufi"
    print(switch_lasts_and_firsts("car"))  # => "rac"

    print(take_partial("abcdef", 2, 3))  # => "cde"
    print(take_partial("abcdef", 0, 1))  # => "abcdef"
    print(take_partial("abcdef", 1, 0))  # => ""
    print(take_partial("Hello world", 3, 3))  # => "lo ld"

    print(min_diff([1, 2, 3]))  # => 1
    print(min_diff([1, 9, 17]))  # => 8
    print(min_diff([100, 90]))  # => 10
    print(min_diff([1, 100, 1000, 1]))  # => 0

    print(get_symbols_by_occurrences("hello"))  # => {1: ['e', 'o', 'h'], 2: ['l']}
    print(get_symbols_by_occurrences("abcaba"))  # => {2: ['b'], 1: ['c'], 3: ['a']}
