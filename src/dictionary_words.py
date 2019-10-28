import random, sys

# example with own small text file I created
# def get_words(arg):
#     with open('words.txt') as file:
#         # print(list(file))
#
#         words = file.read().split()
#
#         random_words = []
#         for i in range(int(arg)):
#             random_words.append(random.choice(words))
#
#         return ' '.join(random_words) + '.'

word_file = '/usr/share/dict/words'

def get_words(arg):
    with open(word_file, 'r') as file:

        words = file.read().split()

        random_words = []
        for i in range(int(arg)):
            random_words.append(random.choice(words))

        # random_words = [random.choice(words) for i in range(int(arg))]

        return ' '.join(random_words) + '.'



if __name__ == '__main__':
    num = sys.argv[1:]
    sentence = get_words(num[0])
    print(sentence)
