'Boundary definitions for letters'

from math import pi, tan

y_lim, width = 5, 1
left_end, right_end = -3.5, 3.5

def get_xy(point):

    x, y = point
    assert isinstance(x, float) and isinstance(y, float)

    return x, y

def assert_A(point, slope=10/3):

    x, y = get_xy(point)

    inside_outer_left_arm    = lambda x, y: y + y_lim <= slope  * (x - left_end) 
    inside_outer_right_arm   = lambda x, y: y + y_lim <= -slope * (x - right_end) 
    outside_inner_left_arm   = lambda x, y: y + y_lim >= slope  * (x - (left_end+width)) 
    outside_inner_right_arm  = lambda x, y: y + y_lim >= -slope * (x - (right_end-width)) 

    return (-width <= y <= 0 or y_lim-width <= y <= y_lim)  and (inside_outer_left_arm(x, y) and inside_outer_right_arm(x, y)) \
        or (-y_lim <= y <= -width or 0 <= y <= y_lim-width) and (inside_outer_left_arm(x, y) and outside_inner_left_arm(x, y) or inside_outer_right_arm(x, y) and outside_inner_right_arm(x, y))

def assert_B(point):

    x, y = get_xy(point)

    curve_left_end = left_end + width
    outer_major_axis = right_end - curve_left_end
    outer_minor_axis = y_lim / 2
    inner_major_axis = outer_major_axis - width 
    inner_minor_axis = outer_minor_axis - width

    inside_upper_outer_curve  = lambda x, y: outer_minor_axis**2 * (x-curve_left_end)**2 + outer_major_axis**2 * (y-outer_minor_axis)**2 <= outer_minor_axis**2 * outer_major_axis**2 
    inside_lower_outer_curve  = lambda x, y: outer_minor_axis**2 * (x-curve_left_end)**2 + outer_major_axis**2 * (y+outer_minor_axis)**2 <= outer_minor_axis**2 * outer_major_axis**2 
    outside_upper_inner_curve = lambda x, y: inner_minor_axis**2 * (x-curve_left_end)**2 + inner_major_axis**2 * (y-outer_minor_axis)**2 >= inner_minor_axis**2 * inner_major_axis**2 
    outside_lower_inner_curve = lambda x, y: inner_minor_axis**2 * (x-curve_left_end)**2 + inner_major_axis**2 * (y+outer_minor_axis)**2 >= inner_minor_axis**2 * inner_major_axis**2 

    return (-outer_minor_axis <= y-outer_minor_axis <= outer_minor_axis or -outer_minor_axis <= y+outer_minor_axis <= outer_minor_axis) and (left_end <= x <= left_end+width) or \
        left_end+width <= x <= right_end and (inside_upper_outer_curve(x, y) and outside_upper_inner_curve(x, y) or inside_lower_outer_curve(x, y) and outside_lower_inner_curve(x, y))

def assert_C(point, center=1, theta=pi/3):

    x, y = get_xy(point)

    return  (x-center)**2 + y**2 <= y_lim**2 \
        and (x-center)**2 + y**2 >= (y_lim-1)**2 \
        and (x <= 0 or abs(y/(x-center)) >= tan(theta))

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

def assert_E(point):

    x, y = get_xy(point)

    ...

assert_funcs = {
    'A': assert_A,
    'B': assert_B,
    'C': assert_C,
    'D': assert_D,
    # 'E': assert_E,
    # 'F': assert_F,
    # 'G': assert_G,
    # 'H': assert_H,
    # 'I': assert_I,
    # 'J': assert_J,
    # 'K': assert_K,
    # 'L': assert_L,
    # 'M': assert_M,
    # 'N': assert_N,
    # 'O': assert_O,
    # 'P': assert_P,
    # 'Q': assert_Q,
    # 'R': assert_R,
    # 'S': assert_S,
    # 'T': assert_T,
    # 'U': assert_U,
    # 'V': assert_V,
    # 'W': assert_W,
    # 'X': assert_X,
    # 'Y': assert_Y,
    # 'Z': assert_Z
}


if __name__ == '__main__':

    import argparse
    import sys
    import numpy as np
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser(description=__doc__.strip().split('\n')[0], add_help=False)
    parser.add_argument('letter', type=str)
    args = parser.parse_args()

    letter = args.letter.upper()
    assert_func = assert_funcs[letter]

    sample_size = 10_000
    sample = np.random.uniform(-y_lim, y_lim, (sample_size, 2)).tolist()
    sample = [point for point in sample if assert_func(point)]

    plt.scatter(*zip(*sample))
    plt.xlim(-y_lim, y_lim)
    plt.ylim(-y_lim, y_lim)
    plt.show()