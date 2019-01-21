from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

class UserDoesNotExist(Exception):
    pass

class UserAccessExpired(Exception):
    pass

class UserNoPermission(Exception):
    pass

def get_secret_token(username):
    if not username in [u.name for u in USERS]:
        raise UserDoesNotExist
    elif [u.expired for u in USERS if u.name == username][0]:
        raise UserAccessExpired
    elif [u.role != ADMIN for u in USERS if u.name == username][0]:
        raise UserNoPermission
    return SECRET