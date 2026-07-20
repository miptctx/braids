from sage.all import *

# 2x2 блоки
var('a11 a12 a21 a22 b11 b12 b21 b22 c11 c12 c21 c22 d11 d12 d21 d22')

A = matrix(2,2,[a11,a12,a21,a22])
B = matrix(2,2,[b11,b12,b21,b22])
C = matrix(2,2,[c11,c12,c21,c22])
D = matrix(2,2,[d11,d12,d21,d22])

R = block_matrix([[A,B],[C,D]])

Id2 = identity_matrix(2)
Id8 = identity_matrix(8)

P = (Id2.tensor_product(R) *
     R.inverse().tensor_product(Id2) *
     Id2.tensor_product(R) *
     R.inverse().tensor_product(Id2) *
     Id2.tensor_product(R))

eqns = []
for i in range(8):
    for j in range(8):
        eqns.append(P[i,j] - (1 if i==j else 0))

# Проверка линейной части по B,C около B=C=0
subs0 = {
b11:0,b12:0,b21:0,b22:0,
c11:0,c12:0,c21:0,c22:0,
a11:1,a12:0,a21:0,a22:1,
d11:1,d12:0,d21:0,d22:1
}

J = jacobian(eqns, [b11,b12,b21,b22,c11,c12,c21,c22])
J0 = J.subs(subs0)

print("rank wrt off-diagonal blocks =", J0.rank())
