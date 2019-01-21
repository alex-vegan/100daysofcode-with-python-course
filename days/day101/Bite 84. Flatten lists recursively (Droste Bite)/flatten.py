def flatten(list_of_lists):
    flat_list = []
    for element in list_of_lists:
        if type(element) in [int, str]:
            flat_list.append(element)
        elif type(element) in [list, tuple]:
            flat_list.extend(flatten(element))
    return flat_list


if __name__ == "__main__":
    list_of_lists = [1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]
    print(flatten(list_of_lists))
