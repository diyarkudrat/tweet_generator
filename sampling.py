import random
import sys
from histogram import read_file, histogram_dict

def get_count(histogram):
    ''' Add up all values in histogram'''
    count = 0
    for key, value in histogram.items():
        count += value
    return count



def prob_word(histogram, count):
    '''For each key-value pair, if random index chosen is less than or equal to the total value,
       return the word'''

    total = 0
    index = random.randint(1, count)

    for key, value in histogram.items():
        total += value

        if index <= total:
            return key


    # print('!!!')



def main_sample(text_file):
    '''Calling the function that returns the random word '''

    # print('!!!')
    histogram = histogram_dict(text_file)
    count = get_count(histogram)
    # print('!!!')

    word = prob_word(histogram, count)
    display_word = print(word)
    return display_word

    # print(count)
if __name__ == '__main__':
    # args = sys.argv[1]
    #
    # text_file = args

    # text_file = '\Term_2\cs_1.2\tweet_generator\src\fish.txt'
    # text_file = 'fish.txt'

    # histogram = histogram_dict(text_file)
    # count(histogram)

    # print(type(text_file))
    text_file = 'fish.txt'
    main_sample(text_file)

    # print(count)
