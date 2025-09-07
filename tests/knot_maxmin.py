from sage.all import *
from braids import knotting_max, knotting_min
from braids.utils import sort_triangulation


PR = PolynomialRing(QQ, 'z_5,z_4,z_3,z_2,z_1')
PR.inject_variables()

F = PR.fraction_field()

t_0 = sort_triangulation({z_1,z_2,z_3})

t_1, m_1 = knotting_max(t_0, {z_1,z_2,z_3}, z_4, F=F)
t_2, m_2 = knotting_max(t_1, {z_2,z_3,z_4}, z_5, F=F)

t_3, m_3 = knotting_min(t_2, z_5, F=F)
t_4, m_4 = knotting_min(t_3, z_4, F=F)

assert t_0 == t_4

m = m_4*m_3*m_2*m_1

show(m)
