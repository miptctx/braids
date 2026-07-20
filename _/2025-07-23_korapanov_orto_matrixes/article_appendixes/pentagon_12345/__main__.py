from sage.all import *
from braids.korepanov import braiding_ext as braiding
from braids.utils import sort_triangulation, rotate_tuple

z_1,z_2,z_3,z_4,z_5 = var("z_1,z_2,z_3,z_4,z_5")

F=SR

P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

assume(z_1 > 0)
assume(z_2 > z_1)
assume(z_3 > z_2)
assume(z_4 > z_3)
assume(z_5 > z_4)

t_l, m_l = braiding(P,
                    (rotate_tuple(z_1,z_2,z_3,z_4),{z_2,z_4}),
                    (rotate_tuple(z_1,z_3,z_4,z_5),{z_1,z_4}),
                    F=F)


t_r, m_r = braiding(P,
                    (rotate_tuple(z_1,z_2,z_4,z_5),{z_1,z_4}),
                    (rotate_tuple(z_2,z_3,z_4,z_5),{z_2,z_4}),
                    (rotate_tuple(z_1,z_2,z_3,z_5),{z_2,z_5}),
                    F=F)


lhs = m_l.subs({z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5})
rhs = m_r.subs({z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5})

lhs = lhs.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
rhs = rhs.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

print("LHS:")
print(lhs)

print("RHS:")
print(rhs)

print("LHS=RHS", lhs == rhs)
