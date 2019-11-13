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

def sentence(count, total, histogram):
    sentence = ""

    while count > 0:
        index = random.randint(0, total - 1)
        total_count = 0

        for key, value in histogram.items():
            if index <= total_count:
                sentence += f' {key}'
                break

            total_count += value

        count -= 1

    return sentence


def main_sample(text_file):
    '''Calling the function that returns the random word '''

    histogram = histogram_dict(text_file)
    count = get_count(histogram)

    word = prob_word(histogram, count)
    display_word = print(word)
    return display_word

if __name__ == '__main__':

    text_file = read_file('fish.txt')
    main_sample(text_file)
