# В этом примере изем глобальные решения через какой-то PHCpack

from sage.all import *
from phcpy.solver import solve

# --- переменные ---
var('r11 r12 r13 r14 r21 r22 r23 r24 r31 r32 r33 r34 r41 r42 r43 r44')
var('s11 s12 s13 s14 s21 s22 s23 s24 s31 s32 s33 s34 s41 s42 s43 s44')

rvars = [r11,r12,r13,r14,
         r21,r22,r23,r24,
         r31,r32,r33,r34,
         r41,r42,r43,r44]

svars = [s11,s12,s13,s14,
         s21,s22,s23,s24,
         s31,s32,s33,s34,
         s41,s42,s43,s44]

vars = rvars + svars

# --- матрицы ---
R = matrix(4,4,rvars)
S = matrix(4,4,svars)

Id2 = identity_matrix(2)
Id4 = identity_matrix(4)
Id8 = identity_matrix(8)

# --- тензорные операторы ---
A1 = Id2.tensor_product(R)
A2 = S.tensor_product(Id2)
A3 = Id2.tensor_product(R)
A4 = S.tensor_product(Id2)
A5 = Id2.tensor_product(R)

P = A1*A2*A3*A4*A5

# --- уравнения ---
eqns = []

# (I⊗R)(S⊗I)(I⊗R)(S⊗I)(I⊗R) = I
for i in range(8):
    for j in range(8):
        eqns.append(P[i,j] - (1 if i==j else 0))

# RS = I
for i in range(4):
    for j in range(4):
        eqns.append((R*S)[i,j] - (1 if i==j else 0))
        eqns.append((S*R)[i,j] - (1 if i==j else 0))

# --- перевод в строки для phcpy ---
eqn_strings = [str(e) for e in eqns]
var_strings = [str(v) for v in vars]

print("number of equations:", len(eqn_strings))
print("number of variables:", len(var_strings))

# --- запуск ---
sols = solve(eqn_strings, var_strings, verbose=True)

print("number of solutions:", len(sols))
print(sols[:3])
