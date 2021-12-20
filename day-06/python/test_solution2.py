
import pytest

import solution2


@pytest.mark.parametrize(
    "fish_ages, num_days, expected",
    [
        ([3, 4, 3, 1, 2], 18, 26),
        ([3, 4, 3, 1, 2], 80, 5934),
        ([3, 4, 3, 1, 2], 256, 26984457539),
    ]
)
def test_solution(fish_ages, num_days, expected):
    result = solution2.count_fish(fish_ages, num_days)
    assert result == expected
