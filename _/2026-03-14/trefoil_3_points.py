# В этом файле делаем трилистник на трех нитях и на 2х нитях со вторым движением маркова
# После этого решаем системы уравнений x=xA для обеих трилистников.
# Ожидание: системы линейных уравнений будут неопределенными, но их общие решения будут одинаковыми.

from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

z_1,z_2,z_3,z_4,z_5,z_6,z_7 = var("z_1,z_2,z_3,z_4,z_5,z_6,z_7")
x_1,x_2,x_3,x_4,x_5,x_6,x_7 = var("x_1,x_2,x_3,x_4,x_5,x_6,x_7")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)
assume(z_6 < z_7)

F = SR

T = sort_triangulation({z_1,z_2,z_6},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_1,z_5,z_6},{z_2,z_3,z_4},{z_2,z_4,z_5},{z_2,z_5,z_6})

# Трилисник на 2х нитях и одним вторым движением Маркова
print('Трилисник на 2х нитях и одним вторым движением Маркова')
t_1, m = braiding(T,
                (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4), (z_2,z_5),(z_1,z_4),(z_3,z_5),(z_4,z_6), (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4),
                (z_2,z_4),(z_1,z_6),(z_4,z_5),
                F=F)

#print("Result matrix")
#show(m)
print()
print('trace')
print(m.trace().simplify_full())


_x_ = matrix([[x_1,x_2,x_3,x_4,x_5,x_6,x_7]])

ax = _x_*m
#print()
#print('x*A:')
#show(ax)

eqs = [
  _x_[0][0] == ax[0][0],
  _x_[0][1] == ax[0][1],
  _x_[0][2] == ax[0][2],
  _x_[0][3] == ax[0][3],
  _x_[0][4] == ax[0][4],
  _x_[0][5] == ax[0][5],
  _x_[0][6] == ax[0][6],
]

result = solve(eqs, x_1,x_2,x_3,x_4,x_5,x_6,x_7)
print()
print('result')
print(result)


# Трилисник на 3х нитях
print()
print('Трилисник на 3х нитях')
t_2, m = braiding(T,
                (z_2,z_5),(z_1,z_6),(z_4,z_5),
                (z_2,z_4),(z_1,z_6),(z_1,z_5),(z_3,z_4),(z_4,z_6),
                (z_2,z_6),(z_1,z_5),(z_3,z_6),(z_4,z_5),
                F=F)

assert t_1 == t_2

#print("Result matrix")
#show(m)
print()
print('trace')
print(m.trace().simplify_full())

ax = _x_*m
#print()
#print('x*A:')
#show(ax)

eqs = [
  _x_[0][0] == ax[0][0],
  _x_[0][1] == ax[0][1],
  _x_[0][2] == ax[0][2],
  _x_[0][3] == ax[0][3],
  _x_[0][4] == ax[0][4],
  _x_[0][5] == ax[0][5],
  _x_[0][6] == ax[0][6],
]

result = solve(eqs, x_1,x_2,x_3,x_4,x_5,x_6,x_7)
print()
print('result')
print(result)
