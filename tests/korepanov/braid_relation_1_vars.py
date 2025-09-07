# This is trefoil on 2 strands

from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

z_1,z_2,z_3,z_4,z_5,z_6,z_7 = var("z_1,z_2,z_3,z_4,z_5,z_6,z_7")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)
assume(z_6 < z_7)

F = SR

P = sort_triangulation({z_1,z_2,z_7},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_1,z_5,z_6},{z_1,z_6,z_7},{z_2,z_3,z_4},{z_2,z_4,z_5},{z_2,z_5,z_6},{z_2,z_6,z_7})

t_ij, m_ij = braiding(P, (z_2,z_6),(z_1,z_7),(z_5,z_6), (z_2,z_4),(z_1,z_5),(z_5,z_7),(z_3,z_4), F=F)

t_ji, m_ji = braiding(P, (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4), (z_2,z_6),(z_1,z_7),(z_4,z_6), F=F)

assert t_ij == t_ji

# m_ij = m_ij.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

# print("Result matrix m_ij")
# show(m_ij)
print("Result matrix m_ij[3][2]")
show(m_ij[3][2])
print("Result matrix m_ij[4][2]")
show(m_ij[4][2])
print("Result matrix m_ij[3][3]")
show(m_ij[3][3])
print("Result matrix m_ij[4][3]")
show(m_ij[4][3])
print("Result matrix m_ij[6][7]")
show(m_ij[6][7])
print("Result matrix m_ij[7][7]")
show(m_ij[7][7])


print("")

# m_ji = m_ji.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

# print("Result matrix m_ji")
# show(m_ji)
#print("Result matrix m_ji[7][8]")
#show(m_ji[7][8])
print("Result matrix m_ji[3][2]")
show(m_ji[3][2])
print("Result matrix m_ji[4][2]")
show(m_ji[4][2])
print("Result matrix m_ji[3][3]")
show(m_ji[3][3])
print("Result matrix m_ji[4][3]")
show(m_ji[4][3])
print("Result matrix m_ji[6][7]")
show(m_ji[6][7])
print("Result matrix m_ji[7][7]")
show(m_ji[7][7])


print("###### simplify #########")
print(" simplify m_ij ")
# m_ij = m_ij.simplify_full()
m_ij = m_ij.simplify()
print(" simplify m_ji ")
# m_ji = m_ji.simplify_full()
m_ji = m_ji.simplify()

print("###################")
print("Result matrix m_ij[7][7]")
show(m_ij[7][7])
print("Result matrix m_ji[7][7]")
show(m_ji[7][7])

m_ij = m_ij.subs({z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5, z_6: 6, z_7: 7})
m_ji = m_ji.subs({z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5, z_6: 6, z_7: 7})

print("###################")
print("Result matrix m_ij[7][7]")
show(m_ij[7][7])
print("Result matrix m_ji[7][7]")
show(m_ji[7][7])

print("Equation satisfied: ", m_ij == m_ji)
