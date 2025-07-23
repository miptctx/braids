from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

# PR = PolynomialRing(QQ, 'm,l,k,j,i')
PR = PolynomialRing(QQ, 'm,l,k,j,i')
PR.inject_variables()

print(i < j)

F = PR.fraction_field()

# show(vector(F, [(k + j)/(l - m)]))

# P = sort_triangulation({1,2,3}, {1,3,4}, {1,4,5})
P = sort_triangulation({i,j,k}, {i,k,l}, {i,l,m})

# t, matrix = braiding(P, {1,4},{1,3},{3,5},{2,5},{2,4})
t, matrix = braiding(P, {i,l},{i,k},{k,m},{j,m},{j,l}, F=F)


#show(P)
#show(t)
#assert P == t

print('################')
print_triangles_pretty(t, justify=4)
# show(t)
print(matrix)
