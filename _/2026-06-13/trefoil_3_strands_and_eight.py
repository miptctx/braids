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

# Трилистник на трех нитях
trefoil_flips = (
  (z_2,z_5),(z_1,z_6),(z_4,z_5),
  (z_2,z_4),(z_1,z_6),(z_1,z_5),(z_3,z_4),(z_4,z_6),
  (z_2,z_6),(z_1,z_5),(z_3,z_6),(z_4,z_5)
)

# Восьмерка на трех нитях
eight_flips = (
  (z_2,z_5),(z_1,z_6),(z_4,z_5),
  (z_2,z_6),(z_1,z_4),(z_3,z_4),(z_5,z_6),
  (z_2,z_4),(z_1,z_5),(z_4,z_6),
  (z_2,z_6),(z_1,z_5),(z_3,z_6),(z_4,z_5)
)


##############################################
######### Permute 4, 5 and 6 points ##########
##############################################
origin = [z_4, z_5, z_6]
matrices_tr = []
matrices_ei = []
for permut in Permutations(origin):
  print("permutation:", permut)
  T_p = permute_in_triangulations(T, origin, permut)
  flips_tr = permute_in_flips(trefoil_flips, origin, permut)
  flips_ei = permute_in_flips(eight_flips, origin, permut)
  t_tr, m_tr = braiding(T_p, *flips_tr, F=F)
  t_ei, m_ei = braiding(T_p, *flips_ei, F=F)
  assert t_tr == t_ei
  matrices_tr.append(m_tr)
  matrices_ei.append(m_ei)


traces_tr = [m.trace() for m in matrices_tr]
traces_ei = [m.trace() for m in matrices_ei]

print()
traces_tr_int = [t.subs(subs_vars_val) for t in traces_tr]
traces_ei_int = [t.subs(subs_vars_val) for t in traces_ei]
print('traces tref:', traces_tr_int)
print('traces eight:', traces_ei_int)

print()
print("traces tref sum:", sum(traces_tr_int))
print("traces eigh sum:", sum(traces_ei_int))

###############################################
############### Определитель ##################
###############################################
m_tr_int = [m.subs(subs_vars_val) for m in matrices_tr]
m_ei_int = [m.subs(subs_vars_val) for m in matrices_ei]

dets_tr = [m.det() for m in m_tr_int]
dets_ei = [m.det() for m in m_ei_int]

print()
print("dets tref:", dets_tr)
print("dets eigh:", dets_ei)

det_tr = prod(dets_tr)
det_ei = prod(dets_ei)

print()
print("det tref:", det_tr)
print("det eigh:", det_ei)


###############################################
############### Хар. могоч. ###################
###############################################
m_tr_int = [m.subs(subs_vars_val) for m in matrices_tr]
m_ei_int = [m.subs(subs_vars_val) for m in matrices_ei]

chars_tr = [m.charpoly() for m in m_tr_int]
chars_ei = [m.charpoly() for m in m_ei_int]

print()
print("chars tref:", chars_tr)
print("chars eigh:", chars_ei)

