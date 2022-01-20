import random
import sys

amount_of_words = int(sys.argv[1:][0])

f = open('words.txt', 'r')
words = f.read()
words_list = words.split(" ")

def randomize_words():
    random.shuffle(words_list)
    return words_list

if __name__ == '__main__':
    randomized_words = randomize_words()
    print(' '.join(randomized_words[0:amount_of_words]))