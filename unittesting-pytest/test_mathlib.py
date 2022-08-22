import mathlib
import pytest
import sys


def test_calc_total():
    total = mathlib.calc_add(4, 5)
    assert total == 9


def test_calc_multiply():
    result = mathlib.calc_multiply(4, 5)
    assert result == 20


def test_dummy():
    assert True


# for skipping test
# @pytest.mark.skip(reason="I don't want to test at this moment.")
# skip if
# @pytest.mark.skip(sys.version_info > (3, 5), reason="I don't want to test at this moment.")
# def test_calc_total():
#     total = mathlib.calc_add(4, 5)
#     assert total == 9


# based on OS
@pytest.mark.windows
def test_windows():
    assert True


@pytest.mark.mac
def test_mac():
    assert True


@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output
