from enumerate_data import enumerate_names_countries
import re

expected_lines = [r'1. Julian\s+Australia',
                  r'2. Bob\s+Spain',
                  r'3. PyBites\s+Global',
                  r'4. Dante\s+Argentina',
                  r'5. Martin\s+USA',
                  r'6. Rodolfo\s+Mexico']


def test_enumerate_names_countries(capfd):
    enumerate_names_countries()
    output = capfd.readouterr()[0]
    for regex in expected_lines:
        assert re.search(regex, output)
