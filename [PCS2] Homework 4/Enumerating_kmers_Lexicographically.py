from itertools import product

f = open("rosalind_lexf.txt", 'r')
a = list(f.readline().rstrip().split())
n = int(f.readline().rstrip())
f.close()

for perm in product(a, repeat=n): 
    print( "".join(perm))

