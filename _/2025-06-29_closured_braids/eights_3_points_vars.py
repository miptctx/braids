# This is trefoil on 2 strands

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

'''
PR = PolynomialRing(QQ, 't_125,t_134,t_145,t_234,t_245')
PR.inject_variables()

F = PR.fraction_field()
'''

z_1,z_2,z_3,z_4,z_5,z_6,z_7 = var("z_1,z_2,z_3,z_4,z_5,z_6,z_7")

F = SR

T = sort_triangulation({z_1,z_2,z_6},{z_1,z_4,z_5},{z_1,z_3,z_4},{z_1,z_5,z_6},{z_2,z_3,z_4},{z_2,z_4,z_5},{z_2,z_5,z_6})

t, m = braiding(T,
                (z_2,z_5),(z_1,z_6),(z_4,z_5),(z_2,z_6),(z_1,z_4),(z_5,z_6),(z_3,z_4),
                (z_2,z_4),(z_1,z_5),(z_4,z_6),
                (z_2,z_5),(z_1,z_6),(z_4,z_5),(z_3,z_6),
                F=F)

print("Result matrix")
print_triangles_pretty(T)
print_triangles_pretty(t)
show(m)

eqs = [
  m[0][0] == 1,
  m[1][1] == 1,
  m[2][2] == 1,
  m[3][3] == 1,
  m[4][4] == 1,
  m[5][5] == 1,
  m[6][6] == 1,
]

print("Eqs")
show(eqs)

res = solve(eqs, z_1,z_2,z_3,z_4,z_5,z_6)
print("Result")
show(res)

res = m.transpose().solve_right(vector([1,1,1,1,1,1,1]))
show(res)

res_1 = res[0].simplify_full()
res_2 = res[1].simplify_full()
res_3 = res[2].simplify_full()
res_4 = res[3].simplify_full()
res_5 = res[4].simplify_full()
res_6 = res[5].simplify_full()

print("Result")
show(res_1)
show(res_2)
show(res_3)
show(res_4)
show(res_5)
show(res_6)
