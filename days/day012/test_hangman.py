from unittest.mock import patch
import random
import pytest
from hangman import loadWords, chooseWord, isWordGuessed, getGuessedWord, getAvailableLetters, hangman

TEST_WORDLIST_FILENAME = "test_words.txt"
TEST_SECRET_WORD = "python"


def test_loadWords():
    test_wordlist = loadWords(TEST_WORDLIST_FILENAME)
    assert len(test_wordlist) == 42
    assert test_wordlist[0] == 'Python'


@patch.object(random, "choice")
def test_chooseWord(x, wordlist=TEST_WORDLIST_FILENAME):
    x.return_value = "python"
    assert chooseWord(wordlist) == "python"


def test_isWordGuessed():
    assert isWordGuessed(['p','y','t','h','o','n'], 'python') == True


def test_getGuessedWord():
    assert getGuessedWord('python', []) == '......'
    assert getGuessedWord('python', ['b','a','s','i','c']) == '......'
    assert getGuessedWord('python', ['p','t','n']) == 'p.t..n'
    assert getGuessedWord('python', ['p','y','t','h','o','n']) =='python'


@pytest.mark.parametrize('arg, ret', [
    (['p'],'abcdefghijklmnoqrstuvwxyz'),
    (['p','y'],'abcdefghijklmnoqrstuvwxz'),
    (['p','y','t'],'abcdefghijklmnoqrsuvwxz'),
    (['p','y','t','h'],'abcdefgijklmnoqrsuvwxz'),
    (['p','y','t','h','o'],'abcdefgijklmnqrsuvwxz'),
    (['p','y','t','h','o','n'],'abcdefgijklmqrsuvwxz')
])
def test_getAvailableLetters(arg, ret):
    assert getAvailableLetters(arg) == ret


@patch("builtins.input", side_effect=['p','Y','P','g','O', 'A', 'a', 'h','p','t','n'])
def test_hangman_win(inp, capfd):
    hangman(TEST_SECRET_WORD)
    out = capfd.readouterr()[0]
    #print(out)
    output = [line.strip() for line in out.split('\n') if line.strip()]
    assert output[-1] == 'Congratulations, you won!'


@patch("builtins.input", side_effect=['a','B','c','D', 'E', 'f', 'g', 'H', 'i'])
def test_hangman_lose(inp, capfd):
    hangman(TEST_SECRET_WORD)
    out = capfd.readouterr()[0]
    #print(out)
    output = [line.strip() for line in out.split('\n') if line.strip()]
    assert output[-1] == 'Sorry, you ran out of guesses. The word was "{}"'.format(TEST_SECRET_WORD)
