import math
help(print)
help(math.ceil)
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
print(len(SCRABBLE_LETTER_VALUES))
print(type(SCRABBLE_LETTER_VALUES.keys()))
word = "*aBC"
print(word.lower())
word_test = "red"
print(list(word_test))
list = ['r','e','d']
print(type(str(list)))
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
print(VOWELS + CONSONANTS)