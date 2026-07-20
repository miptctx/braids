import sys

from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _round(val, pres=6):
  return val.apply_map(lambda x: round(x.real(), pres) + round(x.imag(), pres) * I)

def _round_val(val):
  x = CC(val)
  return round(x.real(), 6) + round(x.imag(), 6) * I


F = SR

z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)

# subs_vars_val = {z_1: QQ(1), z_2: QQ(2), z_3: QQ(3), z_4: QQ(4), z_5: QQ(5), z_6: QQ(6)}
# subs_vars_val = {z_1: QQ(11), z_2: QQ(2), z_3: QQ(31), z_4: QQ(40), z_5: QQ(515), z_6: QQ(16)}
subs_vars_val = {z_1: QQ(1)/2, z_2: QQ(2)/3, z_3: QQ(3)/1, z_4: QQ(4)/3, z_5: QQ(5)/5, z_6: QQ(6)/7}


T = sort_triangulation({z_1,z_3,z_4}, {z_1,z_5,z_6}, {z_1,z_2,z_6}, {z_1,z_4,z_5}, {z_2,z_3,z_4}, {z_2,z_4,z_5}, {z_2,z_5,z_6})
print_triangles_pretty(T)


##################################
##### trefoil on 3 strands #######
##################################
t, m_t = braiding(T,
                {z_2,z_5},{z_1,z_6},{z_2,z_4},{z_5,z_6},{z_3,z_4},
                {z_2,z_4},{z_1,z_5},{z_2,z_6},{z_5,z_4},{z_3,z_6},
                F=F)

m_t_int = m_t.subs(subs_vars_val)

print_triangles_pretty(t)

m_p = matrix([
  [1,0,0,0,0,0,0],
  [0,1,0,0,0,0,0],
  [0,0,0,1,0,0,0],
  [0,0,1,0,0,0,0],
  [0,0,0,0,1,0,0],
  [0,0,0,0,0,0,1],
  [0,0,0,0,0,1,0]
])

m_t = m_t*m_p    # согласование базиса

################################
##### Conjugated trefoil #######
################################

t_top, m_top = braiding(T, {z_2,z_5},{z_1,z_4},{z_5,z_6},{z_3,z_4}, F=F)
t_bot, m_bot = braiding(T, {z_2,z_4},{z_1,z_5},{z_5,z_6},{z_3,z_4}, F=F)
assert t_top == t_bot

print_triangles_pretty(t_top)

m = m_bot.subs({z_4:z_5, z_5:z_6, z_6:z_4})*m_t
m_t_conj = m.subs({z_4:z_5, z_5:z_4})*m_top

#####################################
##### Check conjugated braids #######
#####################################

print()
print("#### Check ####")
m_check = m_bot.subs({z_4:z_5, z_5:z_4})*m_top
m_check = m_check.simplify_full()
show(m_check)

#############################################
##### Make permutations and calculate #######
#############################################

print()
print("permute and substitute variables to matrixes...")
permutations = []
trefoil_matrixes = []
trefoil_matrixes_conj = []
for x_4, x_5, x_6 in Permutations([z_4, z_5, z_6]):
  permutations.append((x_4, x_5, x_6))
  z_subs = {z_4:x_4, z_5:x_5, z_6:x_6}
  trefoil_matrixes.append(Matrix(QQ, m_t.subs(z_subs).subs(subs_vars_val)))
  trefoil_matrixes_conj.append(Matrix(QQ, m_t_conj.subs(z_subs).subs(subs_vars_val)))


A_diag = block_diagonal_matrix(trefoil_matrixes)
A_diag_conj = block_diagonal_matrix(trefoil_matrixes_conj)


print()
print("find eigen matrix of trefoil matrix")
a_eig, a_vect = A_diag.eigenmatrix_right()

print()
print("find eigen matrix of conjugated trefoil matrix")
a_eig_conj, a_vect_conj = A_diag_conj.eigenmatrix_right()

a_eig = _round(a_eig)
a_vect = _round(a_vect)

a_eig_conj = _round(a_eig_conj)
a_vect_conj = _round(a_vect_conj)

#print("eigen values of trefoil")
#print(a_eig)
#print("eigen values of trefoil cojugated")
#print(a_eig_conj)
#print("eigen vectors of trefoil")
#print(a_vect)
#print("eigen vectors of trefoil conjugated")
#print(a_vect_conj)

print()
print("total eigenvalues", a_eig.nrows())

print()
print("det trefoil:", A_diag.det())
print("trace trefoil:", A_diag.trace())
# print("charpoly trefoil:", A_diag.charpoly())

print()
print("det trefoil conj:", A_diag_conj.det())
print("trace trefoil conj:", A_diag_conj.trace())
# print("charpoly trefoil conj:", A_diag_conj.charpoly())

print()
print("search unique eigenvalues")
a_uniq_vals = set([a_eig[i,i] for i in range(a_eig.nrows())])
a_uniq_vals_conj = set([a_eig_conj[i,i] for i in range(a_eig_conj.nrows())])
uniq_values = a_uniq_vals & a_uniq_vals_conj
print("unique values count:", len(uniq_values), ", they are:", uniq_values)


exit()
print()
print("trefoil eigen vectors")
print(_round(a_vect, pres=2))
print("conjugated trefoil eigen vectors")
print(_round(a_vect_conj, pres=2))
