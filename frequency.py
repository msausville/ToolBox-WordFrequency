"""
    Analyzes the word frequencies in a book downloaded from Project Gutenberg
"""

from collections import Counter
# from bs4 import BeautifulSoup
import requests
import string

# print('first test')
# print(string.punctuation)

# html = BeautifulSoup(requests.get('http://www.gutenberg.org/files/2591/2591-0.txt').text, 'lxml')


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    master_word_list = []

    for line in lines:
        # print(type(line))
        line = line.lower()
        if line == '\n':
            continue
        cut_up_line = line.strip('\n')
        word_list = cut_up_line.split(' ')
        master_word_list.extend(word_list)
    return master_word_list
        # print(line)
    # print(master_word_list)


    # for i in range(0, len(lines)):
    #     line = lines[i]
    #     word_list.extend line


# print(listgrimms)


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    word_dictionary = {}
    for word in word_list:
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1

    word_count_obj_list = []
    for word, count in word_dictionary.items():
        word_count_obj_list.append(WordCountObj(word, count))

    word_count_obj_list.sort(key=lambda wcobj: wcobj.count, reverse=True)

    final_list =[]
    i = 0
    while i < n:
        final_list.append(word_count_obj_list[i].word)
        i += 1
    return final_list


class WordCountObj:
    def __init__(self, word, count):
        self.word = word  # string
        self.count = count  # int

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    # print(string.punctuation)
    top_words = get_top_n_words(get_word_list('pg32325.txt'), 60)
    print(top_words)

