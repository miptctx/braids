from sage.all import *

a, b, c, d = 1, 2, 3, 4
A = matrix(CC, [[a,b],[c,d]])

A_inv = A.inverse()
a_inv, b_inv, c_inv, d_inv = A_inv[0][0], A_inv[0][1], A_inv[1][0], A_inv[1][1]

A_inv_3 = A**(-3)
a_inv_3, b_inv_3, c_inv_3, d_inv_3 = A_inv_3[0][0], A_inv_3[0][1], A_inv_3[1][0], A_inv_3[1][1]


n = matrix(CC, [
  [0, 0, a, b, -a_inv, -b_inv, 0, 0],
  [0, 0, c, d, -c_inv, -d_inv, 0, 0]
])


u = matrix(CC, [
  [0, 0],
  [0, 0],
  [-a, -b],
  [-c, -d],
  [a_inv, b_inv],
  [c_inv, d_inv],
  [0, 0],
  [0, 0]
])


R = matrix(CC, [
  [a,b,0,0,0,0,0,0],
  [c,d,0,0,0,0,0,0],
  [0,0,0,0,a_inv,b_inv,0,0],
  [0,0,0,0,c_inv,d_inv,0,0],
  [0,0,a_inv,b_inv,a-a_inv_3,b-b_inv_3,0,0],
  [0,0,c_inv,d_inv,c-c_inv_3,d-d_inv_3,0,0],
  [0,0,0,0,0,0,a,b],
  [0,0,0,0,0,0,c,d]
])


'''
idv = matrix(CC, [
  [1,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1]
])
'''
idv = matrix(CC, [
  [1,0],
  [0,1]
])


print('trefoil')
a_0 = u
a_1 = idv.tensor_product(idv).tensor_product(u)
a_2 = idv.tensor_product(R.inverse()).tensor_product(idv)
a_3 = R.tensor_product(idv).tensor_product(idv)
a_4 = idv.tensor_product(R.inverse()).tensor_product(idv)
a_5 = idv.tensor_product(idv).tensor_product(n)
a_6 = n

#print("a_1")
#show(a_1)
#print("a_0")
#show(a_0)

# m = a_0*a_1*a_2*a_3*a_4*a_5*a_6
m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(m)

print('opposit trefoil')
a_0 = u
a_1 = idv.tensor_product(idv.tensor_product(u))
a_2 = idv.tensor_product(R.tensor_product(idv))
a_3 = R.inverse().tensor_product(idv.tensor_product(idv))
a_4 = idv.tensor_product(R.tensor_product(idv))
a_5 = idv.tensor_product(idv.tensor_product(n))
a_6 = n

m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(m)


print('trivial')
a_0 = u
a_1 = idv.tensor_product(idv.tensor_product(u))
a_2 = idv.tensor_product(R.inverse().tensor_product(idv))
a_3 = R.tensor_product(idv.tensor_product(idv))
a_4 = idv.tensor_product(R.tensor_product(idv))
a_5 = idv.tensor_product(idv.tensor_product(n))
a_6 = n

m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(m)

print('trivial link')
show(a_6*a_0)
