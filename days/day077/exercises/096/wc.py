def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        file = f.read().strip()
        char_nums = len(file)
        lines = file.split('\n')
        line_nums = len(lines)
        word_nums = 0
        for line in lines:
            words = line.split()
            word_nums += len(words)
    return f'{line_nums} {word_nums} {char_nums} {file_}'
        
            
        
        