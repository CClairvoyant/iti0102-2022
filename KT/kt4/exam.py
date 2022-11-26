"""KT4."""


def two_digits_into_list(nr: int) -> list:
    """
    Return list of digits of 2-digit number.

    two_digits_into_list(11) => [1, 1]
    two_digits_into_list(71) => [7, 1]

    :param nr: 2-digit number
    :return: list of length 2
    """
    return [int(str(nr)[0]), int(str(nr)[1])]


def sum_elements_around_last_three(nums: list) -> int:
    """
    Find sum of elements before and after last 3 in the list.

    If there is no 3 in the list or list is too short
    or there is no element before or after last 3 return 0.

    Note if 3 is last element in the list you must return
    sum of elements before and after 3 which is before last.


    sum_elements_around_last_three([1, 3, 7]) -> 8
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) -> 9
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) -> 5
    sum_elements_around_last_three([1, 2, 3]) -> 0

    :param nums: given list of ints
    :return: sum of elements before and after last 3
    """
    if nums[1:-1].count(3) == 0:
        return 0
    elif nums[::-1].index(3) == 0:
        return nums[-nums[-2::-1].index(3) - 3] + nums[-nums[-2::-1].index(3) - 1]
    else:
        return nums[-nums[::-1].index(3) - 2] + nums[-nums[::-1].index(3)]


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    new_s = ""
    largest_block = 0
    current_block = 0
    if s:
        current_block += 1
    while s:
        new_s += s[0]
        s = s[1:]
        if s and s[0] == new_s[-1]:
            current_block += 1
        else:
            if current_block > largest_block:
                largest_block = current_block
            current_block = 1
    return largest_block


def create_dictionary_from_directed_string_pairs(pairs: list) -> dict:
    """
    Create dictionary from directed string pairs.

    One pair consists of two strings and "direction" symbol ("<" or ">").
    The key is the string which is on the "larger" side,
    the value is the string which is on the "smaller" side.

    For example:
    ab>cd => "ab" is the key, "cd" is the value
    kl<mn => "mn" is the key, "kl" is the value

    The input consists of list of such strings.
    The output is a dictionary, where values are lists.
    Each key cannot contain duplicate elements.
    The order of the elements in the values should be
    the same as they appear in the input list.

    create_dictionary_from_directed_string_pairs([]) => {}

    create_dictionary_from_directed_string_pairs(["a>b", "a>c"]) =>
    {"a": ["b", "c"]}

    create_dictionary_from_directed_string_pairs(["a>b", "a<b"]) =>
    {"a": ["b"], "b": ["a"]}

    create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]) =>
    {"1": ["1", "2"]}
    """
    d = {}
    for pair in pairs:
        if len(pair.split(">")) == 2:
            if pair.split(">")[0] not in d:
                d[pair.split(">")[0]] = [pair.split(">")[-1]]
            elif pair.split(">")[0] in d and pair.split(">")[-1] not in d[pair.split(">")[0]]:
                d[pair.split(">")[0]].append(pair.split(">")[-1])
        elif len(pair.split("<")) == 2:
            if pair.split("<")[-1] not in d:
                d[pair.split("<")[-1]] = [pair.split("<")[0]]
            elif pair.split("<")[-1] in d and pair.split("<")[0] not in d[pair.split("<")[-1]]:
                d[pair.split("<")[-1]].append(pair.split("<")[0])
    return d


if __name__ == '__main__':
    assert two_digits_into_list(11) == [1, 1]
    assert two_digits_into_list(71) == [7, 1]

    assert sum_elements_around_last_three([1, 3, 7]) == 8
    assert sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) == 9
    assert sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) == 5
    assert sum_elements_around_last_three([1, 2, 3]) == 0

    assert max_block("hoopla") == 2
    assert max_block("abbCCCddBBBxx") == 3
    assert max_block("") == 0

    assert create_dictionary_from_directed_string_pairs([]) == {}
    assert create_dictionary_from_directed_string_pairs(["a>b", "a>c"]) == {"a": ["b", "c"]}
    assert create_dictionary_from_directed_string_pairs(["a>b", "a<b"]) == {"a": ["b"], "b": ["a"]}
    assert create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]) == {"1": ["1", "2"]}
