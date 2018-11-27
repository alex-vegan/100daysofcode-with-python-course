def get_profile(*args, name='julian', profession='programmer', **kwargs):
    if len(args) != 0 or len(kwargs) != 0:
        raise TypeError('awaited couple named args "name" & "pafession" only')
    return f'{name} is a {profession}'