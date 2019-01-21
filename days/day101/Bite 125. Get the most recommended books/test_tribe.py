from tribe import load_page, get_top_books

content = load_page()  # make sure we do this once!
books = get_top_books(content=content)


def test_books_6_occurrences():
    assert books[0] == 'Man’s Search For Meaning'


def test_books_5_occurrences():
    assert books[1] == 'Tao Te Ching'


def test_books_4_occurrences():
    assert sorted(books[2:5]) == ['Sapiens: A Brief History of Humankind',
                                  ('The 4-Hour Workweek: Escape the 9-5, Live '
                                   'Anywhere and Join the New Rich'),
                                  'The Fountainhead']  # 4x