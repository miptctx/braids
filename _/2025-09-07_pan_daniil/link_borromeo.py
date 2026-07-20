from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation

z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6
# z_1,z_2,z_3,z_4,z_5,z_6 = 1,4,3,6,5,2
# z_1,z_2,z_3,z_4,z_5,z_6 = 7,13,23,193,419,601

t_0 = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_6},{z_1,z_4,z_5},{z_1,z_5,z_6}, {z_2,z_3,z_6},{z_2,z_4,z_5},{z_2,z_5,z_6})

edges_init = make_init_vars_for_edges(t_0)

t_1, m = braiding(t_0, edges_init,
                  (z_1,z_5),(z_2,z_4),(z_5,z_6),
                  (z_2,z_6),(z_1,z_4),(z_4,z_5),(z_3,z_6),
                  (z_1,z_6),(z_2,z_5),(z_4,z_6),
                  (z_2,z_4),(z_1,z_5),(z_5,z_6),(z_3,z_4),
                  (z_1,z_4),(z_2,z_6),(z_4,z_5),
                  (z_2,z_5),(z_1,z_6),(z_4,z_6),(z_3,z_5))

# assert t_1 == t_0

print("Result edges e_ij")
show(make_subs_dict_for_edges(edges_init, m, diff=False))
print("")
show(make_subs_dict_for_edges(edges_init, m, diff=True))
