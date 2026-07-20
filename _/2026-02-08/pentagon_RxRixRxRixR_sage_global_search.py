# В этом примере делается глобальный численный поиск в Sage
# Для уравнения (I⊗R)(R^-1⊗I)(I⊗R)(R^-1⊗I)(I⊗R)=I


from sage.all import *
import random

# --- переменные ---
var('x_11 x_12 x_13 x_14')
var('x_21 x_22 x_23 x_24')
var('x_31 x_32 x_33 x_34')
var('x_41 x_42 x_43 x_44')

vars = [x_11,x_12,x_13,x_14,
        x_21,x_22,x_23,x_24,
        x_31,x_32,x_33,x_34,
        x_41,x_42,x_43,x_44]

# --- матрица R ---
R = matrix(4,4,vars)

Id2 = identity_matrix(2)
Id8 = identity_matrix(8)

# --- система ---
P = (Id2.tensor_product(R) *
     R.inverse().tensor_product(Id2) *
     Id2.tensor_product(R) *
     R.inverse().tensor_product(Id2) *
     Id2.tensor_product(R))

eqns = []
for i in range(8):
    for j in range(8):
        eqns.append(P[i,j] - (1 if i==j else 0))

# --- попытки ---
def try_random():
    start = [complex(random.uniform(-2,2), random.uniform(-2,2)) for _ in vars]
    try:
        sol = find_root(eqns, vars, start)
        return sol
    except:
        return None

# --- многократный запуск ---
sols = []
for k in range(30):
    s = try_random()
    if s is not None:
        print("FOUND:", s)
        sols.append(s)

print("total found:", len(sols))
