# Hangman game
#

# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(str(len(wordlist)) + " words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if not letter in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter + ' '
        else:
            result += '_ '
    return result

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abclist = []
    for letter in abc:
        abclist += letter

    for letter in lettersGuessed:
        abclist.remove(letter)
        
    return ''.join(abclist)    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    - At the start of the game, let the user know how many 
      letters the secretWord contains.

    - Ask the user to supply one guess (i.e. letter) per round.

    - The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    - After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

    count = 8
    lettersGuessed = []
    
    while count > 0:
        print("-------------")
        
        # WIN: user guess fulfilled, win
        if not '_' in getGuessedWord(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
            
        print("You have " + str(count) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        
        # Ensure the user provides one letter
        while True:                           
            guess = input("Please guess a letter: ")
            if guess not in string.ascii_lowercase:
                print("please provide a legitimate letter.", end='')
            else:
                break

        
        # case 1: you already guessed it
        if isWordGuessed(guess, lettersGuessed):
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        # case 2: not guessed + correct guess (in secretWord)
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        # LOSE: user guess failed, lose
        elif count == 1 and guess not in secretWord:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            break        
        # case 3: not guessed + incorrect guess (not in secretWord)
        else:
            lettersGuessed.append(guess)
            count -= 1
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))

                    


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
