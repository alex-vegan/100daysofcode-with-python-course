from sys import argv


file_old, file_new, file_diff = argv[1:]


def diff_files(file_old, file_new, file_diff):
    with open(file_old, 'r') as f_old, open(file_new, 'r') as f_new, open(file_diff, 'w') as f_diff:
        for old_line in f_old:
            new_line = f_new.readline()
            if old_line.strip() != new_line.strip():
                f_diff.write(f'{old_line.strip():20} >>> {new_line.strip():20}\n')
    return None


if __name__ == "__main__":
    diff_files(file_old, file_new, file_diff)
