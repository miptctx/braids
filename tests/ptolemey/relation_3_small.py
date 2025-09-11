# This is trefoil on 2 strands

from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,7),(1,4,5),(1,5,6),(1,6,7),(2,3,7),(2,4,5),(2,5,6),(2,6,7))

edges_init = make_init_vars_for_edges(T)

t_jl_kl_ik_jk, e_jl_kl_ik_jk = braiding(T, edges_init,
                                        (2,5),(1,6),(4,5),(6,7),(1,5),(2,7),(5,6),(3,7),(2,5),(1,7),(3,5),(1,6),(5,7),(4,6),
                                        (2,7),(1,6),(5,6),(3,7),(2,6),(1,7),(3,6),(5,7),
                                        (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6),
                                        (2,6),(1,5),(4,5),(6,7),(2,5),(1,6),(5,7),(4,6))

t_kl_ik_jk_jl, e_kl_ik_jk_jl = braiding(T, edges_init,
                                        (2,7),(1,6),(5,6),(3,7),(2,6),(1,7),(3,6),(5,7),
                                        (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6),
                                        (2,6),(1,5),(4,5),(6,7),(2,5),(1,6),(5,7),(4,6),
                                        (2,5),(1,6),(4,5),(6,7),(1,5),(2,7),(5,6),(3,7),(2,5),(1,7),(3,5),(1,6),(5,7),(4,6))

assert t_jl_kl_ik_jk == t_kl_ik_jk_jl

print("Result edges e_jk_ik_kl_jl")
e_jl_kl_ik_jk_n = make_subs_dict_for_edges(edges_init, e_jl_kl_ik_jk)
show(e_jl_kl_ik_jk_n)

print("Result edges e_jl_jk_ik_kl")
e_kl_ik_jk_jl_n = make_subs_dict_for_edges(edges_init, e_kl_ik_jk_jl)
show(e_kl_ik_jk_jl_n)

print("is relation valid: ", e_jl_kl_ik_jk_n == e_kl_ik_jk_jl_n)
