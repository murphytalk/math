from math import sqrt
from orthogonalization import orthogonalize

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    L_star = orthogonalize(L)
    L_norm = [ sqrt(v*v) for v in L_star ]
    return [ L_star[i]/L_norm[i] for i in range(len(L_star)) ]

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    pass
