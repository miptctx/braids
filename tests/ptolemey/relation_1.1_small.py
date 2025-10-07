# This is trefoil on 2 strands

from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,7),(1,4,5),(1,5,6),(1,6,7),(2,3,7),(2,4,5),(2,5,6),(2,6,7))

edges_init = make_init_vars_for_edges(T)

t_ij_kl, e_ij_kl = braiding(T, edges_init, (2,5),(1,4),(5,6),(2,4),(1,5),(4,6),  (2,7),(1,6),(5,6),(3,7),(2,6),(1,7),(3,6),(5,7))

t_kl_ij, e_kl_ij = braiding(T, edges_init, (2,7),(1,6),(5,6),(3,7),(2,6),(1,7),(3,6),(5,7),  (2,5),(1,4),(5,6),(2,4),(1,5))

assert t_ij_kl == t_kl_ij

print("is realtion valid: ", e_ij_kl == e_kl_ij)
