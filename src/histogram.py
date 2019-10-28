def read_file(text_file):
    with open(text_file, 'r') as f:
        words = f.read().split()

    return words

# text = [1, 2, 1, 4, 5, 2]
def histogram(text_file):
    ''' Returns a list of lists '''

    text = read_file(text_file)
    histogram = []

    for word in text:
        updated = False
        for list in histogram:
            if word == list[0]:
                list[1] += 1
                updated = True

        if updated == False:
            histogram.append([word, 1])

    return histogram

def unique_words(histogram):
    '''Returns total count of unique words based off of histogram data'''

    count = 0
    for list in histogram:
        count += 1

    return count

def frequency(word, histogram):
    '''Returns how many times a specific word is in a histogram data set'''

    for list in histogram:
        if list[0] == word:
            return list[1]


if __name__ == '__main__':
    histogram = histogram('txt_files/histo_sample_song.txt')
    word = 'it'
    frequency = frequency(word, histogram)
    unique_words = unique_words(histogram)
    # histogram = histogram(text)

    print(histogram)
    print(f'Amount of times {word} appeared in text: {frequency}')
    print(f'Unique Words: {unique_words}')
