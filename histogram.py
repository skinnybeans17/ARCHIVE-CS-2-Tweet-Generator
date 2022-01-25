def histogram(file):
    with open(file, 'r') as f:
        text = f.read().split()
        histogram = {}

        for word in text:
            if word in histogram.keys():
                histogram[word] += 1
            else:
                histogram[word] = 1
        return histogram

def unique_words(histogram):
    print("This text contains [" + str(len(histogram)) + "] unique words.")
    return len(histogram)

def frequency(word: str, histogram):
    if type(histogram) == dict:
        return histogram[word]
    else:
        for pair in histogram:
            if pair in histogram:
                if pair[0] == word:
                    return pair[1]

if __name__ == '__main__':
    histogram = histogram('onefish.txt')
    print(histogram)
    print(unique_words(histogram))
    print(frequency('fish', histogram))