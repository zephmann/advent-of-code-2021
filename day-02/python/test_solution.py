
import pytest

import solution


@pytest.mark.parametrize(
    "movements, expected",
    [
        (["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"], 150),
        (["forward 5", "forward 8", "forward 2"], 0),
        (["up 5", "down 5"], 0),
        (["up 5", "forward 5"], -25),
        ([], 0)
    ]
)
def test_solution(movements, expected):
    result = solution.move_submarine(movements)
    assert result == expected
