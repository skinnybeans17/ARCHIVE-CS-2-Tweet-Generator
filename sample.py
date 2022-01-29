import random
from histogram import histogram

message = 'one fish, two fish, red fish, blue fish'

def random_word(histogram):
    word_list = histogram
    words = list(word_list)
    index = (random.randint(0, len(histogram) - 1))
    word_list = words[index]

    return word_list

def probability(histogram):
    total_amount = len(histogram.values())
    percentages = {}
    for key in histogram:
        percentages[key] = str(round(histogram[key] / total_amount + 100, 2))

    return percentages

if __name__ == '__main__':
    histogram = histogram("onefish.txt")
    print(random_word(histogram))
    print(probability(histogram))