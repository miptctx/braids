from sage.all import *

A = var('A')

F = SR

n = matrix(F, [[0, sqrt(-1)*A, -sqrt(-1)*A**(-1), 0]])
u = n.transpose()

U = n.tensor_product(u)

I = matrix(F, [[1, 0], [0, 1]])

R = A*U + A**(-1)*I.tensor_product(I)

print("U")
show(U)

print("")
print("R")
show(R)

print("")
print("####################")
print("### Trivial loop ###")
print("####################")
m = n*u
print(m)

print("")
print("#########################################")
print("### Trivial with 2 reidemeister moves ###")
print("#########################################")
a_1 = u
a_2 = u.tensor_product(I).tensor_product(I)
a_3 = I.tensor_product(R.inverse()).tensor_product(I)
a_4 = n.tensor_product(I).tensor_product(I)

a_5 = u.tensor_product(I).tensor_product(I)
a_6 = I.tensor_product(R).tensor_product(I)
a_7 = n.tensor_product(I).tensor_product(I)

a_8 = n

m = a_8*a_7*a_6*a_5*a_4*a_3*a_2*a_1
m = m.simplify_full()

show(m)


print("")
print("###########################################################################")
print("### Trivial with 2 reidemeister moves each on the opposite site of knot ###")
print("###########################################################################")
a_1 = u
a_2 = u.tensor_product(I).tensor_product(I)
a_3 = I.tensor_product(R.inverse()).tensor_product(I)
a_4 = n.tensor_product(I).tensor_product(I)

a_5 = I.tensor_product(I).tensor_product(u)
a_6 = I.tensor_product(R).tensor_product(I)
a_7 = I.tensor_product(I).tensor_product(n)

a_8 = n

m = a_8*a_7*a_6*a_5*a_4*a_3*a_2*a_1
m = m.simplify_full()

show(m)


print("")
print("############################################################################")
print("### Trivial with 2 reidemeister moves one of them on the top of the knot ###")
print("############################################################################")
a_1 = u
a_2 = u.tensor_product(I).tensor_product(I)
a_3 = I.tensor_product(R.inverse()).tensor_product(I)
a_4 = n.tensor_product(I).tensor_product(I)

a_5 = R.inverse()
a_6 = n

m = a_6*a_5*a_4*a_3*a_2*a_1
m = m.simplify_full()

show(m)
