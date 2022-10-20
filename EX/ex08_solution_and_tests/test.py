"""Tests of solution.py."""


import solution


def test_students_study_night():
    """Test function with nighttime's first and last hours."""
    assert solution.students_study(1, True) is False
    assert solution.students_study(1, False) is False
    assert solution.students_study(4, True) is False
    assert solution.students_study(4, False) is False


def test_students_study_day():
    """Test function with daytime's first and last hours."""
    assert solution.students_study(5, True) is True
    assert solution.students_study(5, False) is False
    assert solution.students_study(17, True) is True
    assert solution.students_study(17, False) is False


def test_students_study_evening():
    """Test function with evening's first and last hours."""
    assert solution.students_study(18, True) is True
    assert solution.students_study(18, False) is True
    assert solution.students_study(24, True) is True
    assert solution.students_study(24, False) is True


def test_lottery_all_fives():
    """Test function with jackpot numbers."""
    assert solution.lottery(5, 5, 5) == 10


def test_lottery_same_numbers():
    """Test function with a, b, c being the same, but not 5."""
    assert solution.lottery(3, 3, 3) == 5
    assert solution.lottery(17, 17, 17) == 5
    assert solution.lottery(-6, -6, -6) == 5
    assert solution.lottery(0, 0, 0) == 5


def test_lottery_two_numbers_same():
    """Test function with two numbers being the same and one being different."""
    assert solution.lottery(5, 5, 4) == 0
    assert solution.lottery(1, 10, 1) == 0
    assert solution.lottery(6, 8, 8) == 1


def test_lottery_all_different():
    """Test function with all numbers being different."""
    assert solution.lottery(6, 3, 23) == 1


def test_fruit_basket_zero():
    """Test function with ordered amount being zero."""
    assert solution.fruit_order(0, 0, 0) == 0
    assert solution.fruit_order(0, 4, 0) == 0
    assert solution.fruit_order(3, 0, 0) == 0
    assert solution.fruit_order(2, 4, 0) == 0


def test_fruit_basket_only_large():
    """Test function with no small baskets."""
    assert solution.fruit_order(0, 3, 15) == 0
    assert solution.fruit_order(0, 1, 10) == -1
    assert solution.fruit_order(0, 1, 12) == -1
    assert solution.fruit_order(0, 7, 15) == 0
    assert solution.fruit_order(0, 7, 11) == -1
    assert solution.fruit_order(0, 5, 7) == -1


def test_fruit_basket_only_small():
    """Test function with no large baskets."""
    assert solution.fruit_order(8, 0, 6) == 6
    assert solution.fruit_order(9, 0, 11) == -1
    assert solution.fruit_order(4, 0, 4) == 4
    assert solution.fruit_order(4, 0, 6) == -1
    assert solution.fruit_order(3, 0, 2) == 2


def test_fruit_basket_small_and_large():
    """Test function with various combinations of both baskets and ordered amount."""
    assert solution.fruit_order(3, 2, 13) == 3
    assert solution.fruit_order(2, 5, 12) == 2
    assert solution.fruit_order(8, 1, 16) == -1
    assert solution.fruit_order(8, 1, 12) == 7
    assert solution.fruit_order(6, 2, 12) == 2
    assert solution.fruit_order(2, 40, 123) == -1
    assert solution.fruit_order(4, 2, 7) == 2
    assert solution.fruit_order(2000, 3000, 16004) == 1004
