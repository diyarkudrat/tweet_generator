def read_file(text_file):
    with open('blog_post.txt', 'r') as file:
        words = f.read().split()

    return words

def histogram(text_file):
    text = read_file(text_file)
    histogram = []

    for word in text:
        for list in histogram:
            if word == list[0]:
                list[1] += 1

            else:
                histogram.append([word, 1])

    return histogram

def unique_words(histogram):
    count = 0
    for list in histogram:
        count += 1

    return count

def frequency(word, histogram):
    for list in histogram:
        if list[0] == word:
            return list[1]


# if __name__ == '__main__':
#     histogram = histogram('blog_post.txt')
#     frequency = frequency('it', histogram)
#     unique_words = unique_words(histogram)
#
#     print(histogram)
#     print(f'Amount of times {})
