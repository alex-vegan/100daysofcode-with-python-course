from score import Score


def test_enum_content():
    assert list(Score) == [Score.BEGINNER, Score.INTERMEDIATE,
                           Score.ADVANCED, Score.CHEATED]


def test_equality_comparison():
    assert Score.BEGINNER is Score.BEGINNER
    assert Score.INTERMEDIATE is not Score.ADVANCED


def test_str_using_thumbsup():
    assert str(Score.BEGINNER) == 'BEGINNER => ????'
    assert str(Score.INTERMEDIATE) == 'INTERMEDIATE => ??????'
    assert str(Score.ADVANCED) == 'ADVANCED => ????????'
    assert str(Score.CHEATED) == 'CHEATED => ??'


def test_average():
    assert Score.average() == 2.5