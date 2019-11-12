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


def markov_chain(words_list):

    markov_dict = dict()

    for index, word in enumerate(words_list):

        if markov_dict.get(word) == None:
            markov_dict[word] = Dictogram()

        if index < len(words_list) - 1:
            next = words_list[index]
            markov_dict.get(word).add_count(next)

    return markov_dict



if __name__ == "__main__":

    words_list = cleanup_text_file('histo_sample_song.txt')

    print(markov_chain(words_list))
