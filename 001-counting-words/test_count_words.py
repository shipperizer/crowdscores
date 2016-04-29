# run this test by using py.test:
# (pip install pytest)
# $> py.test -k test_count_words

import pytest
from count_words import count_words


@pytest.mark.parametrize('lines, result', [
        (
            ['Little pig, let me come in.', 'No, no, no, no, not by the hair on my little chin chin.'],
            [('no', 4), ('chin', 2), ('little', 2)]
        ),
        (
            ['Lorem ipsum dolor sit amet,', 'consectetur adipiscing elit; *sed do eiusmod tempor incididunt'],
            [('adipiscing', 1), ('amet', 1), ('consectetur', 1)]
        )
    ]
)
def test_count_words(lines, result):
    expected_top_three = result
    assert count_words(lines)[:3] == expected_top_three
