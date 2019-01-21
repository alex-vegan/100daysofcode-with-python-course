import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
#color_values_module = os.path.join('/tmp', 'color_values.py')
#urllib.request.urlretrieve('https://bit.ly/2MSuu4z', color_values_module)
#sys.path.append('/tmp')

color_values_module = 'color_values.py'

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self._color = color
        self.rgb = None
        if color.upper() in COLOR_NAMES.keys():
            self.rgb = COLOR_NAMES[color.upper()]

    @classmethod
    def hex2rgb(cls, hex_value):
        """Class method that converts a hex value into an rgb one"""
        return (int(hex_value[1:3], 16), int(hex_value[3:5], 16), int(hex_value[5:7], 16))

    @classmethod
    def rgb2hex(cls, rgb_value):
        """Class method that converts an rgb value into a hex one"""
        try:
            result = '#{:02x}{:02x}{:02x}'.format(*rgb_value)
        except:
            raise ValueError("Unknown format")
        if not all([0 <= item <= 255 for item in rgb_value]):
            raise ValueError("Range overflowed")
        return result

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self._color.lower()}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb:
            return str(self.rgb)
        else:
            return 'Unknown'