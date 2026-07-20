# This is trefoil on 2 strands

from sage.all import *
from braids import braiding, knotting_min
from braids.utils import sort_triangulation

def _show(*args):
  # show(latex(*args))
  show(*args)

# z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")
z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

F = QQ
# F = SR

t_0 = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_6},{z_1,z_4,z_5},{z_1,z_5,z_6}, {z_2,z_3,z_4},{z_3,z_4,z_5},{z_3,z_5,z_6})

t_1, m_1 = braiding(t_0, (z_1,z_4),(z_3,z_5),(z_5,z_6),(z_2,z_4), F=F)

t_2, m_2 = knotting_min(t_1, z_6, F=F)
t_l, m_3 = knotting_min(t_2, z_4, F=F)

m_l = m_3*m_2*m_1

print("Result matrix left crossing")
_show(m_l)
print("")
#t_l, m_4 = knotting_min(t_l, z_5, F=F)
#_show(m_4*m_l)
#print("")

t_1, m_1 = braiding(t_0, (z_3,z_5),(z_1,z_6),(z_1,z_4),(z_5,z_4), F=F)

t_2, m_2 = knotting_min(t_1, z_4, F=F)
t_r, m_3 = knotting_min(t_2, z_6, F=F)

assert t_l == t_r

m_r = m_3*m_2*m_1

print("Result matrix right crossing")
_show(m_r)
print("")
#t_r, m_4 = knotting_min(t_r, z_5, F=F)
#_show(m_4*m_r)
#print("")


print("Matrix equal:", m_l == m_r)
