import re
from sys import argv


file_old, file_new = argv[1:]


def remove_version(file_old, file_new):
    with open(file_old, 'r') as f_old, open(file_new, 'w') as f_new:
        regex = (r'(\S+)==.*')
        for line in f_old:
            match = re.search(regex, line)
            f_new.write(match.group(1) + '\n')
    return None


if __name__ == "__main__":
    remove_version(file_old, file_new)
