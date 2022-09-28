import string
import random
from collections import Counter

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    # LETTER_POOL = ['A','A','A','A','A','A','A','A','A','B','B','C','C','D','D','D','D','E','E','E','E','E','E','E','E''E','E','E','E','F','F','G','G','G','H','H','I','I','I','I','I','I','I','I','I','J','K','L','L','L','L','M','M','N','N','O','O','O','O','O','O','O','O','P','P','Q','R','R','R','R','R','R','S','S','S','S','T','T','T','T','T','T','U','U','U','U','V','V','W','W','X','Y','Y','Z']
    # random_letter = random.choices(LETTER_POOL, k=10)
    
    hand = []
    while len(hand) < 10:
        # random_letter = random.choices(list(LETTER_POOL.keys()), weight = list(LETTER_POOL.values()), k=10)
        random_letter = random.choice(string.ascii_uppercase)
        hand.append(random_letter)
        if hand.count(random_letter) > LETTER_POOL[random_letter]:
            hand.pop()
    return hand

    # hand = []
    # while len(hand) < 10:
    #     random_letter = random.choice(string.ascii_uppercase)
    #     if hand.count(draw_letters) < LETTER_POOL[random_letter]:
    #         hand.append(random_letter)
    #         continue
    #     else:
    #         continue
    # return hand

def uses_available_letters(word, letter_bank):
    word_case = word.upper()
    letter_count_dict = Counter(letter_bank)
    for letter in word_case:
        if letter in letter_count_dict and letter_count_dict[letter] > 0:
            # if word_case.Counter(letter) <= letter_bank.Counter(letter):
            letter_count_dict[letter] -= 1
            continue
        else:
            return False
    return True

    # word_case = word.upper()
    # for letter in word_case:
    #     while letter in letter_bank:
    #         if word.count(letter.casefold()) <= letter_bank.count(letter):
    #             return True
    #         return False
    #     return False

def score_word(word):
    LETTER_SCORE = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 2, 
    'Q': 10, 
    'R': 3, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}
    word_case = word.upper()
    if len(word_case) >= 7:
        score = 8
    else:
        score = 0
    for letter in word_case:
        score += LETTER_SCORE[letter]
    return score

def get_highest_word_score(word_list):
    sorted_word_list = sorted(word_list, key=len)
    score_list = []
    word_score_dict = {}
    for word in sorted_word_list:
        word_score = score_word(word)
        score_list.append(word_score)
        word_score_dict[word] = word_score
    
    highest_word_score = max(set(score_list))
    for word, score in word_score_dict.items():
        if score != highest_word_score:
            word_score_dict.pop(word)
            continue
        elif len(word) == 10:
            winning_tuple = (word, score)
        else:
            winning_tuple = list(word_score_dict.items())[0]
    return winning_tuple
    # highest_word = list(word_score_dict.keys())[list(word_score_dict.values()).index(highest_word_score)]
