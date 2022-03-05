from histogram import histogram_dict, read_file
from dictogram import Dictogram

file = './data/peaky_blinders_s1e1.txt'
word_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()

char_limit = 200

def dictionary_histogram_generator(word_list):
    start_word = word_list[0]
    dict_histogram = {}
    for i in range(len(word_list) - 1):
        current_word = word_list[i]
        next_word = word_list[i + 1]
        if current_word not in dict_histogram:
            histogram = Dictogram()
            histogram.add_count(next_word)
            dict_histogram[word] = histogram
        else:
            dict_histogram[current_word].add_count(next_word)
    return dict_histogram

def tweet_generator(markov_chain_dict):
    tweet_sentence = ''
    start = next(iter(markov_chain_dict))
    tweet_sentence += start

    while len(tweet) < char_limit:
        tweet_list = tweet.split()
        last_word = tweet_list[-1]
        last_word_histogram = markov_chain_dict[last_word]
        next_word = last_word_histogram.sample()
        tweet += ' ' + next_word
    return tweet


if __name__ == '__main__':
    markov_chain = dictionary_histogram_generator(word_list)
    tweet = tweet_generator(markov_chain)
    print(tweet)