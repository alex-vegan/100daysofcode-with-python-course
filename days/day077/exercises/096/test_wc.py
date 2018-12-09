import os
import re
from tempfile import NamedTemporaryFile

import pytest

from wc import wc

lines = [b'Hello world',
         b'Keep calm and code in Python',
         b'Have a nice weekend']


@pytest.mark.parametrize("some_text, expected", [
    (lines[0], '1 2 11'),
    (b'\n'.join(lines[:2]), '2 8 40'),
    (b'\n'.join(lines), '3 12 60'),
])
def test_wc(some_text, expected):
    with NamedTemporaryFile(dir='/tmp') as f:
        f.write(some_text)
        f.seek(0)  # need to go to start file
        output = wc(f.name)
        # replace tabs / multiple spaces by single space
        output = re.sub(r'\t|\s+', ' ', output)

        assert expected in output

        # file with/without path allowed
        assert f.name in output or os.path.basename(f.name) in output