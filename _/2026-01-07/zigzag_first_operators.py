# В этом файле я хотел проверить движение Тураева и I движением Рейдемейстера в самых первых операторах.
# Но перепутал и забыл, что надо делать перекресток с точкой 4, а не флипы между точками 5 и 6.
# В итоге делал флипы между точками 5 и 6 и получил единичные матрицы, как и положено.


from sage.all import *
from braids import braiding, knotting_max, knotting_min
from braids.utils import sort_triangulation

def _show(*args):
  # show(latex(*args))
  show(*args)

#var("z_1,z_2,z_3,z_4,z_5,z_6")
#assume(z_1 < z_2)
#assume(z_2 < z_3)
#assume(z_3 < z_4)
#assume(z_4 < z_5)
#assume(z_5 < z_6)

z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

F = QQ
# F = SR

t_0 = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_4},{z_2,z_3,z_4})

t_1, m_1 = knotting_max(t_0, {z_1,z_3,z_4}, z_5, F=F)
t_2, m_2 = knotting_max(t_1, {z_1,z_4,z_5}, z_6, F=F)
t_b, m_b = braiding(t_2, {z_4,z_5}, {z_1,z_6}, {z_3,z_5}, F=F)
t_3, m_3 = knotting_min(t_b, z_5, F=F)
t_4, m_4 = knotting_min(t_3, z_6, F=F)

print("")
print("m_1")
show(m_1)

print("")
print("m_2")
show(m_2)

print("")
print("m_b")
show(m_b)

print("")
print("m_3")
show(m_3)

print("")
print("m_4")
show(m_4)

m = m_4*m_3*m_b*m_2*m_1

print("")
print("Result")
# _show(m.simplify_full())
_show(m)
