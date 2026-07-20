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

subs_vars_val = {z_1: QQ(1), z_2: QQ(2), z_3: QQ(3), z_4: QQ(4), z_5: QQ(5), z_6: QQ(6)}
# subs_vars_val = {z_1: QQ(11), z_2: QQ(2), z_3: QQ(31), z_4: QQ(40), z_5: QQ(515), z_6: QQ(16)}
# subs_vars_val = {z_1: QQ(1)/2, z_2: QQ(2)/3, z_3: QQ(3)/1, z_4: QQ(4)/3, z_5: QQ(5)/5, z_6: QQ(6)/7}


T = sort_triangulation({z_1,z_3,z_4}, {z_1,z_5,z_6}, {z_1,z_2,z_6}, {z_1,z_4,z_5}, {z_2,z_3,z_4}, {z_2,z_4,z_5}, {z_2,z_5,z_6})
print_triangles_pretty(T)

##################################
######## Считаем сигмы ###########
##################################
t_sigma_1, m_sigma_1 = braiding(T, (z_2,z_5),(z_1,z_6),(z_4,z_5), F=F)
print_triangles_pretty(t_sigma_1)

t_sigma_1_inv, m_sigma_1_inv = braiding(T, (z_1,z_5),(z_2,z_6),(z_4,z_5), F=F)

t_sigma_2, m_sigma_2 = braiding(T, (z_1,z_5),(z_2,z_4),(z_5,z_6),(z_3,z_4), F=F)
print_triangles_pretty(t_sigma_2)

t_sigma_2_inv, m_sigma_2_inv = braiding(T, (z_2,z_5),(z_1,z_4),(z_5,z_6),(z_3,z_4), F=F)

print("### sigmas ###")
show(latex(m_sigma_2))
print()
show(latex(m_sigma_2.subs({z_5: z_6, z_6: z_5})))

##################################
##### trefoil on 3 strands #######
##################################

# σ1σ2σ1σ2

m_trefoil_1 = m_sigma_1
m_trefoil_2 = m_sigma_2.subs({z_4:z_4, z_5:z_6, z_6:z_5})
m_trefoil_3 = m_sigma_1.subs({z_4:z_6, z_5:z_4, z_6:z_5})
m_trefoil_4 = m_sigma_2.subs({z_4:z_6, z_5:z_5, z_6:z_4}) # final dots order is 564

m_trefoil = m_trefoil_4 * m_trefoil_3 * m_trefoil_2 * m_trefoil_1

#############################################
##### trefoil conjugated on 3 strands #######
#############################################

# σ2^(-1)σ1σ2σ1σ2σ2

m_trefoil_conj_1 = m_sigma_2_inv
m_trefoil_conj_2 = m_sigma_1.subs({z_4:z_5, z_5:z_4, z_6:z_6})
m_trefoil_conj_3 = m_sigma_2.subs({z_4:z_5, z_5:z_6, z_6:z_4})
m_trefoil_conj_4 = m_sigma_1.subs({z_4:z_6, z_5:z_5, z_6:z_4})
m_trefoil_conj_5 = m_sigma_2.subs({z_4:z_6, z_5:z_4, z_6:z_5})
m_trefoil_conj_6 = m_sigma_2.subs({z_4:z_4, z_5:z_6, z_6:z_5}) # final dots order is 645

m_trefoil_conj = m_trefoil_conj_6 * m_trefoil_conj_5 * m_trefoil_conj_4 * m_trefoil_conj_3 * m_trefoil_conj_2 * m_trefoil_conj_1


##################################
###### eight on 3 strands ########
##################################

# σ1σ2^(-1)σ1σ2^(-1)

m_eight_1 = m_sigma_1
m_eight_2 = m_sigma_2_inv.subs({z_4:z_4, z_5:z_6, z_6:z_5})
m_eight_3 = m_sigma_1.subs({z_4:z_6, z_5:z_4, z_6:z_5})
m_eight_4 = m_sigma_2_inv.subs({z_4:z_6, z_5:z_5, z_6:z_4}) # final dots order is 564

m_eight = m_eight_4 * m_eight_3 * m_eight_2 * m_eight_1


####################################
###### trivial on 3 strands ########
####################################

# σ1σ2

m_triv_1 = m_sigma_1
m_triv_2 = m_sigma_2.subs({z_4:z_4, z_5:z_6, z_6:z_5}) # final dots order is 645

m_triv = m_triv_2*m_triv_1

####################################
###### trivial on 3 strands ########
####################################

# σ1σ2^(-1)

m_triv_1_2 = m_sigma_1
m_triv_2_2 = m_sigma_2_inv.subs({z_4:z_4, z_5:z_6, z_6:z_5}) # final dots order is 645

m_triv2 = m_triv_2_2*m_triv_1_2

#############################################
##### Make permutations and calculate #######
#############################################

assert m_trefoil != m_trefoil_conj and m_trefoil != m_eight and m_trefoil != m_triv and m_trefoil != m_triv2
assert m_trefoil_conj != m_eight and m_trefoil_conj != m_triv and m_trefoil_conj != m_triv2
assert m_eight != m_triv and m_eight != m_triv2
assert m_triv != m_triv2

print()
print("permute and substitute variables to matrixes...")
permutations = []
trefoil_matrixes = []
trefoil_matrixes_conj = []
eight_matrixes = []
trivial_matrixes = []
trivial2_matrixes = []
for x_4, x_5, x_6 in Permutations([z_4, z_5, z_6]):
  permutations.append((x_4, x_5, x_6))
  z_subs = {z_4:x_4, z_5:x_5, z_6:x_6}
  trefoil_matrixes.append(Matrix(QQ, m_trefoil.subs(z_subs).subs(subs_vars_val)))
  trefoil_matrixes_conj.append(Matrix(QQ, m_trefoil_conj.subs(z_subs).subs(subs_vars_val)))
  eight_matrixes.append(Matrix(QQ, m_eight.subs(z_subs).subs(subs_vars_val)))
  trivial_matrixes.append(Matrix(QQ, m_triv.subs(z_subs).subs(subs_vars_val)))
  trivial2_matrixes.append(Matrix(QQ, m_triv2.subs(z_subs).subs(subs_vars_val)))


M_trefoil      = block_diagonal_matrix(trefoil_matrixes)
M_trefoil_conj = block_diagonal_matrix(trefoil_matrixes_conj)
M_eight        = block_diagonal_matrix(eight_matrixes)
M_triv         = block_diagonal_matrix(trivial_matrixes)
M_triv2        = block_diagonal_matrix(trivial2_matrixes)

assert M_trefoil != M_trefoil_conj and M_trefoil != M_eight and M_trefoil != M_triv and M_trefoil != M_triv2
assert M_trefoil_conj != M_eight and M_trefoil_conj != M_triv and M_trefoil_conj != M_triv2
assert M_eight != M_triv and M_eight != M_triv2
assert M_triv != M_triv2


print()
print("find eigen matrix of trefoil matrix")
trefoil_eig, trefoil_vect = M_trefoil.eigenmatrix_right()

print()
print("find eigen matrix of conjugated trefoil matrix")
trefoil_conj_eig, trefoil_conj_vect = M_trefoil_conj.eigenmatrix_right()

print()
print("find eigen matrix of eight matrix")
eight_eig, eight_vect = M_eight.eigenmatrix_right()

print()
print("find eigen matrix of trivial matrix")
triv_eig, triv_vect = M_triv.eigenmatrix_right()

print()
print("find eigen matrix of trivial matrix")
triv2_eig, triv2_vect = M_triv2.eigenmatrix_right()


trefoil_eig = _round(trefoil_eig)
trefoil_vect = _round(trefoil_vect)

trefoil_conj_eig = _round(trefoil_conj_eig)
trefoil_conj_vect = _round(trefoil_conj_vect)

eight_eig = _round(eight_eig)
eight_vect = _round(eight_vect)

triv_eig = _round(triv_eig)
triv_vect = _round(triv_vect)

triv2_eig = _round(triv2_eig)
triv2_vect = _round(triv2_vect)

assert trefoil_eig != trefoil_conj_eig and trefoil_eig != eight_eig and trefoil_eig != triv_eig and trefoil_eig != triv2_eig
assert trefoil_conj_eig != eight_eig and trefoil_conj_eig != triv_eig and trefoil_conj_eig != triv2_eig
assert eight_eig != triv_eig and eight_eig != triv2_eig
assert triv_eig != triv2_eig

print()
print("total eigenvalues of trefoil", trefoil_eig.nrows())
print("total eigenvalues of conjugacy trefoil", trefoil_conj_eig.nrows())
print("total eigenvalues of eight", eight_eig.nrows())
print("total eigenvalues of trivial", triv_eig.nrows())

print()
print("det trefoil:", M_trefoil.det())
print("trace trefoil:", M_trefoil.trace())

print()
print("det trefoil conj:", M_trefoil_conj.det())
print("trace trefoil conj:", M_trefoil_conj.trace())

print()
print("det eight:", M_eight.det())
print("trace eight:", M_eight.trace())

print()
print("det trivial:", M_triv.det())
print("trace trivial:", M_triv.trace())

print()
print("det trivial2:", M_triv2.det())
print("trace trivial2:", M_triv2.trace())

print()
print("is charpoly of the trefoil and eight same:", M_trefoil.charpoly() == M_eight.charpoly())

print()
print("search unique eigenvalues")
trefoil_uniq_vals = set([trefoil_eig[i,i] for i in range(trefoil_eig.nrows())])
trefoil_conj_uniq_vals = set([trefoil_conj_eig[i,i] for i in range(trefoil_conj_eig.nrows())])
eight_uniq_vals = set([eight_eig[i,i] for i in range(eight_eig.nrows())])
triv_uniq_vals = set([triv_eig[i,i] for i in range(triv_eig.nrows())])
triv2_uniq_vals = set([triv2_eig[i,i] for i in range(triv2_eig.nrows())])

uniq_values = trefoil_conj_uniq_vals & trefoil_uniq_vals
print("unique values count of trefoils:", len(uniq_values), ", they are:", uniq_values)

uniq_values = trefoil_uniq_vals & eight_uniq_vals
print("unique values count of trefoil and eight:", len(uniq_values), ", they are:", uniq_values)

uniq_values = trefoil_conj_uniq_vals & eight_uniq_vals
print("unique values count of conjugated trefoil and eight:", len(uniq_values), ", they are:", uniq_values)

uniq_values = trefoil_conj_uniq_vals & triv_uniq_vals
print("unique values count of conjugated trefoil and trivial:", len(uniq_values), ", they are:", uniq_values)

uniq_values = trefoil_conj_uniq_vals & triv2_uniq_vals
print("unique values count of conjugated trefoil and trivial2:", len(uniq_values), ", they are:", uniq_values)
