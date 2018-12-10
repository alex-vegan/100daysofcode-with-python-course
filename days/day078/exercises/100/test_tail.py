from tempfile import NamedTemporaryFile

from tail import tail

lines = [b'Hello world!',
         b'We hope that you are learning a lot of Python.',
         b'Have fun with our Bites of Py.',
         b'Keep calm and code in Python!',
         b'Become a PyBites ninja!']


def test_tail():
    with NamedTemporaryFile(dir='/tmp') as f:
        f.write(b'\n'.join(lines))
        f.seek(0)

        assert tail(f.name, 1) == ['Become a PyBites ninja!']
        assert tail(f.name, 2) == ['Keep calm and code in Python!',
                                   'Become a PyBites ninja!']

        # n of > file length basically gets the whole file, but need to do some
        # byte to str conversion and strip off last line's newline char
        expected = [line.decode("utf-8") for line in lines]
        assert tail(f.name, 10) == expected