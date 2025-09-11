# This is trefoil on 2 strands

from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,8),(1,4,5),(1,5,6),(1,6,7),(1,7,8),(2,3,8),(2,4,5),(2,5,6),(2,6,7),(2,7,8))

edges_init = make_init_vars_for_edges(T)

t_jk_ik_kl_jl, e_jk_ik_kl_jl = braiding(T, edges_init,
                                        (1,5),(2,6),(2,7),(4,5),(5,6),(7,8),(2,5),(1,7),(1,6),(5,8),(5,7),(4,6),
                                        (2,5),(1,4),(2,6),(2,7),(4,5),(4,6),(7,8),(2,4),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6),
                                        (1,7),(2,8),(3,8),(6,7),(2,7),(1,8),(3,7),(6,8),
                                        (2,6),(1,5),(2,7),(2,8),(4,5),(3,8),(5,6),(5,7),(1,8),(2,5),(1,7),(3,5),(1,6),(5,8),(4,6),(5,7))

t_jl_jk_ik_kl, e_jl_jk_ik_kl = braiding(T, edges_init,
                                        (2,6),(1,5),(2,7),(2,8),(4,5),(3,8),(5,6),(5,7),(1,8),(2,5),(1,7),(3,5),(1,6),(5,8),(4,6),(5,7),
                                        (1,5),(2,6),(2,7),(4,5),(5,6),(7,8),(2,5),(1,7),(1,6),(5,8),(5,7),(4,6),
                                        (2,5),(1,4),(2,6),(2,7),(4,5),(4,6),(7,8),(2,4),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6),
                                        (1,7),(2,8),(3,8),(6,7),(2,7),(1,8),(3,7),(6,8))

assert t_jk_ik_kl_jl == t_jl_jk_ik_kl

print("Result edges e_jk_ik_kl_jl")
e_jk_ik_kl_jl_n = make_subs_dict_for_edges(edges_init, e_jk_ik_kl_jl)
show(e_jk_ik_kl_jl_n)

print("Result edges e_jl_jk_ik_kl")
e_jl_jk_ik_kl_n = make_subs_dict_for_edges(edges_init, e_jl_jk_ik_kl)
show(e_jl_jk_ik_kl_n)

print("is relation valid: ", e_jk_ik_kl_jl_n == e_jl_jk_ik_kl_n)
