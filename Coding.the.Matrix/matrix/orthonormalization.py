from math import sqrt
from orthogonalization import orthogonalize,aug_orthogonalize
from vec import Vec

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
    def adjust(v,multipliers):
        return Vec(v.D,{i: v.f[i]*multipliers[i] if i in v.f else 0 for i in v.D})
    
    q,r = aug_orthogonalize(L)
    Qlist = orthonormalize(q)
    Rlist = [ adjust(v,[ sqrt(v*v) for v in orthogonalize(L) ]) for v in r ]
    return Qlist,Rlist
    
