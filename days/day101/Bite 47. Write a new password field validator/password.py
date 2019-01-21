import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())

def validate_password(password):
    validator = {'leng':False,'digit':False,'lowch':False,'upch':False,'punc':False,'unused':False}
    _lowch = False
    if len(password) > 5 and len(password) < 13:
        validator['leng'] = True
    for char in list(password):
        if char in string.digits:
            validator['digit'] = True
        if char in string.ascii_lowercase and _lowch:
            validator['lowch'] = True
        if char in string.ascii_lowercase:
            _lowch = True
        if char in string.ascii_uppercase:
            validator['upch'] = True
        if char in string.punctuation:
            validator['punc'] = True
    if not password in used_passwords:
        validator['unused'] = True
    result = all(validator.values())
    if result:
        used_passwords.add(password)
    return result
        