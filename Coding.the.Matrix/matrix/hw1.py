# Please fill out this stencil and submit using the provided submission script.

from GF2 import one



## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [-1,7]
p1_v_minus_u = [-1,-1]
p1_three_v_minus_two_u = [-3,1]



## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [1,0,6]
p2_v_minus_u = [3,-2,4]
p2_two_v_minus_u = [5,-3,9]
p2_v_plus_two_u = [0,1,7]



## Problem 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [one,0,0]
p3_vector_sum_2 = [0,one,one]



## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.

def check_key(keys):
    key_set = set()
    for k in keys:
        if k != ' ':
            if k not in key_set:
                key_set.add(k)
            else:
                return False
    return True

def solve_p4(data,result):
    keys = [' ','a','b','c','d','e','f']
    result_set = set()
    for k1 in keys:
        for k2 in keys:
            for k3 in keys:
                for k4 in keys:
                    for k5 in keys:
                        for k6 in keys:
                                kk = [k1,k2,k3,k4,k5,k6]
                                #make sure each key is used only once
                                if check_key(kk):
                                    sum = None
                                    for k in kk:
                                        if k != ' ':
                                            if sum is None:
                                                sum = data[k]
                                            else:
                                                sum = [ x+y for x,y in zip(sum,data[k])]
                                    if sum == result:
                                        #remove duplicates
                                        s = ''
                                        for x in sorted([x for x in kk if x !=' ']):
                                            if x != ' ':
                                                s=s+x
                                        result_set.add(s)

    print(result_set)    

u_0010010 = {'e', 'd', 'c'}
u_0100010 = {'e', 'd', 'c', 'b'}



## Problem 5
# Use the same format as the previous problem

v_0010010 = {'c','d'}
v_0100010 = set()



## Problem 6
uv_a = 5
uv_b = 6
uv_c = 16
uv_d = -1



## Problem 7
# use 'one' instead of '1'

def solve_p7():
    def dot(i,x):
        return sum([ii*xx for ii,xx in zip(i,x)])
    
    l = [0,one]
    for x1 in l:
        for x2 in l:
            for x3 in l:
                for x4 in l:
                    x = [x1,x2,x3,x4]
                    if dot([one,one,0,0],x) == one and dot([one,0,one,0],x) == one and dot([one,one,one,one],x) == one:
                        print(x)

x_gf2 = [one,0,0,0]



## Problem 8
v1 = [2,3,-4,1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]

if __name__ == '__main__':    
    p4   = {'a':[one,one,0,0,0,0,0],
            'b':[0,one,one,0,0,0,0],
            'c':[0,0,one,one,0,0,0],
            'd':[0,0,0,one,one,0,0],
            'e':[0,0,0,0,one,one,0],
            'f':[0,0,0,0,0,one,one]}

    print("p4")
    solve_p4(p4,[0,0,one,0,0,one,0])
    solve_p4(p4,[0,one,0,0,0,one,0])

    print("p5")
    p5 = {'a':[one,one,one,0,0,0,0],
          'b':[0,one,one,one,0,0,0],
          'c':[0,0,one,one,one,0,0],
          'd':[0,0,0,one,one,one,0],
          'e':[0,0,0,0,one,one,one],
          'f':[0,0,0,0,0,one,one]}
    solve_p4(p5,[0,0,one,0,0,one,0])
    solve_p4(p5,[0,one,0,0,0,one,0])

    print("p7")
    solve_p7()
