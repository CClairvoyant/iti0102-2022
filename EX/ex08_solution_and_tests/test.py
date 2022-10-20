import pytest
import solution


def test_solve_test():
    assert solution.students_study(19, False) is True
    assert solution.students_study(1, True) is False
