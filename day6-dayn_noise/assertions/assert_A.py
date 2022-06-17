def assert_A(point):

    x, y = point

    assert isinstance(x, float) and isinstance(y, float)

    inside_outer_left_arm    = lambda x, y: y < 10  * (x+3) / 3.5
    inside_outer_right_arm   = lambda x, y: y < -10 * (x-3) / 3.5
    outside_inner_left_arm   = lambda x, y: y > 10  * (x+2) / 3.5
    outside_inner_right_arm  = lambda x, y: y > -10 * (x-2) / 3.5

    return (-1 <= y <= 0 or 4 <= y <= 5)  and (inside_outer_left_arm(x, y) and inside_outer_right_arm(x, y)) \
        or (-5 <= y <= -1 or 0 <= y <= 4) and (inside_outer_left_arm(x, y) and outside_inner_left_arm(x, y) or inside_outer_right_arm(x, y) and outside_inner_right_arm(x, y))

if __name__ == '__main__':

    import numpy as np
    import matplotlib.pyplot as plt

    sample_size = 10_000
    sample = np.random.uniform(-10, 10, (sample_size, 2)).tolist()
    sample = [point for point in sample if assert_A(point)]

    plt.scatter(*zip(*sample))
    plt.show()