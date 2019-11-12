from dictogram import Dictogram
import random


def cleanup_text_file(file_name):

    with open(file_name, 'r') as f:
        text = f.read().split()

    words_list = []
    for word in text:
        word = word.strip(".@'/").lower()
        words_list.append(word)

    return words_list


def create_markov_chain(words_list):

    markov_dict = dict()

    for index, word in enumerate(words_list):

        if markov_dict.get(word) == None:
            markov_dict[word] = Dictogram()

        if index + 1 < len(words_list):
            next = words_list[index + 1]
            markov_dict.get(word).add_count(next)

    return markov_dict

def sentence_gen(markov_chain, length):

    sampled_word = random.choice(list(markov_chain))

    sentence = sampled_word

    for item in range(length - 1):
        sampled_word = markov_chain[sampled_word].sample()

        sentence += ' ' + sampled_word

    return sentence



if __name__ == "__main__":

    words_list = cleanup_text_file('histo_sample_song.txt')
    markov_chain = create_markov_chain(words_list)

    print(sentence_gen(markov_chain, 10))

    # print(markov_chain(words_list))
