# This is trefoil on 2 strands

from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,8),(1,4,5),(1,5,6),(1,6,7),(1,7,8),(2,3,8),(2,4,5),(2,5,6),(2,6,7),(2,7,8))

edges_init = make_init_vars_for_edges(T)

t_ijikjk, e_ijikjk = braiding(T, edges_init,
                      (2,5),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6),
                      (2,5),(1,4),(2,6),(2,7),(4,5),(2,8),(3,8),(4,6),(4,7),(2,4),(1,8),(1,7),(3,4),(1,6),(4,8),(4,7),(1,5),(4,6),
                      (2,7),(1,6),(2,8),(5,6),(3,8),(6,7),(2,6),(1,8),(3,6),(1,7),(5,7),(6,8))

t_ikjkij, e_ikjkij = braiding(T, edges_init,
                      (2,5),(1,4),(2,6),(2,7),(4,5),(2,8),(3,8),(4,6),(4,7),(2,4),(1,8),(1,7),(3,4),(1,6),(4,8),(4,7),(1,5),(4,6),
                      (2,7),(1,6),(2,8),(5,6),(3,8),(6,7),(2,6),(1,8),(3,6),(1,7),(5,7),(6,8),
                      (2,5),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6))

t_jkijik, e_jkijik = braiding(T, edges_init,
                      (2,7),(1,6),(2,8),(5,6),(3,8),(6,7),(2,6),(1,8),(3,6),(1,7),(5,7),(6,8),
                      (2,5),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6),
                      (2,5),(1,4),(2,6),(2,7),(4,5),(2,8),(3,8),(4,6),(4,7),(2,4),(1,8),(1,7),(3,4),(1,6),(4,8),(4,7),(1,5),(4,6))

assert t_ijikjk == t_ikjkij and t_ikjkij == t_jkijik

print("Result edges e_ijikjk")
e_ijikjk_n = make_subs_dict_for_edges(edges_init, e_ijikjk)
show(e_ijikjk_n)

print("Result edges e_ikjkij")
e_ikjkij_n = make_subs_dict_for_edges(edges_init, e_ikjkij)
show(e_ikjkij_n)

print("Result edges e_jkijik")
e_jkijik_n = make_subs_dict_for_edges(edges_init, e_jkijik)
show(e_jkijik_n)

print("is realtion valid: ", e_ijikjk_n == e_ikjkij_n and e_ikjkij_n == e_jkijik_n)
