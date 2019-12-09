from dictogram import Dictogram
import random
from string import punctuation


def cleanup_text_file(file_name):

    with open(file_name, 'r') as f:
        text = f.read().split()

    words_list = []
    for word in text:
        word = word.strip(".@'/").lower()
        words_list.append(word)

    return words_list


class MarkovChain(dict):

    def __init__(self, words_list = None):

        super(MarkovChain, self).__init__()


        if words_list is not None:
            self.create_markov_chain(words_list)
            self['start'] = Dictogram(['the'])
            self['end'] = Dictogram(['.'])

    def create_markov_chain(self, words_list):

        for index in range(len(words_list) - 2):

            first_word = words_list[index]
            middle_word = words_list[index + 1]
            last_word = words_list[index + 2]

            if (first_word, middle_word) not in self:
                dict = Dictogram([(middle_word, last_word)])
                self[(first_word, middle_word)] = dict

            else:
                self[(first_word, middle_word)].add_count((middle_word, last_word))

        # return self.dict_histogram

    def sentence_gen(self, length=10):

        sampled_word = random.choice(list(self.get('start')))

        sentence = sampled_word

        for item in range(length - 1):
            sampled_word = self[sampled_word].sample()

            sentence += " " + sampled_word


        sentence += random.choice(list(self.get('end')))

        return sentence


if __name__ == "__main__":
    words_list = cleanup_text_file('sample_book.txt')
    markov_chain = MarkovChain(words_list)

    print(markov_chain)
    print(markov_chain.sentence_gen())
