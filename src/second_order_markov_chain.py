from dictogram import Dictogram
import random




def cleanup_text_file(file_name):

    with open(file_name, 'r') as f:
        text = f.read().split()

    words_list = []
    for word in text:
        word = word.strip(".@'?/+[]()""br<>").lower()
        words_list.append(word)

    return words_list


class MarkovChain(dict):

    def __init__(self, words_list = None):

        super(MarkovChain, self).__init__()


        if words_list is not None:
            self.create_markov_chain(words_list)
            self['start'] = Dictogram(['The'])
            self['end'] = Dictogram(['.'])

        self.sentence = None

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

    def get_tuples(self, word):
        tuples = []

        for tuple in list(self):
            if word in tuple[0]:
                tuples.append(tuple)

        return tuples

    def sentence_gen(self, length):

        start_word=random.choice(list(self.get('start')))
        end_word=random.choice(list(self.get('end')))

        sampled_word = random.choice(random.choice(list(self)))

        sentence = start_word + ' ' + sampled_word

        while length > 0:
            # get all tuples with sampled_word
            tuples = self.get_tuples(sampled_word)
            # choose a random tuple
            new_tuple = random.choice(tuples)
            # add second word to sentence
            sentence = sentence + ' ' + new_tuple[1]
            # random word = new sampled_word
            sampled_word = new_tuple[1]
            # subtract 1 from length
            length -= 1

        self.sentence =  sentence
        self.sentence += end_word
        return self.sentence



if __name__ == "__main__":
    words_list = cleanup_text_file('chance_lyrics.txt')
    markov_chain = MarkovChain(words_list)

    # print(markov_chain)
    print(markov_chain.sentence_gen(10))
