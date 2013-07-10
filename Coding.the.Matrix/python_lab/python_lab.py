## Task 1
minutes_in_week = 7*24*60

## Task 2
remainder_without_mod = 2304811 - (2304811//47)*47

## Task 3
divisible_by_3 = (673+909)%3 == 0

## Task 4
x = -9
y = 1/2
statement_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares = { x*x for x in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = { 4, 5, 6 }
Y1 = { 7, 8, 9 }

## Task 8: enter in the two new sets
### My trick : Simplify the production to addition by using exponent
X2 = {2**1,2**2,2**3}
Y2 = {2**9,2**8,2**7}

## Task 9
'''
Task 9 asks you to return a set of all the base 10 numbers that do not exceed 3 digits in the given base system.
If the given base is 10, then the set is obviously {1,2,3,...,998,999}, because 1000 is 4 digits.
If the base is 2, then the output is {1,2,3,4,5,6,7} because 7 in base 2 is 111,
which is the last 3 digit number in base 2.
'''
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = { x1*base*base+x2*base+x3 for x1 in digits for x2 in digits for x3 in digits}

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T =  {s  for s in S for t in T if s == t}

## Task 11
L_average = sum( [20, 10, 15, 75] )/4

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(x) for x in LofL])

## Task 13
cartesian_product = [ [x,y] for x in {'A','B','C'} for y in {1,2,3} ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(i,j,k) for i in S for j in S for k in S if i+j+k == 0]

## Task 15
exclude_zero_list = [(i,j,k) for i in S for j in S for k in S if i+j+k == 0 and not (i==j and j==k)]

## Task 16
first_of_tuples_list = [(i,j,k) for i in S for j in S for k in S if i+j+k == 0 and not (i==j and j==k)][0]

## Task 17
L1 = [1,1,2] # <-- want len(L1) != len(list(set(L1)))
L2 = [3,2,1] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {...}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = ...

## Task 20
list_sum_zip = [...]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [...]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [...] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [...] # <-- as you do here

## Task 23
square_dict = {...}

## Task 24
D = {'red','white','blue'}
identity_dict = {...}

## Task 25
base = 10
digits = set(range(10))
representation_dict = {...}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = { ... }

## Task 27
def nextInts(L): return [ ... ]

## Task 28
def cubes(L): return [ ... ] 

## Task 29
def dict2list(dct, keylist): return [ ... ]

## Task 30 
def list2dict(L, keylist): return { ... } 

