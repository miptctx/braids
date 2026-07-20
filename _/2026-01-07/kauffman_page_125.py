from sage.all import *

A = var('A')

F = SR

M = matrix(F, [[0, sqrt(-1)*A, -sqrt(-1)*A**(-1), 0]])

U = M.tensor_product(M.transpose())

I = matrix(F, [[1, 0], [0, 1]])

R = A*U + A**(-1)*I.tensor_product(I)

print("U")
show(U)

print("")
print("R")
show(R)

print("")
print("###########################")
print("### Trefoil calculation ###")
print("###########################")
N = M
M = M.transpose()
a_0 = M
a_1 = I.tensor_product(I.tensor_product(M))
a_2 = I.tensor_product(R.inverse().tensor_product(I))
a_3 = R.tensor_product(I.tensor_product(I))
a_4 = I.tensor_product(R.inverse().tensor_product(I))
a_5 = I.tensor_product(I.tensor_product(N))
a_6 = N

m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.simplify_full()

show(m)


print("")
print("######################")
print("### Mirrot trefoil ###")
print("######################")
a_0 = M
a_1 = I.tensor_product(I.tensor_product(M))
a_2 = I.tensor_product(R.tensor_product(I))
a_3 = R.inverse().tensor_product(I.tensor_product(I))
a_4 = I.tensor_product(R.tensor_product(I))
a_5 = I.tensor_product(I.tensor_product(N))
a_6 = N

m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.simplify_full()

show(m)


print("")
print("###########################")
print("### Trivial calculation ###")
print("###########################")
a_0 = M
a_1 = I.tensor_product(I.tensor_product(M))
a_2 = I.tensor_product(R.tensor_product(I))
a_3 = R.tensor_product(I.tensor_product(I))
a_4 = I.tensor_product(R.inverse().tensor_product(I))
a_5 = I.tensor_product(I.tensor_product(N))
a_6 = N

m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.simplify_full()

show(m)



print("")
print("#########################################")
print("### Trefoil with 2 reidemeister moves ###")
print("#########################################")
a_0 = M
a_1 = I.tensor_product(I).tensor_product(M)
a_2 = I.tensor_product(R.inverse()).tensor_product(I)
a_3 = I.tensor_product(I).tensor_product(I).tensor_product(I).tensor_product(M)
a_4 = I.tensor_product(I).tensor_product(I).tensor_product(R).tensor_product(I)
a_5 = R.tensor_product(I).tensor_product(I).tensor_product(I).tensor_product(I)
a_6 = I.tensor_product(I).tensor_product(I).tensor_product(I).tensor_product(N)
a_7 = I.tensor_product(I).tensor_product(I).tensor_product(I).tensor_product(M)
a_8 = I.tensor_product(I).tensor_product(I).tensor_product(R.inverse()).tensor_product(I)
a_9 = I.tensor_product(I).tensor_product(I).tensor_product(I).tensor_product(N)
a_10 = I.tensor_product(R.inverse()).tensor_product(I)
a_11 = I.tensor_product(I).tensor_product(N)
a_12 = N

m = a_12*a_11*a_10*a_9*a_8*a_7*a_6*a_5*a_4*a_3*a_2*a_1*a_0
m = m.simplify_full()

show(m)


################################################################
print("")
print("### Deformation ###")

var('c_1,c_2,c_3,d_1,d_2,d_3')
var('e_1,e_2,e_3,f_1,f_2,f_3')

m_0 = matrix([
  [c_1],
  [c_2],
  [c_3]])
m_1 = matrix([
  [1,0,0],
  [0,1,0],
  [0,0,d_1],
  [0,0,d_2],
  [0,0,d_3]
])
m_2 = matrix([
  [1,0,0,0,0],
  [0,e_1,e_2,0,e_3],
  [0,0,0,1,0]
])
m_3 = matrix([[f_1,f_2,f_3]])

m = m_3*m_2*m_1*m_0
print(m, '=', '-A^2 - A^(-2)')
print(m.simplify_full(), '=', '-A^2 - A^(-2)')
