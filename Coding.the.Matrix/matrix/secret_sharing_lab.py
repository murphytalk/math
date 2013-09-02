# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from vec import Vec
from independence import is_independent
from itertools import combinations


## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = Vec(a0.D,{i:randGF2() for i in range(6)})
        if a0*u == s and b0*u ==t:
            return u    

## Problem 2
# Give each vector as a Vec instance
def gen():
    while True:
        vecs = [(a0,b0)]
        while len(vecs)<5:
            vecs.append(( Vec(a0.D,{i:randGF2() for i in range(6)}),Vec(a0.D,{i:randGF2() for i in range(6)})))
        if all(is_independent(list(sum(x,()))) for x in combinations(vecs,3)):
            return vecs
        
secret_a0 = a0
secret_b0 = b0
secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: 0, 4: 0, 5: 0})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: 0, 4: 0, 5: one})
secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: 0, 4: 0, 5: 0})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: one, 4: one, 5: 0})
secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: 0, 4: one, 5: one})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: 0, 4: 0, 5: 0})
secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: 0, 4: one, 5: one})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: one, 4: 0, 5: 0})


