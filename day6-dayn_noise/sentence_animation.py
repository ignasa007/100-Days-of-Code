'''
animation script
'''

from tqdm import tqdm
import numpy as np
from assertions import *

assert_funcs = {
    'A': assert_A,
    'B': assert_B,
    'C': assert_C,
    'D': assert_D
}

def get_input_sentence(parser):
    
    args = parser.parse_args()
    sentence = args.sentence

    return sentence

def get_letter_data(letter, word_position, letter_position):

    sample_size = 1_000 * 10**word_position
    sample = np.random.uniform(-y_lim, y_lim, (sample_size, 2)).tolist()
    letter_sample = [((x + 2*y_lim*letter_position), y) for (x, y) in sample if assert_funcs[letter]((x, y))]

    return letter_sample

def get_word_data(word, word_position):

    word_sample = [get_letter_data(letter, word_position, letter_position-(len(word)-1)/2) for letter_position, letter in tqdm(enumerate(word))]
    word_sample = [(x * 10**word_position, y * 10**word_position) for letter_sample in word_sample for x, y in letter_sample]

    return word_sample

def get_sentence_data(sentence):

    sentence_sample = [get_word_data(word, word_position) for word_position, word in enumerate(sentence.split())]

    return sentence_sample

if __name__ == '__main__':

    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser(description=__doc__.strip().split('\n')[0], add_help=False)
    parser.add_argument('sentence', type=str)
    sentence = get_input_sentence(parser)

    sentence_sample = get_sentence_data(sentence.upper())
    word_sample = sentence_sample[0]

    for word_sample in sentence_sample:
        plt.scatter(*zip(*word_sample), s=0.1)
        
    plt.show()