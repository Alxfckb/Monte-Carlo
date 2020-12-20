'''
You throw two dice, one black and one green.
What is the probability that the number of eyes on the black die is larger than the number of eyes on the green die?
'''
import sys
import numpy as np
import random
'''
M = 0
N = 10**6
for i in range(N):
    black = random.randint(1, 6)
    brown = random.randint(1, 6)
    if black > brown:
        M+=1

p = float(M)/N * 100
'''

N = 10**6                                                                       # Number of throws
r = np.random.random_integers(1, 6, size=(2, N))
black = r[0,:]                                                                  # Eyes for all throws with black green = r[1,:]
green = r[1,:]
success = black > green                                                         # success[i] is true if black[i]>green[i]
M = np.sum(success)                                                             # Sum up all successes
p = float(M)/N                                                                  # Compute the probability

print(p*100)
