from sage.all import *


#A = matrix(CC, [[1,2],[3,4]])
A = matrix(CC, [1])

n = matrix(CC, [0, 1, -1, 0]).tensor_product(A)
u = matrix(CC, [0, -1, 1, 0]).transpose().tensor_product(A)

#n = matrix(CC, [0, I, -I, 0])
#u = matrix(CC, [0, -I, I, 0]).transpose()

#print("u*n")
#show(u*n)
#print("")


R = matrix(CC, [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]).tensor_product(A)
# show(R)

idv = matrix(CC, [[1,0],[0,1]]).tensor_product(identity_matrix(CC, A.nrows()))


print('trefoil')
a_0 = u
a_1 = idv.tensor_product(idv).tensor_product(u)
a_2 = idv.tensor_product(R.transpose()).tensor_product(idv)
a_3 = R.tensor_product(idv).tensor_product(idv)
a_4 = idv.tensor_product(R.transpose()).tensor_product(idv)
a_5 = idv.tensor_product(idv).tensor_product(n)
a_6 = n

# m = a_0*a_1*a_2*a_3*a_4*a_5*a_6
m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(m)


print('opposit trefoil')
a_0 = u
a_1 = idv.tensor_product(idv.tensor_product(u))
a_2 = idv.tensor_product(R.tensor_product(idv))
a_3 = R.transpose().tensor_product(idv.tensor_product(idv))
a_4 = idv.tensor_product(R.tensor_product(idv))
a_5 = idv.tensor_product(idv.tensor_product(n))
a_6 = n

m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(m)


print('trivial')
a_0 = u
a_1 = idv.tensor_product(idv.tensor_product(u))
a_2 = idv.tensor_product(R.transpose().tensor_product(idv))
a_3 = R.tensor_product(idv.tensor_product(idv))
a_4 = idv.tensor_product(R.tensor_product(idv))
a_5 = idv.tensor_product(idv.tensor_product(n))
a_6 = n

m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(m)
