from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def inner(user):
        if not user in known_users:
            result = f'please create an account'
        elif not user in loggedin_users:
            result = f'please login'
        else:
            result = func(user)
        return result
    return inner


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'


if __name__ == "__main__":
    for user in known_users + ['alex', 'nata']:
        print(welcome(user))