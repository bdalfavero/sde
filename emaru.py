#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# parameters
tmax = 10.0
nstep = 1000
nsample = 5
dt = tmax / float(nstep)
xinit = 1.0
a = 0.5 # decay constant in exponential
g = 1e-1 # coefficient of brownian motion

def dw(dt):
    """
    sample the brownian motion as a gaussian distribution
    with given standard deviation, and centered about zero.
    """
    
    return np.random.normal(scale=np.sqrt(dt))

def mu(x, t):
    """
    mu in dx = mu(x, t) dt + sigma(x, t) dw
    """
    
    return -a * x

def sigma(x, t):
    """
    sigma coefficient
    """
    
    return g

# allocate arrays for both solutions
xel = np.zeros(nstep + 1) # euler solution
xel[0] = xinit
xem = np.zeros((nsample, nstep + 1)) # euler-maruyama soln
xem[:, 0] = xinit

# solve for euler result
t = 0.0
x = xel[0]
for i in range(1, nstep + 1):
    # step through with euler method
    xel[i] = x + mu(x, t) * dt + 0.0 * dw(dt)
    x = xel[i]
    t = t + dt

# solve for stochastic  result
for j in range(nsample):
    t = 0.0
    x = xem[j, 0]
    for i in range(1, nstep + 1):
        # step through with euler method
        xem[j, i] = x + mu(x, t) * dt + sigma(x, t) * dw(dt)
        x = xem[j, i]
        t = t + dt


# plot solution
plt.plot(xel, 'k--')
plt.plot(np.transpose(xem), '-')
plt.show()
