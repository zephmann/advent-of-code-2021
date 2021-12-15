
import pytest

import solution


@pytest.mark.parametrize(
    "readings, expected",
    [
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7),
        (list(range(10)), 9),
        (list(range(10, 0, -1)), 0),
        ([], 0)
    ]
)
def test_solution(readings, expected):
    result = solution.count_depth_increases(readings)
    assert result == expected
