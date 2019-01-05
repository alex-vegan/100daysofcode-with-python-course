import random

WORDLIST_FILENAME = "words.txt"


def loadWords(file=WORDLIST_FILENAME):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(file, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i in lettersGuessed:
            continue
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    for i in secretWord:
        if i in lettersGuessed:
            guessedWord += i
        else:
            guessedWord += '.'
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if not i in lettersGuessed:
            availableLetters += i
    return availableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game user knows how many letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user receive feedback immediately after each guess about whether their
      guess appears in the computers word.

    * After each round display to the user the partially guessed word so far,
      as well as letters that the user has not yet guessed.
    '''
    lettersGuessed = []
    print('Welcome to the game, Hangman!\n'
          'I am thinking of a word that is', len(secretWord),'letters long\n',
           getGuessedWord(secretWord, lettersGuessed), end='\n')
    mistakesMade = 0
    while not isWordGuessed(secretWord, lettersGuessed) and mistakesMade < 8:
        letter = (input('-'*50 + '\n'
                        'You have ' + str(8-mistakesMade) + ' guesses left.\n'
                        'Available letters: ' + getAvailableLetters(lettersGuessed) + '\n'
                        'Please guess a letter: ')).lower()
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter\n",
                   getGuessedWord(secretWord, lettersGuessed),end='\n')
        else:
            lettersGuessed.append(letter)
            lettersGuessed = list(set(lettersGuessed))
            if letter in secretWord:
                print('Good guess:\n',
                       getGuessedWord(secretWord, lettersGuessed),end='\n')
            else:
                mistakesMade += 1
                print('Oops! That letter is not in my word\n',
                       getGuessedWord(secretWord, lettersGuessed),end='\n')
    print('-'*50)
    if mistakesMade == 8:
        print('Sorry, you ran out of guesses. The word was "' + secretWord + '"')
    else:
        print('Congratulations, you won!')


if __name__ == '__main__':
    wordlist = loadWords(WORDLIST_FILENAME)
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
