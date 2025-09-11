from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_vars_for_points, make_subs_dict_for_edges
from braids.utils import sort_triangulation


points = [1,2,3,4,5,6,7,8]

all_succ = True

for z_1,z_2,z_3,z_4,z_5,z_6,z_7,z_8 in Permutations(points):
  T = sort_triangulation({z_1,z_2,z_6}, {z_1,z_3,z_4}, {z_1,z_4,z_5}, {z_1,z_5,z_6}, {z_2,z_3,z_8}, {z_2,z_6,z_7}, {z_2,z_7,z_8}, {z_3,z_4,z_8}, {z_4,z_5,z_8}, {z_5,z_7,z_8}, {z_5,z_6,z_7})

  edges_init = make_init_vars_for_edges(T)

  t, e = braiding(T, edges_init, {z_5,z_8},{z_5,z_7},{z_4,z_7},{z_4,z_6},{z_8,z_6})

  assert T == t

  e_subs = make_subs_dict_for_edges(edges_init, e)

  success = (e_subs == make_subs_dict_for_edges(edges_init, edges_init))
  if not success:
    print("Permutation", z_1,z_2,z_3,z_4,z_5,z_6,z_7,z_8, "is not satisfied")

  all_succ &= success

print("All permutation were satisfied:", all_succ)
