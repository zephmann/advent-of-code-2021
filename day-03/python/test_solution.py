
import pytest

import solution


@pytest.mark.parametrize(
    "readings, expected",
    [
        (
            [
                "00100", "11110", "10110", "10111", "10101", "01111",
                "00111", "11100", "10000", "11001", "00010", "01010",
            ],
            198
        ),
        (["10", "10", "10"], 2),  # 10 * 01 -> 2 * 1 -> 2
        (["100", "100", "100"], 12),  # 100 * 011 -> 4 * 3 -> 12
        ([], 0),
    ]
)
def test_solution(readings, expected):
    result = solution.calc_power_level(readings)
    assert result == expected
