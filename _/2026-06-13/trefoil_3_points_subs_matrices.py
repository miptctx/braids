# В этом файле делаем трилистник на трех нитях и на 2х нитях со вторым движением маркова.
# Находим матрицу для одной перестановки точек, а остальные получаем перестановкой переменных в ней.
# Получаем сумму следов полученных матриц.
# Ожидание: следы матриц должны быть одинаковыми.

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

subs_vars_val = {z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5, z_6: 6}

F = SR

T = sort_triangulation({z_1,z_2,z_6},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_1,z_5,z_6},{z_2,z_3,z_4},{z_2,z_4,z_5},{z_2,z_5,z_6})

# Трилисник на 2х нитях и одним вторым движением Маркова
print('Трилисник на 2х нитях и одним вторым движением Маркова')
flips = ((z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4), (z_2,z_5),(z_1,z_4),(z_3,z_5),(z_4,z_6), (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4),
         (z_2,z_4),(z_1,z_6),(z_4,z_5))
t_1, m = braiding(T, *flips, F=F)


matrices = []
for z_new_4, z_new_5, z_new_6 in Permutations([z_4, z_5, z_6]):
  print(f"permutation:", z_new_4, z_new_5, z_new_6)
  origin = [z_4, z_5, z_6]
  permut = [z_new_4, z_new_5, z_new_6]
  subs = dict(zip(origin, permut))
  m_t = m.subs(subs)
  matrices.append(m_t)


for i in range(len(matrices)):
  # matrices[i] = matrices[i].simplify_full()
  print("trace:", matrices[i].trace().subs(subs_vars_val))

print()
trace_1 = sum([m.trace() for m in matrices])
#print('common trace:', trace_1)
#print('common trace simplified:', trace_1.simplify_full())


# Трилисник на 3х нитях
print()
print('Трилисник на 3х нитях')
flips = ((z_2,z_5),(z_1,z_6),(z_4,z_5),
        (z_2,z_4),(z_1,z_6),(z_1,z_5),(z_3,z_4),(z_4,z_6),
        (z_2,z_6),(z_1,z_5),(z_3,z_6),(z_4,z_5))
t_2, m = braiding(T, *flips, F=F)

matrices = []
for z_new_4, z_new_5, z_new_6 in Permutations([z_4, z_5, z_6]):
  print(f"permutation:", z_new_4, z_new_5, z_new_6)
  origin = [z_4, z_5, z_6]
  permut = [z_new_4, z_new_5, z_new_6]
  subs = dict(zip(origin, permut))
  m_t = m.subs(subs)
  matrices.append(m_t)

for i in range(len(matrices)):
  # matrices[i] = matrices[i].simplify_full()
  print("trace:", matrices[i].trace().subs(subs_vars_val))

print()
trace_2 = sum([m.trace() for m in matrices])
#print('common trace:', trace_2)
#print('common trace simplified:', trace_2.simplify_full())


print()
print("compare traces")
trace_1 = trace_1.subs(subs_vars_val)
print("trace 1:", trace_1)
trace_2 = trace_2.subs(subs_vars_val)
print("trace 2:", trace_2)
print("trace 1 == trace 2:", trace_1 == trace_2)
