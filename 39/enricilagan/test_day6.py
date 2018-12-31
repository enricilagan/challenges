from day6 import calc_word_value
import pytest


@pytest.mark.parametrize("word, score", [
    ('dog', 5),
    ('cat', 5),
    ('flamingo', 14),
    ('hero', 7)
])
def test_calc_word_value(word, score):
    assert calc_word_value(word) == score
