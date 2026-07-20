from sage.all import *

a,b,c,d = var('a,b,c,d')

p = matrix([[a,b], [c,d]])
q = p.inverse()

print("q")
print(q)
print("")

qa = q[0][0]
qb = q[0][1]
qc = q[1][0]
qd = q[1][1]

m_0 = matrix([[a,0,b],[c,0,d],[0,1,0]])
print("m_0")
print(m_0)
print("")

m_1 = m_0.inverse()
print("m_1")
print(m_1)
print("")

m_q = matrix([[qa,0,qb],[qc,0,qd],[0,1,0]])
print("m_q")
print(m_q)
print("")

'''
m_2 = m_0*m_1
print("m_2")
print(m_2)
print("")
'''

eqs = [
  m_1[0][0] == m_q[0][0],
  m_1[0][1] == m_q[0][1],
  m_1[0][2] == m_q[0][2],
  m_1[1][0] == m_q[1][0],
  m_1[1][1] == m_q[1][1],
  m_1[1][2] == m_q[1][2],
  m_1[2][0] == m_q[2][0],
  m_1[2][1] == m_q[2][1],
  m_1[2][2] == m_q[2][2]
]

result = solve(eqs, a,b,c,d)
print(result)
