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
                break

        if updated == False:
            histogram.append([word, 1])

    return histogram

def histogram_dict(words_list):
    '''Returns dictionary'''

    histogram = dict()

    for word in words_list:
        if word in histogram:
            histogram[word] += 1

        else:
            histogram[word] = 1

    return histogram

def histogram_tuple(text_file):
    '''Returns tuple'''
    text = read_file(text_file)
    amount = 0
    histogram = []

    for word in text:
        updated = False
        for tuple in histogram:
            if tuple[0] == word:
                amount = tuple[1] + 1
                histogram.remove(tuple)
                histogram.append((word, amount))
                updated = True
        if updated == False:
            histogram.append((word, 1))

    return histogram

    # for each tuple in histogram, check if tuple[0] is in tuple. If it is, Add one to ammount.
     # Then remove that tuple from histogram, add new tuple with amount.
     # return Histogram at end



def unique_words(histogram):
    '''Returns total count of unique words based off of histogram data for list of lists.'''
    # return len()
    count = 0
    for list in histogram:
        count += 1

    return count

def frequency(word, histogram):
    '''Returns how many times a specific word is in a histogram data set for list of lists'''

    for list in histogram:
        if list[0] == word:
            return list[1]



if __name__ == '__main__':
    # histogram = histogram('txt_files/histo_sample_song.txt')
    # word = 'already'
    # frequency = frequency(word, histogram)
    # unique_words = unique_words(histogram_dict)
    # histogram = histogram(text)
    words_list = read_file('fish.txt')
    histogram = histogram_dict(words_list)

    print(histogram)
    # print(f'Amount of times {word} appeared in text: {frequency}')
    # print(f'Unique Words: {unique_words}')
