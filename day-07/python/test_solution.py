
import pytest

import solution


@pytest.mark.parametrize(
    "positions, expected",
    (
        ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 37),
        ([2, 3, 5], 3),
        ([7, 3, 10, 9, 1, 21, 7], 29),
        ([-1, -2, -3], 2),
        ([99, 100, 101], 2),
        ([49, 48, 47, 0, 0, 0, 50, 0, 1, 2, 3, 0, 0], 199),
    )
)
def test_solution(positions, expected):
    result = solution.find_fuel_cost(positions)
    assert result == expected
