from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)

T = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4}, {z_1,z_4,z_5})

edges_init = make_init_vars_for_edges(T)

t, edges_result = braiding(T, edges_init, {z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5},{z_2,z_4})

assert T == t

edges_result_subs = make_subs_dict_for_edges(edges_init, edges_result)

print('######  edges init  ######')
show(edges_init)

print('###### edges result ######')
show(edges_result_subs)

print("Equation satisfied:", edges_result_subs == make_subs_dict_for_edges(edges_init, edges_init))
