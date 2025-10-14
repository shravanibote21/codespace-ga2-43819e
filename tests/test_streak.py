import pytest
from streak import longest_positive_streak

@pytest.mark.parametrize("nums, expected", [
    ([], 0),
    ([1, 2, 3, 4, 5], 5),
    ([-1, -2, -3], 0),
    ([0, 0, 0], 0),
    ([1, 2, 0, 4, 5, 6], 3),
    ([1, 2, -1, 4, 5, 6, 7], 4),
    ([1, 0, 2, 0, 3, 0, 4], 1),
    ([1, 2, 3, 0, 1, 2], 3),
    ([0, 1, 2, 3, 4, 0], 4),
    ([1], 1),
    ([0], 0),
    ([-1], 0),
])
def test_longest_positive_streak(nums, expected):
    """
    Tests the longest_positive_streak function with various inputs.
    """
    assert longest_positive_streak(nums) == expected