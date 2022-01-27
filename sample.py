import random
import sys
from histogram import histogram

file = str(sys.argv[1])

if __name__ == '__main__':
    words = histogram(file).split()
    index = random.randint(0, len(words) - 1)

    print(words[index])