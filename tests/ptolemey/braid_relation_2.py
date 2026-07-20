# This is trefoil on 2 strands

from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation({1,2,6}, {1,3,4},{1,4,5},{1,5,6},{2,3,4},{2,4,5},{2,5,6})

edges_init = make_init_vars_for_edges(T)

t_l, e_l = braiding(T, edges_init,
                  (2,5),(1,6),(4,5),
                  (1,6),(2,4),(5,6),(3,4),
                  (2,4),(1,5),(4,6))

t_r, e_r = braiding(T, edges_init,
                  (1,5),(2,4),(5,6),(3,4),
                  (2,4),(1,6),(4,5),
                  (1,6),(2,5),(4,6),(3,5))

assert t_l == t_r

print("Result edges e_l")
show(make_subs_dict_for_edges(edges_init, e_l))

print("Result matrix e_r")
show(make_subs_dict_for_edges(edges_init, e_r))

print("Equation satisfied: ", e_l == e_r)
