# Этот файл нужен для тестирования корректности работы функций перестановки

from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty
from utils import *

z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)

subs_vars_val = {z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5, z_6: 6}

F = SR

T = sort_triangulation({z_1,z_2,z_6},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_1,z_5,z_6},{z_2,z_3,z_4},{z_2,z_4,z_5},{z_2,z_5,z_6})

markov_direct_flips = (
  (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4), (z_2,z_5),(z_1,z_4),(z_3,z_5),(z_4,z_6), (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4),
  (z_2,z_4),(z_1,z_6),(z_4,z_5)
)

markov_inverse_flips = (
  (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4), (z_2,z_5),(z_1,z_4),(z_3,z_5),(z_4,z_6), (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4),
  (z_1,z_4),(z_2,z_6),(z_4,z_5)
)

##############################################
######### Permute 4, 5 and 6 points ##########
##############################################
origin = [z_4, z_5, z_6]
matrices_mov_dir = []
matrices_mov_inv = []
for permut in Permutations(origin):
  print("permutation:", permut)
  T_p = permute_in_triangulations(T, origin, permut)
  flips_dir = permute_in_flips(markov_direct_flips, origin, permut)
  flips_inv = permute_in_flips(markov_inverse_flips, origin, permut)
  t_dir, m_dir = braiding(T_p, *flips_dir, F=F)
  t_inv, m_inv = braiding(T_p, *flips_inv, F=F)
  matrices_mov_dir.append(m_dir)
  matrices_mov_inv.append(m_inv)


traces_dir = [m.trace() for m in matrices_mov_dir]
traces_inv = [m.trace() for m in matrices_mov_inv]

print()
traces_dir_int = [t.subs(subs_vars_val) for t in traces_dir]
traces_inv_int = [t.subs(subs_vars_val) for t in traces_inv]
print('traces dir:', traces_dir_int)
print('traces inv:', traces_inv_int)

print()
print("traces dir sum:", sum(traces_dir_int))
print("traces inv sum:", sum(traces_inv_int))

###############################################
############### Определитель ##################
###############################################
m_dir_int = [m.subs(subs_vars_val) for m in matrices_mov_dir]
m_inv_int = [m.subs(subs_vars_val) for m in matrices_mov_inv]

dets_dir = [m.det() for m in m_dir_int]
dets_inv = [m.det() for m in m_inv_int]

print()
print("dets dir:", dets_dir)
print("dets inv:", dets_inv)

det_dir = prod(dets_dir)
det_inv = prod(dets_inv)

print()
print("det dir:", det_dir)
print("det inv:", det_inv)


###############################################
############### Хар. могоч. ###################
###############################################
m_dir_int = [m.subs(subs_vars_val) for m in matrices_mov_dir]
m_inv_int = [m.subs(subs_vars_val) for m in matrices_mov_inv]

chars_dir = [m.charpoly() for m in m_dir_int]
chars_inv = [m.charpoly() for m in m_inv_int]

print()
print("chars dir:", chars_dir)
print("chars inv:", chars_inv)

