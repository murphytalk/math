from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon

## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    return 0 if (i%2)==0 else one
    

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset,{f:int2GF2(e) for f,e in factors})

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots = []
    rowlists = []

    target_count = len(primeset) +1
    x = intsqrt(N)+2
    while(len(roots)<target_count):
        factors = dumb_factor(x*x-N,primeset)
        if len(factors)>0:
            v = make_Vec(primeset,factors)
            roots.append(x)
            rowlists.append(v)
        x = x+1
    return (roots,rowlists)

## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist = [ roots[i] for i in range(len(roots)) if (i in v.f) and v.f[i]==one ]
    a = prod(alist)
    c = prod([x*x-N for x in alist])
    b = intsqrt(c)
    #print("b*b=%d,c=%d"%(b*b,c))
    assert(b*b==c)
    return (a,b)

def solve(N,primelist):
    roots,rowlist = find_candidates(N,primelist)
    M = echelon.transformation_rows(rowlist)
    index = -1
    while True:
        v = M[index:][0]
        a,b = find_a_and_b(v,roots,N)
        g = gcd(a-b,N)
        if g!=1:
            return g
        else:
            index = index -1
    
## Task 5

smallest_nontrivial_divisor_of_2461799993978700679 = 1230926561
#solve(2461799993978700679,primes(10000))
