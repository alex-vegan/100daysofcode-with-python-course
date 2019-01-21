def get_profile(*args, **kwargs):
    profile = {}
    if len(args) >= 2:
        profile['name'] = args[0]
    else:
        raise TypeError("need more args")
    if isinstance(args[1], int):
        profile['age'] = args[1]
    else:
        raise ValueError("isn't integer")
    if len(args) > 2 and len(args) < 8:
        profile['sports'] = sorted(list(args[2:]))
    if len(args) >= 8:
        raise ValueError("very much sports")
    if kwargs:
        profile['awards'] = kwargs
    return profile