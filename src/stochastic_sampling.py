import random
import sys
from histogram import read_file, histogram_dict


def prob_word(histogram):
    #total = 0

    count = 0
    for key, value in histogram.iteritems():
        count += value
    return count

    total = 0
    index = random.randint(1, count)

    for key, value in histogram.iteritems():
        total += value

        if index <= total:
            return key

def get_random_words(histogram):

    keys = list(histogram.keys())
    words_list = []

    for word in keys:
        words_list.append(word)

    return words_list
    # print(words_list)

def main_sample(text_file):
    words_list = read_file(text_file)
    histogram = histogram_dict(words_list)

    prob_word = prob_word(histogram)
    print(prob_word)

if __name__ == '__main__':
    text_file = sys.argv[1:]
    main_sample(text_file)
