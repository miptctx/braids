# This is trefoil on 2 strands

from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,8),(1,4,5),(1,5,6),(1,6,7),(1,7,8),(2,3,8),(2,4,5),(2,5,6),(2,6,7),(2,7,8))

edges_init = make_init_vars_for_edges(T)

t_ijkl, e_ijkl = braiding(T, edges_init, (2,5),(1,4),(5,6),(2,4),(1,5),(4,6),   (2,8),(1,7),(3,8),(6,7),(2,7),(1,8),(3,7),(6,8))

t_klij, e_klij = braiding(T, edges_init, (2,8),(1,7),(3,8),(6,7),(2,7),(1,8),(3,7),(6,8),   (2,5),(1,4),(5,6),(2,4),(1,5),(4,6))

assert t_ijkl == t_klij

print("is realtion valid: ", e_ijkl == e_klij)
