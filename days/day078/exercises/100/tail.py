def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath) as f:
        file = f.read()
        tail_result = file.split('\n')[-n:]
    return tail_result