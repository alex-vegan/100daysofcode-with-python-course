from functools import wraps


def int_args(func):
    @wraps(func)
    def inner(*args):
        if not all([type(arg) == int for arg in args]):
            raise TypeError
        if not all([arg >= 0 for arg in args]):
            raise ValueError
        return func(*args)
    return inner


def func(*args):
    ''' pure func '''
    pass


if __name__ == "__main__":
    func(1,2,3)
