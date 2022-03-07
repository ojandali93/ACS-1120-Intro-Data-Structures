from dictogram import Dictogram
import random
from random import choice
from tokens import tokens
import sys


def markov_dict(dictionary):
    word_list = source.split()
    markov_dict = {}
    words_range = range(len(word_list) - 2)

    for word_index in words_range:
        first_word = word_list[word_index]
        second_word = word_list[word_index + 1]
        third_word = word_list[word_index + 2]

        curr_tuple = (first_word, second_word)

        if curr_tuple in markov_dict:
            markov_dict[curr_tuple].add_count(third_word)
        else:
            markov_dict[curr_tuple] = Dictogram([third_word])
    return markov_dict

def next_words(histogram):
    count = 0
    dart = random.random()
    for key,value in histogram.items(): 
        count += value
        if count >= dart: 
            return key

def markov_chain(dictionary):
    dict_keys = [key for key, value in dictionary.items()]
    word_list = list(dict_keys[random.randint(0, len(dict_keys) - 1)])

    for word_index in range(10):
        tuple_key = tuple((word_list[index]) for index in range(word_index, word_index + 2))
        if tuple_key in dictionary:
            word_dictogram = dictionary[tuple_key]
            next_word = next_words(word_dictogram)
            word_list.append(next_word)
        else:
            break
    return " ".join(word_list)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        print(markov_chain(markov_dict(source)))
    else:
        print('No source text filename given as argument')