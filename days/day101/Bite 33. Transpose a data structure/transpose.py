from collections import namedtuple

def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    NT = namedtuple('NT', 'key value')
    if type(data) is dict:
        nt_list = []
        for key,value in data.items():
            nt_list.append(NT(key=key, value=value))
        data = nt_list
    if type(data[0]).__base__ is tuple:
        return list(zip(*[list(nt) for nt in data]))
    