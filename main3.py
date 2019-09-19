import math
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
    'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list


def get_frequency_dict(sequence):
    # freq: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):
    character_values_score = 0
    for i in word.lower():
        if i in SCRABBLE_LETTER_VALUES:
            character_values_score += SCRABBLE_LETTER_VALUES[i]

    word_len = len(word)
    word_len_score = (7 * word_len - 3 * (n - word_len))
    if word_len_score <= 0:
        word_len_score = 1

    score = character_values_score * word_len_score
    return score


def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter)
    print()


def deal_hand(n):
    hand = {}
    num_vowels = int(math.ceil(n / 3))

    hand['*'] = 1
    num_vowels -= 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


print(deal_hand(HAND_SIZE))


def update_hand(hand, word):
    hand_copy = hand.copy()

    def count_down_or_remove(copy):
        copy[i] = copy.get(i, 0) - 1
        if copy.get(i, 0) <= 0:
            copy.pop(i)

    for i in word.lower():
        if i in hand_copy:
            count_down_or_remove(hand_copy)
        else:
            count_down_or_remove(hand_copy)
    return hand_copy


def is_valid_word(word, hand, word_list):
    valid_wildcard_list = []
    hand_copy = hand.copy()

    def check_word_to_hand(word_to_validate):
        word_to_validate = word_to_validate.lower()
        passed = True
        for char in word_to_validate:
            if char in hand_copy.keys():
                hand_copy[char] -= 1
                if hand_copy[char] < 0:
                    passed = False
            else:
                passed = False

        if passed is True:
            return True
        else:
            return False

    def wildcard_validity_check(word_to_check):
        word_to_check = word_to_check.lower()
        passed = True
        for vowel in VOWELS:
            is_valid_wildcard = word_to_check.replace('*', vowel)

            if is_valid_wildcard in word_list:
                valid_wildcard_list.append(is_valid_wildcard)

        if len(valid_wildcard_list) == 0:
            passed = False

        if passed is True:
            return True
        else:
            return False

    if '*' in word:
        is_valid = wildcard_validity_check(word)
        if is_valid is True and check_word_to_hand(word) is True:
            return True
    else:
        if check_word_to_hand(word) is True:
            return True
