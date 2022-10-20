"""Tests of solution.py"""


import pytest
import solution


def test_students_study_night():
    assert solution.students_study(1, True) is False
    assert solution.students_study(1, False) is False
    assert solution.students_study(4, True) is False
    assert solution.students_study(4, False) is False


def test_students_study_day():
    assert solution.students_study(5, True) is True
    assert solution.students_study(5, False) is False
    assert solution.students_study(17, True) is True
    assert solution.students_study(17, False) is False


def test_students_study_evening():
    assert solution.students_study(18, True) is True
    assert solution.students_study(18, False) is True
    assert solution.students_study(24, True) is True
    assert solution.students_study(24, False) is True


def test_lottery_all_fives():
    assert solution.lottery(5, 5, 5) == 10


def test_lottery_same_numbers():
    assert solution.lottery(3, 3, 3) == 5
    assert solution.lottery(17, 17, 17) == 5
    assert solution.lottery(-6, -6, -6) == 5
    assert solution.lottery(0, 0, 0) == 5


def test_lottery_two_numbers_same():
    assert solution.lottery(5, 5, 4) == 0
    assert solution.lottery(1, 10, 1) == 0
    assert solution.lottery(6, 8, 8) == 1
    assert solution.lottery(6, 3, 23) == 1


def test_fruit_basket_zero():
    assert solution.fruit_order(0, 0, 0) == 0
    assert solution.fruit_order(0, 4, 0) == 0
    assert solution.fruit_order(3, 0, 0) == 0
    assert solution.fruit_order(2, 4, 0) == 0


def test_fruit_basket_large_exactly_enough():
    assert solution.fruit_order(0, 3, 15) == 0


def test_fruit_basket_large_not_enough():
    assert solution.fruit_order(10, 1, 12) == 7
    assert solution.fruit_order(2, 1, 12) == -1
    assert solution.fruit_order(12, 1, 15) == 10
    assert solution.fruit_order(2, 1, 15) == -1


def test_fruit_basket_large_more_than_enough():
    assert solution.fruit_order(3, 5, 7) == 2
    assert solution.fruit_order(1, 5, 7) == -1



