
import pytest

import solution2


@pytest.mark.parametrize(
    "movements, expected",
    [
        (
            [
                "00100", "11110", "10110", "10111", "10101", "01111",
                "00111", "11100", "10000", "11001", "00010", "01010",
            ],
            230
        ),
        (["11", "00"], 0),
        ([], 0),
    ]
)
def test_solution(movements, expected):
    result = solution2.calc_life_support(movements)
    assert result == expected
