from sage.all import *
from braids.utils import get_permutations
from braids.korepanov import braiding
from braids.utils import sort_triangulation


#z_1,z_2,z_3,z_4,z_5 = 1, 2, 3, 4, 5
#z_1,z_2,z_3,z_4,z_5 = 1, 2, 4, 3, 5
#z_1,z_2,z_3,z_4,z_5 = 1, 4, 2, 3, 5
z_1,z_2,z_3,z_4,z_5 = 1, 3, 5, 2, 4

print(z_1, z_2, z_3, z_4, z_5)

P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

good_pentagons = 0
bad_pentagons = 0

perms_dc = Permutations([0,1,2,3])
perms_ds = Permutations([0,1,2,3])
perms_c = Permutations([0,1,2,3])
perms_s = Permutations([0,1,2,3])
for dc_1, dc_2, dc_3, dc_4 in perms_dc:
  for ds_1, ds_2, ds_3, ds_4 in perms_ds:
    for c_1, c_2, c_3, c_4 in perms_c:
      for s_1, s_2, s_3, s_4 in perms_s:

        def cos_f(*args, **kwargs):
          i_1, j_1, k_1, l_1 = args[c_1], args[c_2], args[c_3], args[c_4]
          i_2, j_2, k_2, l_2 = args[dc_1], args[dc_2], args[dc_3], args[dc_4]
          zeta = ((i_1-l_1)*(j_1-k_1)) / ((i_2-k_2)*(j_2-l_2))
          return abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)

        def sin_f(*args, **kwargs):
          i_1, j_1, k_1, l_1 = args[s_1], args[s_2], args[s_3], args[s_4]
          i_2, j_2, k_2, l_2 = args[ds_1], args[ds_2], args[ds_3], args[ds_4]
          zeta = ((i_1-j_1)*(k_1-l_1)) / ((i_2-k_2)*(j_2-l_2))
          return abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)

        t, m = braiding(P, {z_2,z_4},{z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5}, F=CC, cos_f=cos_f, sin_f=sin_f)
        assert P == t

        mp = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

        if (mp == matrix([[1,0,0],[0,1,0],[0,0,1]])):
          good_pentagons += 1
          print("###############")
          print(c_1, c_2, c_3, c_4)
          print(dc_1, dc_2, dc_3, dc_4)
          print(s_1, s_2, s_3, s_4)
          print(ds_1, ds_2, ds_3, ds_4)
          zetas = ['i', 'j', 'k', 'l']
          i_1, j_1, k_1, l_1 = zetas[c_1], zetas[c_2], zetas[c_3], zetas[c_4]
          i_2, j_2, k_2, l_2 = zetas[dc_1], zetas[dc_2], zetas[dc_3], zetas[dc_4]
          print("cos_f:", f"(({i_1}-{l_1})*({j_1}-{k_1})) / (({i_2}-{k_2})*({j_2}-{l_2}))")
          i_1, j_1, k_1, l_1 = zetas[s_1], zetas[s_2], zetas[s_3], zetas[s_4]
          i_2, j_2, k_2, l_2 = zetas[ds_1], zetas[ds_2], zetas[ds_3], zetas[ds_4]
          print("sin_f:", f"(({i_1}-{j_1})*({k_1}-{l_1})) / (({i_2}-{k_2})*({j_2}-{l_2}))")
        else:
          bad_pentagons += 1


print("Good pentagons:", good_pentagons)
print("Bad pentagons:", bad_pentagons)

quit()


perms = Permutations([1,2,3,4,5])
# perms = get_permutations()

good_pentagons = 0
bad_pentagons = 0

for p_1, p_2, p_3, p_4, p_5 in perms:
  # x_1, x_2, x_3, x_4, x_5 = elements[p_1-1], elements[p_2-1], elements[p_3-1], elements[p_4-1], elements[p_5-1]

  # _m_l = m_l.subs({z_1: x_1, z_2: x_2, z_3: x_3, z_4: x_4, z_5: x_5})
  _m_l = m_l.subs({z_1: p_1, z_2: p_2, z_3: p_3, z_4: p_4, z_5: p_5})
  _m_l = _m_l.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

  # _m_r = m_r.subs({z_1: x_1, z_2: x_2, z_3: x_3, z_4: x_4, z_5: x_5})
  _m_r = m_r.subs({z_1: p_1, z_2: p_2, z_3: p_3, z_4: p_4, z_5: p_5})
  _m_r = _m_r.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

  # m_p = m_p.subs({z_1: x_1, z_2: x_2, z_3: x_3, z_4: x_4, z_5: x_5})
  _m_p = m_p.subs({z_1: p_1, z_2: p_2, z_3: p_3, z_4: p_4, z_5: p_5})
  _m_p = _m_p.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

  if (_m_l != _m_r):
  # if (_m_p != matrix([[1,0,0],[0,1,0],[0,0,1]])):
    bad_pentagons += 1
    # print("###############")
    # # print(x_1, x_2, x_3, x_4, x_5)
    print(p_1, p_2, p_3, p_4, p_5)
    show(_m_l)
    print("")
    show(_m_r)
    # show(_m_p)
  else:
    # print(p_1, p_2, p_3, p_4, p_5)
    good_pentagons += 1


print("Good pentagons:", good_pentagons)
print("Bad pentagons:", bad_pentagons)
