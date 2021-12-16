
import pytest

import solution2


@pytest.mark.parametrize(
    "movements, expected",
    [
        (["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"], 900),
        (["forward 5", "forward 8", "forward 2"], 0),
        (["up 5", "up 5"], 0),
        (["down 5", "down 5"], 0),
        (["up 5", "down 5"], 0),
        (["forward 5", "up 5"], 0),
        (["up 5", "forward 5"], -125),
        (["down 5", "forward 5"], 125),
        ([], 0),
    ]
)
def test_solution(movements, expected):
    result = solution2.move_submarine(movements)
    assert result == expected
