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
    assert solution.lottery(5, 5, 5) is 10


def test_lottery_same_numbers():
    assert solution.lottery(3, 3, 3) is 5
    assert solution.lottery(17, 17, 17) is 5
    assert solution.lottery(-6, -6, -6) is 5
    assert solution.lottery(0, 0, 0) is 5


def test_lottery_two_numbers_same():
    assert solution.lottery(5, 5, 4) is 0
    assert solution.lottery(1, 10, 1) is 0
    assert solution.lottery(6, 8, 8) is 1
    assert solution.lottery(6, 3, 23) is 1
