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

def get_input_word(parser):
    
    args = parser.parse_args()
    sentence = args.word

    return sentence

def get_letter_data(letter, letter_position):

    sample_size = 2_000
    sample = np.random.uniform(-y_lim, y_lim, (sample_size, 2)).tolist()
    letter_sample = [((x + 2*y_lim*letter_position), y) for (x, y) in sample if assert_funcs[letter]((x, y))]

    return letter_sample

def get_word_data(word):

    word_sample = [get_letter_data(letter, letter_position-(len(word)-1)/2) for letter_position, letter in tqdm(enumerate(word))]
    word_sample = [point for letter_sample in word_sample for point in letter_sample]

    return word_sample

def get_random_sample(y_lim, len_word):

    sample_size = 15_000
    random_sample = np.random.uniform(-y_lim*len_word, y_lim*len_word, (sample_size, 2)).tolist()

    return random_sample

if __name__ == '__main__':

    import argparse
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation 

    parser = argparse.ArgumentParser(description=__doc__.strip().split('\n')[0], add_help=False)
    parser.add_argument('word', type=str)
    word = get_input_word(parser)

    word_sample = get_word_data(word.upper())
    random_sample = get_random_sample(y_lim, len(word))

    fig, axs = plt.subplots(1, 2, figsize=(16, 8))
    axs[0].scatter(*zip(*(word_sample+random_sample)), s=0.1)  
    axs[0].set_xlim(-y_lim, y_lim)
    axs[0].set_ylim(-y_lim, y_lim)
    axs[1].scatter(*zip(*(word_sample+random_sample)), s=0.1)
    plt.show()