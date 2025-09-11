# This is trefoil on 2 strands

from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,8),(1,4,5),(1,5,6),(1,6,7),(1,7,8),(2,3,8),(2,4,5),(2,5,6),(2,6,7),(2,7,8))

edges_init = make_init_vars_for_edges(T)

t_1, e_ijkl = braiding(T, edges_init,
                       (1,5),(2,4),(1,6),(1,7),(4,5),(4,6),(7,8),(2,8),(1,4),(3,8),(4,7),(2,4),(1,8),(1,7),(3,4),(1,6),(4,8),(4,7),(1,5),(4,6),
                       (2,5),(1,6),(4,5),(6,7),(1,5),(2,7),(5,6),(7,8),(2,5),(1,7),(1,6),(5,8),(5,7),(4,6))

t_2, e_klij = braiding(T, edges_init,
                       (2,5),(1,6),(4,5),(6,7),(1,5),(2,7),(5,6),(7,8),(2,5),(1,7),(1,6),(5,8),(5,7),(4,6),
                       (1,5),(2,4),(1,6),(1,7),(4,5),(4,6),(7,8),(2,8),(1,4),(3,8),(4,7),(2,4),(1,8),(1,7),(3,4),(1,6),(4,8),(4,7),(1,5),(4,6))

assert t_1 == t_2

print("Result edges e_ij")
e_ijkl_numbers = make_subs_dict_for_edges(edges_init, e_ijkl)
show(e_ijkl_numbers)

print("Result edges e_ji")
e_klij_numbers = make_subs_dict_for_edges(edges_init, e_klij)
show(e_klij_numbers)

print("is realtion valid: ", e_ijkl_numbers == e_klij_numbers)
