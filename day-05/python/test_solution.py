
import pytest

import solution


@pytest.mark.parametrize(
    "vent_lines, expected",
    [
        (
            [
                [0, 9, 5, 9],
                [8, 0, 0, 8],
                [9, 4, 3, 4],
                [2, 2, 2, 1],
                [7, 0, 7, 4],
                [6, 4, 2, 0],
                [0, 9, 2, 9],
                [3, 4, 1, 4],
                [0, 0, 8, 8],
                [5, 5, 8, 2]
            ],
            5
        ),
        (
            [
                [0, 1, 2, 1],  # horizontal line through middle
                [1, 0, 1, 2],  # vertical line through middle
                [0, 0, 2, 2]   # diagonal line through middle to be skipped
            ],
            1
        )
    ]
)
def test_solution(vent_lines, expected):
    result = solution.get_danger_areas(vent_lines)
    assert result == expected
