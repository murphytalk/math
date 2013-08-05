# version code 761
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec



## Problem 1
def vec_select(veclist, k): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    return [ v for v in veclist if v[k] == 0 ]

def vec_sum(veclist, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    return Vec(D,{ k:sum([ v[k] for v in veclist ]) for k in D})

def vec_select_sum(veclist, k, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    return vec_sum(vec_select(veclist,k),D)



## Problem 2
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
    True
    '''
    return [Vec(v1.D,{k2:float(v2)/k1 for k2,v2 in v1.f.items()}) for k1,v1 in vecdict.items()]



## Problem 3
from GF2 import one
def GF2_span(D, L):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
    >>> len(GF2_span(D, L))
    4
    >>> Vec(D, {}) in GF2_span(D, L)
    True
    >>> Vec(D, {'b': one}) in GF2_span(D, L)
    True
    >>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
    True
    >>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
    True
    '''
    def if_vec_used(working_vec,cof_v_pair):
        '''
        when generate the other vectors in the space,
        in the form k1*v1 + k2*v2 + ... kn*vn
        each vector can only be used once
        '''
        for a,v in working_vec:
            if v == cof_v_pair[1]:
                return True
        return False
        
    def gen(vec_num,working_vec,l,result):
        if(len(working_vec)<vec_num):
            for x in l:
                if not if_vec_used(working_vec,x):
                    working_vec.append(x)
                    gen(vec_num,working_vec,l,result)
            if(len(working_vec)):
                working_vec.pop()
        else:
            #print(working_vec)
            #Now we have all full formed coefficient(scalar) and pairs: (k1,v1) , (k2,v2) , ...,(kn,vn)
            #apply the scalars and add the vectors
            s = sum([a*v for a,v in working_vec])

            #do not add it if it has already been spotted
            duplicate = False
            for v in result:
                if( s == v):
                    #print("dup")
                    duplicate = True
                    break
            if(not duplicate):
                result.append(s)
            if(len(working_vec)):
                working_vec.pop()
            
    #get all combinatins of coefficients and vectors
    l = [ (a,v) for a in (0,one) for v in L]

    res = []
    gen(len(L),[],l,res)
    return res
    

## Problem 4
# Answer with a boolean, please.

is_it_a_vector_space_1 = True
is_it_a_vector_space_2 = False



## Problem 5
is_it_a_vector_space_3 = True
is_it_a_vector_space_4 = False


## Problem 6
is_it_a_vector_space_5 = True
is_it_a_vector_space_6 = False
