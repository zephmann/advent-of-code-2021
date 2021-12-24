
import pytest

import solution2


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], 0),
    ]
)
def test_solution(values, expected):
    result = solution2.calculate(values)
    assert result == expected
