def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    list1 = [letter for letter in word1.lower() if letter.isalnum()]
    list2 = [letter for letter in word2.lower() if letter.isalnum()]
    #print(sorted(list1))
    #print(sorted(list2))
    return sorted(list1) == sorted(list2) 


if __name__ == "__main__":
    print(is_anagram("rail safety", "fairy tales"))
    print(is_anagram("forty five", "over fifty1"))
    