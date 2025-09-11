# This is trefoil on 2 strands

from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,7),(1,4,5),(1,5,6),(1,6,7),(2,3,7),(2,4,5),(2,5,6),(2,6,7))

edges_init = make_init_vars_for_edges(T)

t_1, e_ij_kl = braiding(T, edges_init,
                       (1,5),(2,4),(1,6),(4,5),(6,7),(1,4),(2,7),(4,6),(3,7),(2,4),(1,7),(1,6),(3,4),(4,7),(1,5),(4,6),
                       (2,6),(1,5),(4,5),(6,7),(2,5),(1,6),(5,7),(4,6))

t_2, e_kl_ij = braiding(T, edges_init,
                       (2,6),(1,5),(4,5),(6,7),(2,5),(1,6),(5,7),(4,6),
                       (1,5),(2,4),(1,6),(4,5),(6,7),(1,4),(2,7),(4,6),(3,7),(2,4),(1,7),(1,6),(3,4),(4,7),(1,5),(4,6))

assert t_1 == t_2

print("Result edges e_ij")
e_ij_kl_numbers = make_subs_dict_for_edges(edges_init, e_ij_kl)
show(e_ij_kl_numbers)

print("Result edges e_ji")
e_kl_ij_numbers = make_subs_dict_for_edges(edges_init, e_kl_ij)
show(e_kl_ij_numbers)

print("is realtion valid: ", e_ij_kl_numbers == e_kl_ij_numbers)
