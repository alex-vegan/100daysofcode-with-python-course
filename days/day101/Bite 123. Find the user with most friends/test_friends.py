from friends import get_friend_with_most_friends


def test_get_friend_with_most_friends_default_arg():
    user, friends = get_friend_with_most_friends()
    assert user == 'sara'
    assert sorted(list(friends)) == ['joyce', 'kevin', 'nick', 'rod']


def test_get_friend_with_most_friends_different_friendship_data():
    friendships = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
                   (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
                   (6, 7), (6, 8), (6, 9)]
    user, friends = get_friend_with_most_friends(friendships)
    assert user == 'joyce'
    assert sorted(list(friends)) == ['beverly', 'julian', 'kevin', 'nick',
                                     'rod', 'sara']