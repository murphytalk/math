# version code 941
# Please fill out this stencil and submit using the provided submission script.

from GF2 import one
from math import sqrt, pi
from matutil import coldict2mat
from solver import solve
from vec import Vec



## Problem 1
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.
#
# For example, [1, 3, 5] would mean 1*[2,0,4,0] + 3*[0,1,0,1] + 5*[0,0,-1,-1]
# solve(coldict2mat,b)
rep_1 = [1,1,0]
rep_2 = [0.5,1,1]
rep_3 = [0,1,-1]



## Problem 2
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

lin_comb_coefficients_1 = [3,-1,1]
lin_comb_coefficients_2 = [0.5,-1.5,1]
lin_comb_coefficients_3 = [0.5,-5.5,4]
lin_comb_coefficients_4 = [1,-2,1]



## Problem 3
# Use one from the GF2 module, not the integer 1.
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

gf2_rep_1 = [one,0,one,0]
gf2_rep_2 = [one,0,0,one]
gf2_rep_3 = [one,one,0,one]



## Problem 4
# Use one from the GF2 module, not the integer 1.
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

gf2_lc_rep_1 = [one,one,one,0,0,0,0,0]
gf2_lc_rep_2 = [0,0,0,0,0,0,one,one]
gf2_lc_rep_3 = [one,0,0,one,0,0,0,0]
gf2_lc_rep_4 = [one,0,one,0,0,0,0,0]



## Problem 5
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

lin_dep_R_1 = [-2,1,1]
lin_dep_R_2 = [-4,1,-4/7]
lin_dep_R_3 = [-0.3,0,0,1,3]



## Problem 6
# Please record your solution as a list of coefficients

linear_dep_R_1 = [1,-1,3]
linear_dep_R_2 = [sqrt(2),sqrt(2)/(2*pi),0.5]
linear_dep_R_3 = [1,1,1,1,1]



## Problem 7
# Assign the COEFFICIENT of the vector to each variable.
# Assign sum_to to the vector that you are expressing as a linear combination
# of the other two.  Write the name of the vector as a STRING.  i.e. 'u' or 'w'

u = -1
v = 1
w = 1
sum_to = 'w'



## Problem 8
# Please use the Vec class to represent your vectors

indep_vec_1 = Vec({0, 1, 2},{0: 0, 1: 0, 2: 1})
indep_vec_2 = Vec({0, 1, 2},{0: 0, 1: 2, 2: -2})
indep_vec_3 = Vec({0, 1, 2},{0: 1, 1: -2, 2: 1})
indep_vec_4 = Vec({0, 1, 2},{0: 4, 1: 2, 2: 3})



## Problem 9
# Please give your solution as a list of coefficients of the linear combination

zero_comb_1 = [one,one,0,one]
zero_comb_2 = [0,one,one,one]
zero_comb_3 = [one,one,0,0,one]



## Problem 10
# Please give your solution as a list of coefficients of the vectors
# in the set in order (list the coefficient for v_i before v_j if i < j).
#assign one to edges that consist a loop, 0 to the others
sum_to_zero_1 = [0,one,0,one,one]
sum_to_zero_2 = [0,one,0,one,one,0,0,0]
sum_to_zero_3 = [one,0,one,one,one]
sum_to_zero_4 = [one,one,one,one,one,0,0]



## Problem 11
## Please express your answer a list of ints, such as [1,0,0,0,0]
'''
according to the proof,in
z = alpha * A + (beta1*w1+beta2*w2 + ... + beta_n*w_n)
the answer w can be any of w1,..,w_n where its corresponding beta is not 0
'''
exchange_1 = [0,0,1,0,0]
exchange_2 = [0,0,0,1,0]
exchange_3 = [0,0,0,0,1]


## Problem 12
# Please give the name of the vector you want to replace as a string (e.g. 'v1')
'''
in the original graph a~e are connected and no cycle => independent
so the questions is after adding an edge(z), which edge in (S-A) should be removed so

1. a~e remain being connected
2. there is no cycle

'''
replace_1 = 'v3'
replace_2 = 'v1'
replace_3 = 'v4'



## Problem 13
def rep2vec(u, veclist):
    '''
    Input:
        - u: a vector as an instance of your Vec class with domain set(range(len(veclist)))
        - veclist: a list of n vectors (as Vec instances)
    Output:
        vector v (as Vec instance) whose coordinate representation is u
    Example:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> rep2vec(Vec({0,1,2}, {0:2, 1:4, 2:6}), [a0,a1,a2]) == Vec({'a', 'c', 'b', 'd'},{'a': 2, 'c': 6, 'b': 4, 'd': 0})
        True
    '''
    return coldict2mat(veclist)*u

## Problem 14
def vec2rep(veclist, v):
    '''
    Input:
        - veclist: a list of vectors (as instances of your Vec class)
        - v: a vector (as Vec instance) with domain set(range(len(veclist)))
             with v in the span of set(veclist).
    Output:
        Vec instance u whose coordinate representation w.r.t. veclist is v
    Example:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> vec2rep([a0,a1,a2], Vec({'a','b','c','d'}, {'a':3, 'c':-2})) == Vec({0, 1, 2},{0: 3.0, 1: 0.0, 2: -2.0})
        True
    '''
    #reverse operation of #13 : need to solve u where M*u=v
    return solve(coldict2mat(veclist),v)



## Problem 15
def is_superfluous(L, i):
    '''
    Input:
        - L: list of vectors as instances of Vec class
        - i: integer in range(len(L))
    Output:
        True if the span of the vectors of L is the same
        as the span of the vectors of L, excluding L[i].

        False otherwise.
    Examples:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> is_superfluous(L, 3)
        True
        >>> is_superfluous([a0,a1,a2,a3], 3)
        True
        >>> is_superfluous([a0,a1,a2,a3], 0)
        True
        >>> is_superfluous([a0,a1,a2,a3], 1)
        False
    '''
    if len(L) == 1:
        return False
    
    A = coldict2mat(L[:i]+L[i+1:])
    x = solve(A,L[i])
    residual = L[i] - A*x
    
    if (residual*residual)<1e-14:
        return True
    else:
        return False



## Problem 16
def is_independent(L):
    '''
    input: a list L of vectors (using vec class)
    output: True if the vectors form a linearly independent list.
    >>> vlist = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0})]
    >>> is_independent(vlist)
    False
    >>> is_independent(vlist[:3])
    True
    >>> is_independent(vlist[:2])
    True
    >>> is_independent(vlist[1:4])
    True
    >>> is_independent(vlist[2:5])
    True
    >>> is_independent(vlist[2:6])
    False
    >>> is_independent(vlist[1:3])
    True
    >>> is_independent(vlist[5:])
    True
    '''
    for i in range(len(L)):
        if(is_superfluous(L,i)):
            return False

    return True



## Problem 17
def superset_basis(S, L):
    '''
    Input: 
        - S: linearly independent list of Vec instances
        - L: list of Vec instances such that every vector in S is in Span(L)
    Output:
        Linearly independent list T containing all vectors (as instances of Vec)
        such that the span of T is the span of L (i.e. T is a basis for the span
        of L).
    Example:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> superset_basis([a0, a3], [a0, a1, a2]) == [Vec({'a', 'c', 'b', 'd'},{'a': 1}), Vec({'a', 'c', 'b', 'd'},{'b':1}),Vec({'a', 'c', 'b', 'd'},{'c': 1})]
        True
    '''
    def is_already_in_S(x):
        for i in S:
            if x==i:
                return True
        return False
    
    for x in L:
        if not is_already_in_S(x):            
            if is_independent(S+[x]):
                S.append(x)
            else:
                return S



def has_same_span(vecs1,vecs2):
    '''
    s1=[ list2vec(x) for x in [[1,2,-1],[0,1,1],[2,5,-1]]]
    s2=[ list2vec(x) for x in [[-2,-6,0],[1,1,-2]]]
    has_same_span(s1,s2) == True
    '''
    def is_linear_comb(vec,v):
        A = coldict2mat(vec)
        x = solve(A,v)
        #print("x=%s"%x)
        residual = v - A*x
        #print("res=",residual*residual)
        if (residual*residual)<1e-14:
            return True
        else:
            return False
        
    for v in vecs1:
        if not is_linear_comb(vecs2,v):
            return False

    for v in vecs2:
        if not is_linear_comb(vecs1,v):
            return False

    return True
        

## Problem 18
def exchange(S, A, z):
    '''
    Input:
        - S: a list of vectors, as instances of your Vec class
        - A: a list of vectors, each of which are in S, with len(A) < len(S)
        - z: an instance of Vec such that A+[z] is linearly independent
    Output: a vector w in S but not in A such that Span S = Span ({z} U S - {w})
    Example:
        >>> S = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]]
        >>> A = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]]
        >>> z = list2vec([0,2,1,1])
        >>> exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})
        True

    Example2:    

    S = [list2vec(v) for v in [[3,67,8,4],[0,6,3,4],[5,9,5,2],[67,342,567,5],[9,5,9,0],[7,4,5,3],[34,7,65,3]]]
    A = [list2vec(v) for v in [[3,67,8,4],[0,6,3,4]]]
    z = list2vec([0,0,0,1])
    >>> print(test_format((exchange(S, A, z) == list2vec([9,5,9,0])) or (exchange(S, A, z) == list2vec([7,4,5,3])) or (exchange(S, A, z) == list2vec([34, 7, 65, 3]))))
    False
    >>> print(test_format((exchange(S, A, z) == list2vec([5,9,5,2])) or (exchange(S, A, z) == list2vec([67,342,567,5]))))
    True
    '''
    #solve u where S*u=z
    u = vec2rep(S,z)

    #according to the proof, the w is those in S-A which have a non-zero cofficient
    index_in_S = [k for  k,v in u.f.items() if v!=0 ]
    results = [ S[i] for i in index_in_S if not S[i] in A]

    if len(results)>0:
        #print(coldict2mat(results))
        return results[0]
    else:
        return None

