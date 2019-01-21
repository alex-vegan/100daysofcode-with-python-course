from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

NT = namedtuple('NT', list(blog.keys()))

def dict2nt(dict_):
    return NT(**dict_)


def nt2json(nt):
    dt = dict(nt._asdict())
    dt['started'] = str(dt['started'])
    return json.dumps(dt)

if __name__ == "__main__":
    nt = dict2nt(blog)
    print(nt, type(nt).__base__)
    print('-'*42)
    print(dict(nt._asdict()))
    print('-'*42)
    jsn = nt2json(nt)
    print(jsn, type(jsn))
    print('-'*42)
    data = json.loads(jsn)
    print(data['started'][:4])
    print('-'*42)