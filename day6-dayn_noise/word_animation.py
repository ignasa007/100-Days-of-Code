'''
animation script
'''

from tqdm import tqdm
import numpy as np
from assertions import assert_funcs

def get_input_word(parser):
    
    args = parser.parse_args()
    sentence = args.word

    return sentence

def get_letter_data(letter, letter_position):

    sample_size = 4_000
    sample = np.random.uniform(-y_lim, y_lim, (sample_size, 2)).tolist()
    letter_sample = [((x + 2*y_lim*letter_position), y) for (x, y) in sample if assert_funcs[letter]((x, y))]

    return letter_sample

def get_word_data(word):

    word_sample = [get_letter_data(letter, letter_position-(len(word)-1)/2) for letter_position, letter in tqdm(enumerate(word))]
    word_sample = [point for letter_sample in word_sample for point in letter_sample]

    return word_sample

def get_random_sample(x_lim, y_lim):

    sample_size = 16_000
    x_s = np.random.uniform(-x_lim, x_lim, sample_size).reshape(-1, 1)
    y_s = np.random.uniform(-y_lim, y_lim, sample_size).reshape(-1, 1)
    random_sample = np.hstack((x_s, y_s)).tolist()

    return random_sample

if __name__ == '__main__':

    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser(description=__doc__.strip().split('\n')[0], add_help=False)
    parser.add_argument('word', type=str)
    word = get_input_word(parser)

    word_sample = get_word_data(word.upper())
    random_x_lim, random_y_lim = y_lim*len(word)*1.5, y_lim*1.5
    random_sample = get_random_sample(random_x_lim, random_y_lim)

    animation_size, num_times = 20, 3
    x_lims, y_lims = np.linspace(2, random_x_lim, animation_size).tolist(), np.linspace(1, random_y_lim, animation_size).tolist()
    x_lims, y_lims = x_lims + x_lims[::-1], y_lims + y_lims[::-1]

    plt.scatter(*zip(*(word_sample+random_sample)), s=0.2)
    for x_lim, y_lim in zip(x_lims*num_times, y_lims*num_times):
        plt.xlim(-x_lim, x_lim)
        plt.ylim(-y_lim, y_lim)
        plt.pause(0.01)
    plt.show()