from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_vars_for_points, make_subs_dict_for_edges
from braids.utils import sort_triangulation


# points = (1,2,3,4,5)

# make_vars_for_points(*points)
z_1,z_2,z_3,z_4,z_5,z_6,z_7,z_8 = var("z_1,z_2,z_3,z_4,z_5,z_6,z_7,z_8")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)
assume(z_6 < z_7)
assume(z_7 < z_8)

T = sort_triangulation({z_1,z_2,z_6}, {z_1,z_3,z_4}, {z_1,z_4,z_5}, {z_1,z_5,z_6}, {z_2,z_3,z_8}, {z_2,z_6,z_7}, {z_2,z_7,z_8}, {z_3,z_4,z_8}, {z_4,z_5,z_8}, {z_5,z_7,z_8}, {z_5,z_6,z_7})

edges_init = make_init_vars_for_edges(T)

t, edges_result = braiding(T, edges_init, {z_5,z_8},{z_5,z_7},{z_4,z_7},{z_4,z_6},{z_8,z_6})

assert T == t

edges_result_subs = make_subs_dict_for_edges(edges_init, edges_result)

# print('################')
# show(edges_result_subs)

print("Equation satisfied:", edges_result_subs == make_subs_dict_for_edges(edges_init, edges_init))
