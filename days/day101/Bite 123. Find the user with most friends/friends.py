from collections import defaultdict


names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]

friendships2 = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
                   (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
                   (6, 7), (6, 8), (6, 9)]

def get_friend_with_most_friends(friendships=friendships):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    friend_dict = defaultdict(set)
    for friend1, friend2 in friendships:
        friend_dict[friend1].add(friend2)
        friend_dict[friend2].add(friend1)
    friend, friend_set = max(friend_dict.items(), key=lambda x: len(x[1]))
    friend_list = [users[fr] for fr in friend_set] 
    return (users[friend], friend_list)


if __name__ == "__main__":
    #print(users)
    print(get_friend_with_most_friends(friendships2))