
import pytest

import solution2


@pytest.mark.parametrize(
    "values, expected",
    [
        (
            "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab",
            {
                "abcdefg": 8,
                "bcdef": 5,
                "acdfg": 2,
                "abcdf": 3,
                "abd": 7,
                "abcdef": 9,
                "bcdefg": 6,
                "abef": 4,
                "abcdeg": 0,
                "ab": 1,
            }
        ),
        (
            "gd deg cdag cfade gaebf fdaeg gdcaef ebacdf cbdefg gfdabec",
            {
                "dg": 1,
                "deg": 7,
                "acdg": 4,
                "acdef": 5,
                "abefg": 2,
                "adefg": 3,
                "acdefg": 9,
                "abcdef": 6,
                "bcdefg": 0,
                "abcdefg": 8,
            }
        ),
    ]
)
def test_find_digits(values, expected):
    result = solution2._find_digits(values.split())
    assert result == expected
