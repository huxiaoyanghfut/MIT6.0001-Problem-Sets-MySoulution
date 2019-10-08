# Problem Set 2, hangman.py
# Name: timeshell
# Collaborators:
# Time spent: 10 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = True
    for letter in secret_word:
        if letter not in letters_guessed:
            flag = False
    return flag


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word = guessed_word + "_ "
        else:
            guessed_word = guessed_word + letter
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #letters_all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters_all = "abcdefghijklmnopqrstuvwxyz"
    available_letters = ""
    for letter in letters_all:
        if letter not in letters_guessed:
            available_letters = available_letters + letter
    return available_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the gmae Hangman!")
    print("I am thinking of a word that is ",
          len(secret_word), "letters long.")
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("You have ", warnings, " warnings left.")
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print("--------------------------")
        print("You have ", guesses, " guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        input_user = input("Please guess a letter:")
        if not str.isalpha(input_user) or len(input_user) > 1:
            warnings -= 1
            if warnings > 0:
                print("Oops! That is not avalid letter.You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left\n" +
                      "so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
            continue
        elif input_user in letters_guessed:
            warnings -= 1
            if warnings > 0:
                print("Oops! You've already guessed that letter. You have no warnings left\n" +
                      "so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left \
                so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
            continue
        letters_guessed.append(input_user)
        if input_user not in secret_word:

            print("Oops! The letter is not in my word:",
                  get_guessed_word(secret_word, letters_guessed)
                  )
        else:
            print("Good guess:", get_guessed_word(
                secret_word, letters_guessed))
        guesses -= 1
    if is_word_guessed(secret_word, letters_guessed):
        print("--------------------------")
        print("Congratulations,you won!")
        print("Your Total score for this game is:", 6 - guesses)
    else:
        print("--------------------------")
        print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = True
    my_word = my_word.replace(" ", "")
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if not (my_word[i] == other_word[i] or my_word[i] == '_'):
                flag = False
    else:
        flag = False
    return flag


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = 0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            flag += 1
            print(word)
    if flag == 0:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the gmae Hangman!")
    print("I am thinking of a word that is ",
          len(secret_word), "letters long.")
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("You have ", warnings, " warnings left.")
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print("--------------------------")
        print("You have ", guesses, " guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        input_user = input("Please guess a letter:")
        if input_user == '*':
            my_word = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(my_word)
        elif not str.isalpha(input_user) or len(input_user) > 1:
            warnings -= 1
            if warnings > 0:
                print("Oops! That is not avalid letter.You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That is not avalid letter.You have no warnings left\n" +
                      "so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
            continue
        elif input_user in letters_guessed:
            warnings -= 1
            if warnings > 0:
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left \
                so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
            continue
        letters_guessed.append(input_user)

        if input_user not in secret_word:
            print("Oops! The letter is not in my word:",
                  get_guessed_word(secret_word, letters_guessed)
                  )
        else:
            print("Good guess:", get_guessed_word(
                secret_word, letters_guessed))
        guesses -= 1
    if is_word_guessed(secret_word, letters_guessed):
        print("--------------------------")
        print("Congratulations,you won!")
        print("Your Total score for this game is:", 6 - guesses)
    else:
        print("--------------------------")
        print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    """
    secret_word = choose_word(wordlist)
    while len(secret_word) >5:
        secret_word = choose_word(wordlist)

    #secret_word ="tact"
    hangman(secret_word)

    print(match_with_gaps("te_ t","tact"))
    print(match_with_gaps("a_ _ le","banana"))
    print(match_with_gaps("a_ _ le","apple"))
    print(match_with_gaps("a_ le","apple"))
    show_possible_matches("t_ _ t")
    """

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.
    #
    secret_word = choose_word(wordlist)
    while len(secret_word) > 5:
        secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
