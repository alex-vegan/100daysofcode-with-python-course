from functools import wraps


def make_html(element):
    '''decorator that wraps text inside html tag'''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{element}>{func(*args, **kwargs)}</{element}>'
        return wrapper
    return decorator


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text


if __name__ == '__main__':
    print(get_text('I code with PyBites'))