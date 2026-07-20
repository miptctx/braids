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

# Трилистник на двух нитях и одним движеним Маркова
is_mv_flips = (
  (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4), (z_2,z_5),(z_1,z_4),(z_3,z_5),(z_4,z_6), (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4),
  (z_2,z_4),(z_1,z_6),(z_4,z_5)
)

# Трилистник на трех нитях
no_mv_flips = (
  (z_2,z_5),(z_1,z_6),(z_4,z_5),
  (z_2,z_4),(z_1,z_6),(z_1,z_5),(z_3,z_4),(z_4,z_6),
  (z_2,z_6),(z_1,z_5),(z_3,z_6),(z_4,z_5)
)

##############################################
######### Permute 4, 5 and 6 points ##########
##############################################
origin = [z_4, z_5, z_6]
matrices_is_mv = []
matrices_no_mv = []
for permut in Permutations(origin):
  print("permutation:", permut)
  T_p = permute_in_triangulations(T, origin, permut)
  flips_is = permute_in_flips(is_mv_flips, origin, permut)
  flips_no = permute_in_flips(no_mv_flips, origin, permut)
  t_is, m_is = braiding(T_p, *flips_is, F=F)
  t_no, m_no = braiding(T_p, *flips_no, F=F)
  matrices_is_mv.append(m_is)
  matrices_no_mv.append(m_no)


traces_is = [m.trace() for m in matrices_is_mv]
traces_no = [m.trace() for m in matrices_no_mv]

print()
traces_is_int = [t.subs(subs_vars_val) for t in traces_is]
traces_no_int = [t.subs(subs_vars_val) for t in traces_no]
print('traces is:', traces_is_int)
print('traces no:', traces_no_int)

print()
print("traces is sum:", sum(traces_is_int))
print("traces no sum:", sum(traces_no_int))

###############################################
############### Определитель ##################
###############################################
m_is_int = [m.subs(subs_vars_val) for m in matrices_is_mv]
m_no_int = [m.subs(subs_vars_val) for m in matrices_no_mv]

dets_is = [m.det() for m in m_is_int]
dets_no = [m.det() for m in m_no_int]

print()
print("dets is:", dets_is)
print("dets no:", dets_no)

det_is = prod(dets_is)
det_no = prod(dets_no)

print()
print("det is:", det_is)
print("det no:", det_no)


###############################################
############### Хар. могоч. ###################
###############################################
m_is_int = [m.subs(subs_vars_val) for m in matrices_is_mv]
m_no_int = [m.subs(subs_vars_val) for m in matrices_no_mv]

chars_is = [m.charpoly() for m in m_is_int]
chars_no = [m.charpoly() for m in m_no_int]

print()
print("chars dir:", chars_is)
print("chars inv:", chars_no)

m_total_is = block_diagonal_matrix(m_is_int)
m_total_no = block_diagonal_matrix(m_no_int)
#print()
#print("total is:", m_total_is)
#print("total no:", m_total_no)
print()
print("total trace is:", m_total_is.trace())
print("total trace no:", m_total_no.trace())
print()
print("total charpoly is:", m_total_is.charpoly())
print("total charpoly no:", m_total_no.charpoly())

