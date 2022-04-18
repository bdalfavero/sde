#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# brown.py -- simulation of brownian motion with lagnevin eqns


def dw(dt):

    return np.random.normal(scale=np.sqrt(dt))


def f(s, m, lam, g, dt):
    """
    derivative of vector (vx, vy, x, y)
    """

    # calculate vector elements without reflection
    ds = np.zeros(4)
    ds[0] = -(lam / m) * s[0] * dt + (g / m) * dw(dt)
    ds[1] = -(lam / m) * s[1] * dt + (g / m) * dw(dt)
    ds[2] = s[0]
    ds[3] = s[1]

    # modify velocity if the particle is outside the walls
    # specular reflection with householder transformation
    """
    if s[2] >= 1.0:
        # right wall
        ds[0] = -ds[0]
    if s[2] <= 0.0:
        # left wall
        ds[0] = -ds[0]
    if s[3] >= 1.0:
        # upper wall
        ds[1] = -ds[1]
    if s[3] <= 0.0:
        # lower wall
        ds[1] = -ds[1]
    """

    return ds


def solve_trajectory(sinit, tmax, nstep, eqn_prms):
    """
    solve for a trajectory with given paramters
    """

    # float value for time step
    dt = tmax / float(nstep)

    # allocate array for trajectory
    sv = np.zeros((4, nstep + 1))
    sv[:, 0] = sinit

    # anonymous function to return derivative
    deriv = lambda s: f(s, eqn_prms['m'], eqn_prms['lam'], \
    eqn_prms['g'], tmax / float(nstep))

    # loop over euler steps
    s = sinit
    t = 0.0
    for i in range(1, nstep + 1):
        sv[:, i] = sv[:, i - 1] + deriv(s)
        s = sv[:, i]
        t = t + dt

    return sv


def main():
    
    eqn_params = {
        'm': 1.0,
        'lam': 0.5,
        'g': 0.0
    }

    tmax = 10.0
    nstep = 10000

    sinit = np.zeros(4)
    sinit[0] = np.random.rand()
    sinit[1] = np.random.rand()
    sinit[2] = 0.01 * np.random.rand()
    sinit[3] = 0.01 * np.random.rand()

    sv = solve_trajectory(sinit, tmax, nstep, eqn_params)
    vx = sv[0, :]
    vy = sv[1, :]
    x = sv[2, :]
    y = sv[3, :]

    # derived quantities
    r = np.sqrt(x ** 2 + y ** 2)
    v = np.sqrt(vx ** 2 + vy ** 2)

    fig, axs = plt.subplots(1, 2)
    axs[0].plot(x, y, '-o', markersize=1.0)
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[0].set_title('position')
    axs[1].plot(vx, vy, '-o', markersize=1.0)
    axs[1].set_xlabel('$v_x$')
    axs[1].set_ylabel('$v_y$')
    axs[1].set_title('velocity')

    fig1, axs1 = plt.subplots(1, 2)
    axs1[0].plot(r)
    axs1[0].set_title('distance')
    axs1[1].plot(v)
    axs1[1].set_title('velocity')

    plt.show()


if __name__ == "__main__":
    main()
