
import pytest

import solution2


@pytest.mark.parametrize(
    "readings, expected",
    [
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5),
        (list(range(10)), 7),
        (list(range(10, 0, -1)), 0),
        ([1, 2, 3], 0),
        ([], 0),
    ]
)
def test_solution(readings, expected):
    result = solution2.count_depth_increases(readings)
    assert result == expected
