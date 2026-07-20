# В этом файле рассчитывается тривиальный узел с деформированной матрицей исчезновения второй точки минимума.
# ОЖИДАНИЕ: должен получиться инвариант относительно регулярной изотопии.
# РЕЗУЛЬТАТ: инвариантности относительно регулярной изотопии узла нет, т.к. два последовательных движения рейдемейстера не эквивалентны тривиальному узлу без этих движений,
#            получаемые значения зависят от значений переменных минимумов и максимумов.

from sage.all import *
from braids import braiding
from braids import knotting_max, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _show(*args):
  # show(latex(*args))
  show(*args)


PR = PolynomialRing(QQ, 'A')
PR.inject_variables()

F = PR.fraction_field()

# Deformation
d = -A**2 - A**(-2)
print("d:", d)

min_vars = [d, d, d]
# min_vars = [1, 1, 1]

z_1 = 1
z_2 = 2
z_3 = 3
z_4 = 4
z_5 = 5
z_6 = 6
z_7 = 7
z_8 = 8
z_9 = 9

T = sort_triangulation({z_1,z_2,z_3})

t, m_1 = knotting_max(T, {z_1,z_2,z_3}, z_4, F=F)
t, m_2 = knotting_max(t, {z_1,z_2,z_4}, z_5, F=F)

t, m_4 = knotting_min(t, z_5, F=F)
t, m_5 = knotting_min(t, z_4, vars=min_vars, F=F)

m = m_5 * m_4 * m_2 * m_1

assert T == t

bracket = m[0][0]

print("")
print("loop bracket:", bracket)
print("substituted loop bracket, A=1:", bracket.substitute({A: 1}))


########## Regular isotopy #################
t, m_1 = knotting_max(T, {z_1,z_2,z_3}, z_4, F=F)
t, m_2 = knotting_max(t, {z_1,z_2,z_4}, z_5, F=F)

t, m_3 = knotting_max(t, {z_1,z_2,z_5}, z_6, F=F)
t, m_4 = knotting_max(t, {z_1,z_2,z_6}, z_7, F=F)
t, m_b_1 = braiding(t,
                    (z_2,z_6),(z_1,z_5),(z_6,z_7),(z_4,z_5),
                    F=F)
t, m_5 = knotting_min(t, z_7, F=F)
t, m_6 = knotting_min(t, z_5, vars=min_vars, F=F)

t, m_7 = knotting_max(t, {z_1,z_2,z_6}, z_8, F=F)
t, m_8 = knotting_max(t, {z_1,z_2,z_8}, z_9, F=F)
t, m_b_2 = braiding(t,
                    (z_2,z_6),(z_1,z_8),(z_6,z_4),(z_8,z_9),
                    F=F)
t, m_9 = knotting_min(t, z_9, F=F)
t, m_10 = knotting_min(t, z_6, vars=min_vars, F=F)

t, m_11 = knotting_min(t, z_8, F=F)
t, m_12 = knotting_min(t, z_4, vars=min_vars, F=F)

m = m_12 * m_11 * m_10 * m_9 * m_b_2 * m_8 * m_7 * m_6 * m_5 * m_b_1 * m_4 * m_3 * m_2 * m_1

assert T == t

bracket = m[0][0]

print("")
print("isotoped loop bracket:", bracket)
print("substituted isotoped bracket, A=1:", bracket.substitute({A: 1}))



########## Regular isotopy with same points #################
t, m_1 = knotting_max(T, {z_1,z_2,z_3}, z_4, F=F)
t, m_2 = knotting_max(t, {z_1,z_2,z_4}, z_5, F=F)

t, m_3 = knotting_max(t, {z_1,z_2,z_5}, z_6, F=F)
t, m_4 = knotting_max(t, {z_1,z_2,z_6}, z_7, F=F)
t, m_b_1 = braiding(t,
                    (z_2,z_6),(z_1,z_5),(z_6,z_7),(z_4,z_5),
                    F=F)
t, m_5 = knotting_min(t, z_7, F=F)
t, m_6 = knotting_min(t, z_5, vars=min_vars, F=F)

t, m_7 = knotting_max(t, {z_1,z_2,z_6}, z_5, F=F)
t, m_8 = knotting_max(t, {z_1,z_2,z_5}, z_7, F=F)
t, m_b_2 = braiding(t,
                    (z_2,z_6),(z_1,z_5),(z_6,z_4),(z_5,z_7),
                    F=F)
t, m_9 = knotting_min(t, z_7, F=F)
t, m_10 = knotting_min(t, z_6, vars=min_vars, F=F)

t, m_11 = knotting_min(t, z_5, F=F)
t, m_12 = knotting_min(t, z_4, vars=min_vars, F=F)

m = m_12 * m_11 * m_10 * m_9 * m_b_2 * m_8 * m_7 * m_6 * m_5 * m_b_1 * m_4 * m_3 * m_2 * m_1

assert T == t

bracket = m[0][0]

print("")
print("isotoped loop bracket with same points:", bracket)
print("substituted isotoped bracket with same points, A=1:", bracket.substitute({A: 1}))
