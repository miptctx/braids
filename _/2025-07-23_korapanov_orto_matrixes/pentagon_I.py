from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation


z_1 = 1#1
z_2 = 2#2
z_3 = 3#4
z_4 = 4#5
z_5 = 5#3

P = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4}, {z_1,z_4,z_5})

unique_indexes = set()

good_pentagons = 0
bad_pentagons = 0

for i_cos in range(0,2):
  for i_sin in range(0,2):
    t_1, m_1 = braiding(P, {z_1,z_4}, i_cos=i_cos, i_sin=i_sin)
    for j_cos in range(0,2):
      for j_sin in range(0,2):
        t_2, m_2 = braiding(t_1, {z_1,z_3}, i_cos=j_cos, i_sin=j_sin)
        for k_cos in range(0,2):
          for k_sin in range(0,2):
            t_3, m_3 = braiding(t_2, {z_3,z_5}, i_cos=k_cos, i_sin=k_sin)
            for l_cos in range(0,2):
              for l_sin in range(0,2):
                t_4, m_4 = braiding(t_3, {z_2,z_5}, i_cos=l_cos, i_sin=l_sin)
                found = False
                for m_cos in range(0,2):
                  for m_sin in range(0,2):
                    t_5, m_5 = braiding(t_4, {z_2,z_4}, i_cos=m_cos, i_sin=m_sin)

                    m = m_5 * m_4 * m_3 * m_2 * m_1
                    assert P == t_5
                    m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
                    if m == matrix([[1,0,0],[0,1,0],[0,0,1]]):
                      '''
                      print(
                        'i_cos=', i_cos, 'i_sin=', i_sin, '| j_cos=', j_cos, 'j_sin=', j_sin,
                        '| k_cos=', k_cos, 'k_sin=', k_sin, '| l_cos=', l_cos, 'l_sin=', l_sin,
                        '| m_cos=', m_cos, 'm_sin=', m_sin
                      )
                      '''
                      print(i_cos, i_sin, "|", j_cos, j_sin, "|", k_cos, k_sin, "|", l_cos, l_sin, "|", m_cos, m_sin)
                      found = True
                      good_pentagons += 1
                    else:
                      # print("")
                      # show(m)
                      bad_pentagons += 1
                #if found:
                #  print(i_cos, i_sin, "|", j_cos, j_sin, "|", k_cos, k_sin, "|", l_cos, l_sin)

print("bad pentagond:", bad_pentagons)
print("good pentagond:", good_pentagons)


