import pytest

from non_ascii import extract_non_ascii_words


@pytest.mark.parametrize("phrase, expected", [
    ('An preost wes on leoden, La?amon was ihoten', ['La?amon']),
    ('He wes Leovena?es sone -- li?e him be Drihten', ['Leovena?es', 'li?e']),
    ('He wonede at Ernle?e at ??elen are chirechen', ['Ernle?e', '??elen']),
    ('Uppen Sevarne sta?e, sel ?ar him ?uhte', ['sta?e,', '?ar', '?uhte']),
    ('Onfest Radestone, ?er he bock radde', ['?er']),
    ('Fichier non trouve', ['trouve']),
    ('Over \u0e55\u0e57 57 flavours', ['??']),
    ('Si ... habra que saber algo de Unicode, ?no?', ['Si', 'habra', '?no?']),
    ('This string only contains ascii words', []),
])
def test_extract_non_ascii_words(phrase, expected):
    assert extract_non_ascii_words(phrase) == expected