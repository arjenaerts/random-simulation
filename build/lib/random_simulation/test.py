import rand_f as rf
import rand_c as rc

""" 
Test script that can be run from the terminal.
"""

nr_draws = 1000

# tests random function

rand_nrs = rf.draw(1000, 'normal')
print('normal default: ', rand_nrs.mean())

rand_nrs = rf.draw(1000, 'poisson')
print('poisson default: ', rand_nrs.mean())

rand_nrs = rf.draw(1000, 'binom')
print('binom default: ', rand_nrs.mean())


rand_nrs = rf.draw(1000, 'normal', mu=3, sigma=10)
print('normal default: ', rand_nrs.mean())

rand_nrs = rf.draw(1000, 'poisson', mu=4)
print('poisson default: ', rand_nrs.mean())

rand_nrs = rf.draw(1000, 'binom', n=100, p=0.5)
print('binom default: ', rand_nrs.mean())

# tests random class

simulation = rc.SimRandVar('normal')
simulation.summarise()
rand_nrs = simulation.draw(1000)
print('normal default: ', rand_nrs.mean())

simulation.summarise()