def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    removable_chars = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    result = [char for char in input_string if char not in removable_chars]
    return ''.join(result)