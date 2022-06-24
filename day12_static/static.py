# reference - https://c8.alamy.com/comp/2ER7ATR/pixel-noise-vector-background-of-tv-screen-glitch-texture-digital-and-vhs-video-static-error-pattern-television-no-signal-and-computer-code-glitch-e-2ER7ATR.jpg

import sys

import numpy as np
import matplotlib.pyplot as plt

args = sys.argv[1:]
lims, n = map(int, args) if args else (5, 80)

figsize = 6.4
s = 6 * (figsize / 6.4) / (n / 5)

fig, axs = plt.subplots(1, 1, figsize=(figsize, figsize))

colors = [
    '#897f7d', '#17c1e8', '#215489', '#5210e4', '#2497e3', '#9ed8cf', '#e48938', '#ed5117', '#97ee16', 
    '#1eec5d', '#9c69db', '#dd8eb7', '#d92899', '#39de8d', '#2d7932', '#894a17', '#e2d694', '#46252e', 
    '#d82dc2', '#871a78', '#d2ef35', '#6bcfe1', '#545dd6', '#0f2245', '#0b31db', '#96d858', '#dbbedd', 
    '#923f7f', '#2e928c', '#1be31e', '#dd3b60', '#2d0d8c', '#f8f8f6', '#e1efc2', '#caf1ec', '#144113', 
    '#220e12', '#e0f7f5', '#efd9ef', '#f1f5d8', '#072116', '#070821'
]

state_space = np.linspace(-lims, lims, 2*n*lims+1)
state_space = np.array([(x, y) for x in state_space for y in state_space])
random_indices = np.random.choice(range(state_space.shape[0]), int(1.*state_space.shape[0]), replace=False)
random_sample = state_space[random_indices, :]
random_colors = np.random.choice(colors, random_sample.shape[0])

axs.scatter(random_sample[:, 0], random_sample[:, 1], c=random_colors, s=s**2, marker='s')
axs.set_xlim(-lims, lims)
axs.set_ylim(-lims, lims)
plt.savefig(f'assets/lims-{lims}_n-{n}.png')
plt.show()