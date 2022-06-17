'Boundary definitions for letters'

from math import pi, tan

y_lim, width = 5, 1
left_end, right_end = -4, 4

def get_xy(point):

    x, y = point
    assert isinstance(x, float) and isinstance(y, float)

    return x, y

def assert_A(point, slope=10/3):

    x, y = get_xy(point)

    inside_outer_left_arm    = lambda x, y: y + y_lim < slope  * (x - left_end) 
    inside_outer_right_arm   = lambda x, y: y + y_lim < -slope * (x - right_end) 
    outside_inner_left_arm   = lambda x, y: y + y_lim > slope  * (x - (left_end+width)) 
    outside_inner_right_arm  = lambda x, y: y + y_lim > -slope * (x - (right_end-width)) 

    return (-width <= y <= 0 or y_lim-width <= y <= y_lim)  and (inside_outer_left_arm(x, y) and inside_outer_right_arm(x, y)) \
        or (-y_lim <= y <= -width or 0 <= y <= y_lim-width) and (inside_outer_left_arm(x, y) and outside_inner_left_arm(x, y) or inside_outer_right_arm(x, y) and outside_inner_right_arm(x, y))

def assert_B(point):

    x, y = get_xy(point)

    return assert_D((x, 2*y - (y_lim - width/2))) \
        or assert_D((x, 2*y + (y_lim - width/2))) 

def assert_C(point, center=1, theta=pi/3):

    x, y = get_xy(point)

    return  (x-center)**2 + y**2 <= y_lim**2 \
        and (x-center)**2 + y**2 >= (y_lim-1)**2 \
        and (x < 0 or abs(y/(x-center)) > tan(theta))

def assert_D(point):

    x, y = get_xy(point)

    curve_left_end = left_end + width
    outer_major_axis = right_end - curve_left_end
    outer_minor_axis = y_lim
    inner_major_axis = outer_major_axis - width 
    inner_minor_axis = outer_minor_axis - width

    inside_outer_curve  = lambda x, y: outer_minor_axis**2 * (x-curve_left_end)**2 + outer_major_axis**2 * y**2 <= outer_minor_axis**2 * outer_major_axis**2 
    outside_inner_curve = lambda x, y: inner_minor_axis**2 * (x-curve_left_end)**2 + inner_major_axis**2 * y**2 >= inner_minor_axis**2 * inner_major_axis**2

    return (-outer_minor_axis <= y <= outer_major_axis) and (left_end <= x <= left_end+width or \
        left_end+width <= x <= right_end and inside_outer_curve(x, y) and outside_inner_curve(x, y))

if __name__ == '__main__':

    import argparse
    import sys
    import numpy as np
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser(description=__doc__.strip().split('\n')[0], add_help=False)
    parser.add_argument('letter', type=str)
    args = parser.parse_args()

    letter = args.letter.upper()
    if letter == 'A':
        assert_func = assert_A
    elif letter == 'B':
        assert_func = assert_B
    elif letter == 'C':
        assert_func = assert_C
    elif letter == 'D':
        assert_func = assert_D
    else:
        print(f'enter a valid letter, received {letter}.')
        sys.exit()

    sample_size = 10_000
    sample = np.random.uniform(-10, 10, (sample_size, 2)).tolist()
    sample = [point for point in sample if assert_func(point)]

    plt.scatter(*zip(*sample))
    plt.xlim(-y_lim, y_lim)
    plt.ylim(-y_lim, y_lim)
    plt.show()