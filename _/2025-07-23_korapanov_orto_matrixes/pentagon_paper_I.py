from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


#z_1, z_2, z_3, z_4, z_5 = 1, 2, 3, 4, 5
#z_1, z_2, z_3, z_4, z_5 = 9, 2, 3, 4, 5
#z_1, z_2, z_3, z_4, z_5 = 1, 2, 3, 5, 4
#z_1, z_2, z_3, z_4, z_5 = 1, 2, 4, 3, 5 #!
#z_1, z_2, z_3, z_4, z_5 = 1, 2, 4, 7, 5
#z_1, z_2, z_3, z_4, z_5 = 8, 2, 4, 5, 3
#z_1, z_2, z_3, z_4, z_5 = 1, 2, 4, 5, 3 #!
#z_1, z_2, z_3, z_4, z_5 = 5, 4, 2, 3, 1
#z_1, z_2, z_3, z_4, z_5 = 1, 3, 2, 5, 4 #!
#z_1, z_2, z_3, z_4, z_5 = 1, 3, 4, 2, 5 #!
#z_1, z_2, z_3, z_4, z_5 = 1, 3, 2, 4, 5
#z_1, z_2, z_3, z_4, z_5 = 1, 3, 5, 2, 4 #!
#z_1, z_2, z_3, z_4, z_5 = 1, 4, 2, 3, 5 #!
#z_1, z_2, z_3, z_4, z_5 = 2, 3, 5, 1, 4
z_1, z_2, z_3, z_4, z_5 = 1, 5, 2, 3, 4
#z_1, z_2, z_3, z_4, z_5 = 1, 4, 3, 2, 5

print(z_1, z_2, z_3, z_4, z_5)
print("----------------")

P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

t, m = braiding(P, {z_2,z_4},{z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5})
print_triangles_pretty(P)
print_triangles_pretty(t)
assert P == t
m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
show(m)
print('################')

# quit(0)

unique_indexes = set()

good_pentagons = 0
bad_pentagons = 0
sign_vectors = list()
GF2 = GF(2)

for i_cos in range(0,2):
  for i_sin in range(0,2):
    t_1, m_1 = braiding(P, {z_2,z_4}, i_cos=i_cos, i_sin=i_sin)
    for j_cos in range(0,2):
      for j_sin in range(0,2):
        t_2, m_2 = braiding(t_1, {z_1,z_4}, i_cos=j_cos, i_sin=j_sin)
        for k_cos in range(0,2):
          for k_sin in range(0,2):
            t_3, m_3 = braiding(t_2, {z_1,z_3}, i_cos=k_cos, i_sin=k_sin)
            for l_cos in range(0,2):
              for l_sin in range(0,2):
                t_4, m_4 = braiding(t_3, {z_3,z_5}, i_cos=l_cos, i_sin=l_sin)
                found = False
                for m_cos in range(0,2):
                  for m_sin in range(0,2):
                    t_5, m_5 = braiding(t_4, {z_2,z_5}, i_cos=m_cos, i_sin=m_sin)

                    m = m_5 * m_4 * m_3 * m_2 * m_1
                    assert P == t_5
                    m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
                    if m == matrix([[1,0,0],[0,1,0],[0,0,1]]):
                      print(i_cos, i_sin, "|", j_cos, j_sin, "|", k_cos, k_sin, "|", l_cos, l_sin, "|", m_cos, m_sin)
                      found = True
                      good_pentagons += 1
                      sign_vectors.append(vector(GF2, [i_cos, i_sin, j_cos, j_sin, k_cos, k_sin, l_cos, l_sin, m_cos, m_sin]))
                    else:
                      # print("")
                      # show(m)
                      bad_pentagons += 1
                #if found:
                #  print(i_cos, i_sin, "|", j_cos, j_sin, "|", k_cos, k_sin, "|", l_cos, l_sin)


print("bad pentagons:", bad_pentagons)
print("good pentagons:", good_pentagons)
print("sign vectors size:", len(sign_vectors))

# M = matrix(GF2, [list(v) for v in sign_vectors])
M = matrix(GF2, sign_vectors)
rank = M.rank()
print("sign vectors basis size:", rank)

E = M.echelon_form()
independent_vectors = []
for i in range(E.nrows()):
  if any(E[i, :]):
    independent_vectors.append(E[i])

show(independent_vectors)

shift_vect = sign_vectors[0]
assert shift_vect in sign_vectors
print("shift vector:", shift_vect)

vector_space = []
for v in sign_vectors:
  vect = vector(GF2, list(v))
  vector_space.append(vect - shift_vect)

print("Vector space:")
for v in vector_space:
  show(v)

# is_vector_space = True
for i in range(len(vector_space)):
  for j in range(i+1, len(vector_space)):
    vect = vector_space[i] + vector_space[j]
    assert vect in vector_space
    # is_vector_space &= vect in vector_space
    #if not is_vector_space:
    #  break

# print("is all pairs in space:", is_vector_space)
M = matrix(GF2, vector_space)
rank = M.rank()
print("new vector space basis size:", rank)
E = M.echelon_form()
independent_vectors = []
for i in range(E.nrows()):
  if any(E[i, :]):
    independent_vectors.append(E[i])

for v in independent_vectors:
  assert v in vector_space

print("new vector space basis:")
show(independent_vectors)
