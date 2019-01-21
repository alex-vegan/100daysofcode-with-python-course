from string import printable

def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    non_ascii_list = []
    for word in text.split():
        for letter in word.lower():
            if not letter in printable:
                non_ascii_list.append(word)
                break
    return non_ascii_list


if __name__ == "__main__":
    print(extract_non_ascii_words('This string only contains ascii words'))