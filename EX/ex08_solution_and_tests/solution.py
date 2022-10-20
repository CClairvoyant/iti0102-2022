"""Solutions of random tasks."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    return 18 <= time <= 24 or 5 <= time < 18 and coffee_needed


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10
    elif a == b == c:
        return 5
    elif b != a != c:
        return 1
    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if ordered_amount <= big_baskets * 5 + small_baskets:
        small_baskets_needed = ordered_amount - big_baskets * 5
        while small_baskets_needed < 0:
            small_baskets_needed += 5
        if small_baskets_needed > small_baskets:
            return -1
        else:
            return small_baskets_needed
    else:
        return -1


if __name__ == '__main__':
    print(fruit_order(10, 1, 13))  # -> 8
    print(fruit_order(1, 5, 21))  # -> 1
    print(fruit_order(5, 0, 6))  # -> -1
    print(fruit_order(10, 0, 9))  # -> 9
    print(fruit_order(4, 1, 9))  # -> 4
    print(fruit_order(3, 1, 10))  # -> -1
    print(fruit_order(1, 2, 7))  # -> -1
