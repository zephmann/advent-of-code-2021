
import pytest

import solution2


@pytest.mark.parametrize(
    "positions, expected",
    (
        ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 168),
        ([2, 3, 5, 6], 8),  # 3 + 1 + 1 + 3
        # test input is 94862124
    )
)
def test_solution(positions, expected):
    result = solution2.find_fuel_cost(positions)
    assert result == expected
