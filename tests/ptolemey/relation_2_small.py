# This is trefoil on 2 strands

from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,6),(1,4,5),(1,5,6),(2,3,6),(2,4,5),(2,5,6))

edges_init = make_init_vars_for_edges(T)

t_ijikjk, e_ijikjk = braiding(T, edges_init,
                      (2,5),(1,4),(5,6),(2,4),(1,5),(4,6),
                      (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(3,6),(2,4),(1,6),(3,4),(1,5),(4,6),
                      (2,6),(1,5),(4,5),(3,6),(2,5),(1,6),(3,5),(4,6))

t_ikjkij, e_ikjkij = braiding(T, edges_init,
                      (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(3,6),(2,4),(1,6),(3,4),(1,5),(4,6),
                      (2,6),(1,5),(4,5),(3,6),(2,5),(1,6),(3,5),(4,6),
                      (2,5),(1,4),(5,6),(2,4),(1,5),(4,6))

t_jkijik, e_jkijik = braiding(T, edges_init,
                      (2,6),(1,5),(4,5),(3,6),(2,5),(1,6),(3,5),(4,6),
                      (2,5),(1,4),(5,6),(2,4),(1,5),(4,6),
                      (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(3,6),(2,4),(1,6),(3,4),(1,5),(4,6))

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
