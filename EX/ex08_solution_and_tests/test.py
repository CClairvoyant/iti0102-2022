import pytest
import solution


def test_solve_test():
    assert solution.students_study(18, False) is True
    assert solution.students_study(1, True) is False
    assert solution.students_study(18, True) is True
    assert solution.students_study(17, False) is False
    assert solution.students_study(5, True) is True
    assert solution.students_study(4, False) is False
    assert solution.students_study(1, False) is False
    assert solution.students_study(4, True) is False
    assert solution.students_study(5, False) is False
    assert solution.students_study(17, True) is True
    assert solution.students_study(24, False) is True
    assert solution.students_study(24, True) is True
