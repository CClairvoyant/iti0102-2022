import pytest
import solution


def test_solve_test():
    assert solution.students_study(19, False) is True
    assert solution.students_study(1, True) is False
    assert solution.students_study(20, True) is True
    assert solution.students_study(16, False) is False
    assert solution.students_study(15, True) is True
    assert solution.students_study(2, False) is False
