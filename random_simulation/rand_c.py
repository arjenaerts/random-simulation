from scipy import stats
import random as rd
import numpy as np

"""
Class that simulates random variables from a specified distribution (normal, poisson or binom)
"""


class SimRandVar:
    def __init__(self, dist_type, **kwargs):
        self.dist_type = dist_type
        if self.dist_type == 'normal':
            self.mu = kwargs.get('mu', 0)
            self.sigma = kwargs.get('sigma', 1)
        elif self.dist_type == 'poisson':
            self.mu = kwargs.get('mu', 1)
        elif self.dist_type == 'binom':
            self.n = kwargs.get('n', 1)
            self.p = kwargs.get('p', 0.5)
        else:
            raise ValueError("dist_type must equal normal, poisson or binom")
        self.rand_nrs = np.array([])

    def draw(self, n_samples):
        u_array = np.array([rd.random() for i in range(n_samples)])
        if self.dist_type == 'normal':
            self.rand_nrs = np.array([stats.norm.ppf(u, loc=self.mu, scale=self.sigma) for u in u_array])
        elif self.dist_type == 'poisson':
            self.rand_nrs = np.array([stats.poisson.ppf(u, mu=self.mu) for u in u_array])
        else:
            self.rand_nrs = np.array([stats.binom.ppf(u, n=self.n, p=self.p) for u in u_array])
        return self.rand_nrs

    def summarise(self):
        if len(self.rand_nrs) == 0:
            print('No random numbers have been drawn yet')
        else:
            print('')
            print('min: ', self.rand_nrs.min())
            print('max: ', self.rand_nrs.max())
            print('mean: ', self.rand_nrs.mean())
            print('std: ', self.rand_nrs.std())
            print('')