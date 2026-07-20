from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation({1,2,7},{1,3,4},{1,4,5},{1,5,6},{1,6,7},{2,3,4},{2,4,5},{2,5,6},{2,6,7})

edges_init = make_init_vars_for_edges(T)

t_ij, e_ij = braiding(T, edges_init, (2,6),(1,7),(5,6), (2,4),(1,5),(5,7),(3,4))

t_ji, e_ji = braiding(T, edges_init, (2,4),(1,5),(5,6),(3,4), (2,6),(1,7),(4,6))

assert t_ij == t_ji

print("Result edges e_ij")
show(make_subs_dict_for_edges(edges_init, e_ij))

print("Result edges e_ji")
show(make_subs_dict_for_edges(edges_init, e_ji))

print("Equation satisfied: ", e_ij == e_ji)
