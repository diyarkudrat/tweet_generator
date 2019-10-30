import random
import sys
from histogram import read_file, histogram_dict

def get_count(histogram):
    count = 0
    for key, value in histogram.items():
        count += value
    return count



def prob_word(histogram, count):

    total = 0
    index = random.randint(1, count)

    for key, value in histogram.items():
        total += value

        if index <= total:
            return key


    # print('!!!')



def main_sample(text_file):
    # print('!!!')
    histogram = histogram_dict(text_file)
    count = get_count(histogram)
    # print('!!!')

    word = prob_word(histogram, count)
    print(word)

    # print(count)
if __name__ == '__main__':
    args = sys.argv[1]

    text_file = args

    # text_file = '\Term_2\cs_1.2\tweet_generator\src\fish.txt'
    # text_file = 'fish.txt'

    # histogram = histogram_dict(text_file)
    # count(histogram)

    # print(type(text_file))
    main_sample(text_file)

    # print(count)
