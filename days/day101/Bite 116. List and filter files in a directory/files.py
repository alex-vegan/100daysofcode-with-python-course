import os
import glob

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""

    list_of_files = os.listdir(dirname)
    #list_files = glob.glob('*')
    sized_list_of_files = []
    for file in list_of_files:
        file_path = os.path.join(dirname, file)
        statinfo = os.stat(file_path)
        file_size = statinfo.st_size
        if file_size // ONE_KB >= size_in_kb:
            sized_list_of_files.append(file)
    return sized_list_of_files

if __name__ == "__main__":
    current_dir = '.'
    print(get_files(current_dir, 0))
