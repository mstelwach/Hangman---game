import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = infile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;False otherwise
    """
    if all(i in letters_guessed for i in secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    """
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    """
    guess = ''
    for char in secret_word:
        if char in letters_guessed:
            guess += char
        else:
            guess += '_ '
    return guess


def get_available_letters(letters_guessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not yet been guessed.
    """
    available_letter = string.ascii_lowercase
    for char in available_letter:
        if char in letters_guessed:
            available_letter = available_letter.replace(char, '')
    return available_letter


def hangman(secret_word):
    """
    secretWord: string, the secret word to guess.
    """
    letters_guessed = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secret_word)))
    guesses = 8
    hangman_pic = (
        """
        -----
        |   |
        |
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |  -+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | 
        |  | 
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | | 
        |  | 
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | | 
        |  | | 
        |
        --------
        """)
    print(hangman_pic[0])
    while guesses >= 0:
        print('-----------')
        print('You have {} guesses left.'.format(guesses))
        print('Available letters: {}'.format(get_available_letters(letters_guessed)))
        user_letter = input('Please guess a letter: ').lower()

        if user_letter in letters_guessed:
            print('\033[1m{:10s}\033[0m'.format("Oops! You've already guessed that letter: {}".format(get_guessed_word(secret_word, letters_guessed))))
        else:
            letters_guessed.append(user_letter)
            if user_letter in secret_word:
                print('\033[1m{:10s}\033[0m'.format('Good guess: {}'.format(get_guessed_word(secret_word,
                                                                                             letters_guessed))))
            else:
                guesses -= 1
                if len(secret_word) > 1:
                    print(hangman_pic[(len(hangman_pic) -1) - guesses])
                    print('\033[1m{:10s}\033[0m'.format("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed))))
                else:
                    print(hangman_pic[(len(hangman_pic) -1) - guesses])
                    print('\033[1m{:10s}\033[0m'.format("Oops! You've already guessed that letter: {}".format(get_guessed_word(secret_word, letters_guessed))))

        if is_word_guessed(secret_word, letters_guessed):
            print('------------')
            return '\033[1m{:10s}\033[0m'.format('Congratulations, you won!')
        elif guesses == 0:
            print('------------')
            return '\033[1m{:10s}\033[0m'.format('Sorry, you ran out of guesses. The word was {}.'.format(secret_word))



wordlist = load_words()
secretWord = choose_word(wordlist).lower()
print(hangman(secretWord))


