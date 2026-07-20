from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation, get_permutations

GF2 = GF(2)

perms = Permutations([1,2,3,4,5])
#perms = get_permutations()

very_good_pentagons = 0

all_sign_vectors = set()

print("traverse all cycles")

for z_1, z_2, z_3, z_4, z_5 in perms:
  P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

  print(z_1, z_2, z_3, z_4, z_5)

  good_pentagons = 0
  bad_pentagons = 0
  sign_vectors = set()

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
                  for m_cos in range(0,2):
                    for m_sin in range(0,2):
                      t_5, m_5 = braiding(t_4, {z_2,z_5}, i_cos=m_cos, i_sin=m_sin)

                      m = m_5 * m_4 * m_3 * m_2 * m_1
                      assert P == t_5
                      m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
                      if m == matrix([[1,0,0],[0,1,0],[0,0,1]]):
                        # print(i_cos, i_sin, "|", j_cos, j_sin, "|", k_cos, k_sin, "|", l_cos, l_sin, "|", m_cos, m_sin)
                        good_pentagons += 1
                        sign_vectors.add((i_cos, i_sin, j_cos, j_sin, k_cos, k_sin, l_cos, l_sin, m_cos, m_sin))
                        if (i_cos == i_sin) and (j_cos == j_sin) and (k_cos == k_sin) and (l_cos == l_sin) and (m_cos == m_sin):
                          print(i_cos, i_sin, "|", j_cos, j_sin, "|", k_cos, k_sin, "|", l_cos, l_sin, "|", m_cos, m_sin)
                          very_good_pentagons += 1
                      else:
                        bad_pentagons += 1

  M = matrix(GF2, [list(v) for v in sign_vectors])
  rank = M.rank()
  print("sign vectors basis size:", rank)

  E = M.echelon_form()
  independent_vectors = []
  for i in range(E.nrows()):
    if any(E[i, :]):
      independent_vectors.append(M[i])

  #vectors = [vector(GF2, list(v)) for v in independent_vectors]
  #V = VectorSpace(GF2, rank)
  #vectors_in_space = [V(v) for v in vectors]
  #W = V.span(vectors_in_space)
  #W = V.span(vectors)
  #is_vector_space = W.dimension() == len(M)
  #print("Образуют ли векторы векторное пространство?", is_vector_space)
  #print("Размерность подпространства:", W.dimension())
  #quit()

  show(independent_vectors)
  for v in sign_vectors:
    all_sign_vectors.add(v)

  if good_pentagons != 32 and 0:
    print("bad pentagons:", bad_pentagons)
    print("good pentagons:", good_pentagons)
    print("very good pentagons:", very_good_pentagons)
    exit(0)

print("very good pentagons:", very_good_pentagons)

print("all vectors amount:", len(all_sign_vectors))
M = matrix(GF2, [list(v) for v in all_sign_vectors])
rank = M.rank()
print("all sign vectors basis size:", rank)
E = M.echelon_form()
independent_vectors = []
for i in range(E.nrows()):
  if any(E[i, :]):
    independent_vectors.append(M[i])

show(independent_vectors)

## это ерунда
##vectors = [vector(GF2, list(v)) for v in independent_vectors]
#vectors = [vector(GF2, list(v)) for v in all_sign_vectors]
#V = VectorSpace(GF2, rank)
#vectors_in_space = [V(v) for v in vectors]
#W = V.span(vectors_in_space)
##W = V.span(vectors)
#is_vector_space = W.dimension() == len(vectors)
#print("Образуют ли векторы векторное пространство?", is_vector_space)
#print("Размерность подпространства:", W.dimension())


# 1 0 1 1 1 1 0 1 0 1

# 0 0 1 1 0 1 1 1 0 0
# -------------------
# 0 0 1 1 1 0 0 1 1 1
# ===================
# 0 0 0 0 1 1 1 0 1 1


# 0 1 0 1 0 1 0 1 0 0
# 0 1 1 1 1 1 0 1 1 0 
# -------------------
# 0 0 1 0 1 0 0 0 1 0
# -------------------
# 0 0 1 1 0 1 1 1 0 0
# ===================
# 0 0 0 1 1 1 1 1 1 0