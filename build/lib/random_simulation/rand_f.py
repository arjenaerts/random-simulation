from scipy import stats
import random as rd
import numpy as np

"""
Function that draws n_samples random numbers from dist_type (normal, poisson or binom). Additional 
keyword arguments can be added, depending on chosen distribution (mu and sigma for normal, mu for poission and n and p 
for binom).
"""


def draw(n_samples, dist_type, **kwargs):
    u_array = np.array([rd.random() for i in range(n_samples)])
    if dist_type == 'normal':
        mu = kwargs.get('mu', 0)
        sigma = kwargs.get('sigma', 1)
        return np.array([stats.norm.ppf(u, loc=mu, scale=sigma) for u in u_array])
    elif dist_type == 'poisson':
        mu = kwargs.get('mu', 1)
        return np.array([stats.poisson.ppf(u, mu=mu) for u in u_array])
    elif dist_type == 'binom':
        n = kwargs.get('n', 1)
        p = kwargs.get('p', 0.5)
        return np.array([stats.binom.ppf(u, n=n, p=p) for u in u_array])
    else:
        raise ValueError("dist_type must equal normal, poisson or binom")