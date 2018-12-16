"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request
import re

# prep
tempfile = os.path.join('/tmp', 'dirnames')
urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)
IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()
users, popular_challenges = Counter(), Counter()
Stats = namedtuple('Stats', 'user challenge')

# code
def gen_files():
    """Return a generator of dir names reading in `tempfile`
       `tempfile` has this format:
       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True
       -> use last column to filter out directories (= True)
    """
    regex = r'(\d+)\/(\S+),(False|True)'
    with open(tempfile) as f:
        for line in f:
            line_list = line.strip().split(',')
            is_dir = line_list[-1]
            if is_dir == 'True':
                match = re.search(regex, line)
                popular_challenges[match.group(1)] += 1
                yield line_list[0].split('/')[-1]
            else:
                continue



def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    g = gen_files()
    for user in g:
        if user not in IGNORE:
            users[user] += 1
    user = users.most_common(1)[0][0]
    challenge = popular_challenges.most_common(1)[0]
    return Stats(user=user, challenge=challenge)
