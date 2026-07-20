from sage.all import *

a,b,c,d = var('a,b,c,d')

p = matrix([[a,b], [c,d]])
q = p.inverse()

#print(q)

qa = q[0][0]
qb = q[0][1]
qc = q[1][0]
qd = q[1][1]

_l_1 = matrix([[a,0,b],[c,0,d],[0,1,0]])
print('l_1^(-1)')
print(_l_1.inverse())
print("")

print("_l_1*l_1=")
print((_l_1.inverse()*_l_1).simplify_full())
print("")

l_1 = matrix([[qa,0,qb],[qc,0,qd],[0,1,0]])
print('l_1')
print(l_1)
print("")

l_2 = matrix([[1,0,0],[0,a,b],[0,c,d]])
print('l_2')
print(l_2)
print("")

r_1 = matrix([[a,b,0],[0,0,1],[c,d,0]])
print('r_1')
print(r_1)
print("")

r_2 = matrix([[1,0,0],[0,a,b],[0,c,d]])
print('r_2')
print(r_2)
print("")

r_3 = matrix([[qa,qb,0],[qb,qc,0],[0,0,1]])
print('r_3')
print(r_3)
print("")

lhs = l_2*l_1
rhs = r_3*r_2*r_1

print("lhs")
print(lhs)
print("")
print("rhs")
print(rhs)

eqs = [
  lhs[0][0] == rhs[0][0],
  lhs[0][1] == rhs[0][1],
  lhs[0][2] == rhs[0][2],
  lhs[1][0] == rhs[1][0],
  lhs[1][1] == rhs[1][1],
  lhs[1][2] == rhs[1][2],
  lhs[2][0] == rhs[2][0],
  lhs[2][1] == rhs[2][1],
  lhs[2][2] == rhs[2][2]
]

result = solve(eqs, a,b,c,d)

print("result")
print(result)
