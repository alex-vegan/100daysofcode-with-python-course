programmers = {'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
               'paul': ['C++', 'JS', 'Python'],
               'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
               'tim': ['Python', 'Haskell', 'C++', 'JS'],
               'sue': ['Scala', 'Python'],
               'fabio': ['PHP']}


def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    programmers_list = [set(v) for v in programmers.values()]
    result = programmers_list[0]
    for programmer in programmers_list[1:]:
        result &= programmer
    return sorted(list(result))


if __name__ == "__main__":
    print(common_languages(programmers))
