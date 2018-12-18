from string import digits

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case,
       one twist: numbers have to appear after letters!"""
    digit_words = []
    letter_words = [] 
    for word in words:
        if word[0] in digits:
            digit_words.append(word)
        else:
            letter_words.append(word)
    sorted_letter_words = sorted(letter_words, key=lambda x:x.lower())
    sorted_digit_words = sorted(digit_words)
    return sorted_letter_words + sorted_digit_words
        
               
        