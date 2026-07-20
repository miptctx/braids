# This is trefoil on 2 strands

from sage.all import *
from braids import braiding, knotting_max
from braids.utils import sort_triangulation

def _show(*args):
  # show(latex(*args))
  show(*args)

# z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")
z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

F = QQ
# F = SR

t_0 = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_4},{z_2,z_3,z_4})

t_1, m_1 = knotting_max(t_0, {z_1,z_3,z_4}, z_5, F=F)
t_2, m_2 = knotting_max(t_1, {z_1,z_3,z_5}, z_6, F=F)

t_l, m_3 = braiding(t_2, (z_1,z_5),(z_3,z_4),(z_1,z_4),(z_5,z_6), F=F)

m_l = m_3*m_2*m_1

print("Result matrix left crossing")
_show(m_l)
print("")


t_1, m_1 = knotting_max(t_0, {z_1,z_2,z_4}, z_5, F=F)
t_2, m_2 = knotting_max(t_1, {z_1,z_2,z_5}, z_6, F=F)

t_r, m_3 = braiding(t_2, (z_1,z_5),(z_2,z_4),(z_1,z_4),(z_5,z_6), F=F)

assert t_l == t_r

m_r = m_3*m_2*m_1

print("Result matrix right crossing")
_show(m_r)
print("")


print("Matrix equal:", m_l == m_r)
