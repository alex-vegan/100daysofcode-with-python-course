from miller import py2_earth_hours_left, py2_miller_min_left


def test_py2_earth_hours_left():
    assert py2_earth_hours_left() == 18600.6


def test_py2_miller_min_left():
    assert py2_miller_min_left() == 18.2