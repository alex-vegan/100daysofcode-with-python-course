
from github import Github
g = Github()
rep = g.get_repo('talkpython/100daysofcode-with-python-course')
file_cont = rep.get_file_contents('days/07-09-data-structures/code/data.py')
file = (file_cont.decoded_content).decode('utf-8')
with open('data.py', 'w') as f:
    f.write(file)
from data import us_state_abbrev, states_list


NOT_FOUND = 'N/A'


def get_every_nth_state(states=states_list, n=10):
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)"""
    return states[n-1::n]


def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    try:
        return us_state_abbrev[state_name]
    except KeyError:
        return NOT_FOUND


def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
    if type(data) == dict:
        state_list = data.keys()
    else:
        state_list = data
    max_len = max([len(state) for state in state_list])
    for state in state_list:
        if len(state) == max_len:
            return state


def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
                                          states=states_list):
    """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list without losing
       alphabetical order"""
    result_list = []
    state_abrs = list(us_state_abbrev.values())
    state_abrs.sort()
    result_list.extend(state_abrs[:10])
    state = states[::]
    state.sort()
    result_list.extend(state[-10:])
    return result_list


'''
if __name__ == '__main__':
    print(states_list[9::10])
    print({key:us_state_abbrev[key] for key in list(us_state_abbrev.keys())[9::10]})
    print(sorted(list(us_state_abbrev.keys()))[45])
    print(sorted(list(us_state_abbrev.values()))[27])
'''
