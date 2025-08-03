import pytest
from ml_models.utils import words_to_number


def test_words_to_number():
    assert words_to_number("hundred") == 100
    assert words_to_number("one hundred and twenty") == 120
    assert words_to_number("five hundred and twenty-three") == 523
    assert words_to_number('zero') == 0
    assert words_to_number('one') == 1
    assert words_to_number("twenty") == 20
    assert words_to_number("twenty-five") == 25
    assert words_to_number("one hundred") == 100
    assert words_to_number("a hundred") == 100
    assert words_to_number("one hundred and two") == 102
    assert words_to_number("five hundred forty two") == 542
    assert words_to_number("one thousand") == 1000
    assert words_to_number("one thousand two hundred thirty-four") == 1234
    assert words_to_number("seven million five hundred thousand") == 7500000
    # assert words_to_number("three billion two hundred million five hundred forty one thousand five hundred twenty two") == 3200541252
    # assert words_to_number("one hundred twenty three trillion") == 123000000000
    # assert words_to_number("one hundred and twenty three trillion") == 123000000000


if __name__ == "__main__":
    pytest.main()