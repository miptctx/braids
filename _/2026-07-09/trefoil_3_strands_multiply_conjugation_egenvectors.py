import sys

from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _round(val):
  return val.apply_map(lambda x: round(x.real(), 6) + round(x.imag(), 6) * I)

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
#for x_1, x_2, x_3, x_4, x_5, x_6 in Permutations(subs_vars_val.keys()):
#  permutations.append((x_1, x_2, x_3, x_4, x_5, x_6))
#  z_subs = {z_1:x_1, z_2:x_2, z_3:x_3, z_4:x_4, z_5:x_5, z_6:x_6}
#  trefoil_matrixes.append(m_t.subs(z_subs).subs(subs_vars_val))
#  trefoil_matrixes_conj.append(m_t_conj.subs(z_subs).subs(subs_vars_val))
for x_4, x_5, x_6 in Permutations([z_4, z_5, z_6]):
  permutations.append((x_4, x_5, x_6))
  z_subs = {z_4:x_4, z_5:x_5, z_6:x_6}
  trefoil_matrixes.append(Matrix(QQ, m_t.subs(z_subs).subs(subs_vars_val)))
  trefoil_matrixes_conj.append(Matrix(QQ, m_t_conj.subs(z_subs).subs(subs_vars_val)))

print()
print("calculate egenvectors and egenvalues of matrixes...")
trefoil_egen = []
trefoil_egen_conj = []
for i in range(len(permutations)):
  if not i % 10:
    print(f"{i} of {len(permutations)}")

  # print()
  # show(trefoil_matrixes[i])
  trefoil_egen.append(trefoil_matrixes[i].eigenvectors_right())
  trefoil_egen_conj.append(trefoil_matrixes_conj[i].eigenvectors_right())

print()
print("### eigen vectors of the trivial permutation ###")
print("trefoil")
show(trefoil_egen[0])
print("trefoil conjugated")
show(trefoil_egen_conj[0])

print()
print("calculate charpoly of matrixes...")
trefoil_charpoly = []
trefoil_charpoly_conj = []
for i in range(len(permutations)):
  if not i % 10:
    print(f"{i} of {len(permutations)}")
  trefoil_charpoly.append(trefoil_matrixes[i].charpoly())
  trefoil_charpoly_conj.append(trefoil_matrixes_conj[i].charpoly())

print()
print("### charpoly of the knots ###")
print("trefoil")
show(trefoil_charpoly)
print("trefoil conjugated")
show(trefoil_charpoly_conj)

print()
print("search same charpoly")
similar_charpoly = []
for i, poly in enumerate(trefoil_charpoly):
  try:
    j = trefoil_charpoly_conj.index(poly)
    similar_charpoly.append((poly, permutations[i], permutations[j]))
  except ValueError as error:
    pass

if similar_charpoly:
  print("similar charpoly FOUND!")
  print(similar_charpoly)
else:
  print("similar charpoly NOT found!")


print()
print("collect eigen vectors and eigen values")
trefoil_eigen_vectors = []
for item in trefoil_egen:
  for eg_val, eg_vec, eg_val_mult in item:
    for vect in eg_vec:
      trefoil_eigen_vectors.append(_round(Matrix(CC, eg_vec)))

trefoil_eigen_vectors_conj = []
for item in trefoil_egen_conj:
  for eg_val, eg_vec, eg_val_mult in item:
    for vect in eg_vec:
      trefoil_eigen_vectors_conj.append(_round(Matrix(CC, eg_vec)))

trefoil_eigen_values = []
for item in trefoil_egen:
  for eg_val, eg_vec, eg_val_mult in item:
    trefoil_eigen_values.append(_round_val(CC(eg_val)))

trefoil_eigen_values_conj = []
for item in trefoil_egen_conj:
  for eg_val, eg_vec, eg_val_mult in item:
    trefoil_eigen_values_conj.append(_round_val(CC(eg_val)))


print()
print("total trefoil eigenvectors:", len(trefoil_eigen_vectors))
print("total trefoil conjugated eigenvectors:", len(trefoil_eigen_vectors_conj))

print()
print("search same eigenvectors")
similar_eig_vectors = []
for i, vect in enumerate(trefoil_eigen_vectors):
  try:
    j = trefoil_eigen_vectors_conj.index(vect)
    similar_eig_vectors.append(vect)
  except ValueError as error:
    pass

for i, vect in enumerate(trefoil_eigen_vectors_conj):
  try:
    j = trefoil_eigen_vectors.index(vect)
    if vect not in similar_eig_vectors:
      similar_eig_vectors.append(vect)
  except ValueError as error:
    pass

if similar_eig_vectors:
  print("similar egien vectors FOUND!")
  print(similar_eig_vectors)
else:
  print("similar egien vectors NOT found!")


print()
print("search same eigenvalues")
similar_eig_values = []
for i, val in enumerate(trefoil_eigen_values):
  try:
    j = trefoil_eigen_values_conj.index(val)
    similar_eig_values.append(val)
  except ValueError as error:
    pass


if similar_eig_values:
  print(len(similar_eig_values), "similar egien values trefoil -- conj trefoil FOUND!")
  print(similar_eig_values)
else:
  print("similar egien values NOT found!")


similar_eig_values_2 = []
for i, val in enumerate(trefoil_eigen_values_conj):
  try:
    j = trefoil_eigen_values.index(val)
    similar_eig_values_2.append(val)
  except ValueError as error:
    pass

if similar_eig_values_2:
  print(len(similar_eig_values_2), "similar egien values conj trefoil -- trefoil FOUND!")
  print(similar_eig_values_2)
else:
  print("similar egien values NOT found!")


print()
print("unique trefoil eigen values total count:", len(list(set(trefoil_eigen_values))))
print("unique conjugated trefoil eigen values total count", len(list(set(trefoil_eigen_values_conj))))
print()
print("unique similar trefoil eigen values count:", len(list(set(similar_eig_values))), ", they are", list(set(similar_eig_values)))
print("unique similar conjugated trefoil eigen values count", len(list(set(similar_eig_values_2))), ", they are", list(set(similar_eig_values_2)))

exit()
print()
print("### print eigevectors of similar eigenvalues ###")

print("trefoil -- conj trefoil")
for val in list(set(similar_eig_values)):
  print("  trefoil")
  for item in trefoil_egen:
    for e_val, e_vect, mult in item:
      if _round_val(e_val) == val:
        print("  Value:", val)
        print("  ", e_vect)

  print("  conj trefoil")
  for item in trefoil_egen_conj:
    for e_val, e_vect, mult in item:
      if _round_val(e_val) == val:
        print("  Value:", val)
        print("  ", e_vect)


print("conj trefoil -- trefoil")
for val in list(set(similar_eig_values_2)):
  print("  conj trefoil")
  for item in trefoil_egen_conj:
    for e_val, e_vect, mult in item:
      if _round_val(e_val) == val:
        print("  Value:", val)
        print("  ", e_vect)

  print("  trefoil")
  for item in trefoil_egen:
    for e_val, e_vect, mult in item:
      if _round_val(e_val) == val:
        print("  Value:", val)
        print("  ", e_vect)
