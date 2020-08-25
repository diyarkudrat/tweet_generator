import sys

def cleanup(file_name):
    """ Reads in file and cleans it up """

    with open(file_name, 'r') as f:
        lines = f.readlines()
    word_list = []
    for i, line in enumerate(lines):
        line = line.lstrip().rstrip()

        if len(line.split(' ')) => 4:
            for word in line.split():
                word_list.append(word)


    return word_list