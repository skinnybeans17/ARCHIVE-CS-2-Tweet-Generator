import random
import sys

words_list = sys.argv[1:]

def rearrange_words(words_list):
    split_words = words_list.split(' ')
    print(split_words)
    random.shuffle(split_words)
    print(split_words)

if __name__ == '__main__':
    words_list = input("Enter words here: ")
    rearrange_words(words_list)