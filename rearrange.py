import random
import sys

words_list = sys.argv[1:]

def rearrange_words():
    random.shuffle(words_list)
    return words_list

if __name__ == '__main__':
    rearranged_words = rearrange_words()
    print(' '.join(rearranged_words))