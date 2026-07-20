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

subs_vars_val = {z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5}

F = SR

T = sort_triangulation({z_1,z_2,z_5},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_2,z_3,z_4},{z_2,z_4,z_5})

markov_direct_flips = ((z_1,z_4),(z_2,z_5),(z_3,z_4))
t_1, m_1 = braiding(T, *markov_direct_flips, F=F)

markov_inverse_flips = ((z_2,z_4),(z_1,z_5),(z_3,z_4))
t_2, m_2 = braiding(T, *markov_inverse_flips, F=F)

##############################################
########### Permute points 4 and 5 ###########
##############################################
origin = [z_4, z_5]
permut = [z_5, z_4]
T_p = permute_in_triangulations(T, origin, permut)
assert T_p == ({z_1,z_2,z_4},{z_1,z_3,z_5},{z_1,z_4,z_5},{z_2,z_3,z_5},{z_2,z_4,z_5})

flips_dir = permute_in_flips(markov_direct_flips, origin, permut)
print(flips_dir)
assert flips_dir == ({z_1,z_5},{z_2,z_4},{z_3,z_5})

flips_inv = permute_in_flips(markov_inverse_flips, origin, permut)
assert flips_inv == ({z_2,z_5},{z_1,z_4},{z_3,z_5})

t_3, m_3 = braiding(T_p, *flips_dir, F=F)
t_4, m_4 = braiding(T_p, *flips_inv, F=F)

##############################################
m_1_trace = m_1.trace()
m_2_trace = m_2.trace()
m_3_trace = m_3.trace()
m_4_trace = m_4.trace()

print("m_1 trace:", m_1_trace)
print("m_2 trace:", m_2_trace)
print("m_3 trace:", m_3_trace)
print("m_4 trace:", m_4_trace)

print()
print("m_1 trace:", m_1_trace.subs(subs_vars_val))
print("m_2 trace:", m_2_trace.subs(subs_vars_val))
print("m_3 trace:", m_3_trace.subs(subs_vars_val))
print("m_4 trace:", m_4_trace.subs(subs_vars_val))

print()
print("Expected identical trances")
print("m_1 + m_3 trace:", (m_1_trace + m_3_trace).subs(subs_vars_val))
print("m_2 + m_4 trace:", (m_2_trace + m_4_trace).subs(subs_vars_val))

print()
print("Just for test")
print("m_1 + m_2 trace:", (m_1_trace + m_2_trace).subs(subs_vars_val))
print("m_3 + m_4 trace:", (m_3_trace + m_4_trace).subs(subs_vars_val))

