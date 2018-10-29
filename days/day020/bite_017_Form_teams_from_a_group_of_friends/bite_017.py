import itertools

def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return list(itertools.permutations(friends, team_size))
    return list(itertools.combinations(friends, team_size))