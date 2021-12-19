
import pytest

import solution


@pytest.mark.parametrize(
    "fish_ages, num_days, expected",
    [
        ([3, 4, 3, 1, 2], 18, 26),
        ([3, 4, 3, 1, 2], 80, 5934),
        ([6], 7, 2),
        ([7], 1, 1),
        ([], 1, 0),
        ([0], 1, 2),
    ]
)
def test_solution(fish_ages, num_days, expected):
    result = solution.count_fish(fish_ages, num_days)
    assert result == expected
