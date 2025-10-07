from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges,make_subs_dict_for_edges
from braids.utils import sort_triangulation

# Проверка соотношений образующих в группе крашенный кос b(j,l)b(k,l)b(i,k)b(j,k) = b(k,l)b(i,k)b(j,k)b(j,l), i < j <k < l 

# ссылка на конфигурацию:

# i = D4, j = E5, k = G7 l = H8



triangl = sort_triangulation({1,2,4}, {1,3,8},{1,4,5},{1,5,6},{1,6,7},{1,7,8},
                             {2,3,8},{2,4,5},{2,5,6},{2,6,7},{2,7,8})

                             
                             
                             
                             

init_ribs = make_init_vars_for_edges(triangl)

t_jl_kl_ik_jk, e_jl_kl_ik_jk = braiding(triangl, init_ribs,
                            (1,6),(2,5),(4,5),(1,7),(1,8),(3,5),(5,6),(7,8),(1,5),(2,8),(5,7),(3,8),(1,8),(2,5),(3,5),(1,7),(5,8),(1,6),(4,6),(5,7), #b(j,l)
                            (1,7),(2,8),(6,7),(3,8),(2,7),(1,8),(6,8),(3,7), #b(k,l)
                            (1,5),(2,4),(1,6),(4,5),(6,7),(1,4),(2,7),(4,6),(7,8),(2,4),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6), #b(i,k)
                            (1,6),(2,5),(4,5),(6,7),(1,5),(2,7),(5,6),(7,8),(2,5),(1,7),(5,8),(1,6),(4,6),(5,7)) #b(j,k)

t_kl_ik_jk_jl, e_kl_ik_jk_jl = braiding(triangl, init_ribs,                            
                            (1,7),(2,8),(6,7),(3,8),(2,7),(1,8),(6,8),(3,7),  #b(k,l) 
                            (1,5),(2,4),(1,6),(4,5),(6,7),(1,4),(2,7),(4,6),(7,8),(2,4),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6), #b(i,k)
                            (1,6),(2,5),(4,5),(6,7),(1,5),(2,7),(5,6),(7,8),(2,5),(1,7),(5,8),(1,6),(4,6),(5,7), #b(j,k)
                            (1,6),(2,5),(4,5),(1,7),(1,8),(3,5),(5,6),(7,8),(1,5),(2,8),(5,7),(3,8),(1,8),(2,5),(3,5),(1,7),(5,8),(1,6),(4,6),(5,7)) #b(j,l)

assert t_jl_kl_ik_jk == t_kl_ik_jk_jl

print("assert -done")

e_jl_kl_ik_jk_in_vars = make_subs_dict_for_edges(init_ribs, e_jl_kl_ik_jk) 
e_kl_ik_jk_jl_in_vars = make_subs_dict_for_edges(init_ribs, e_kl_ik_jk_jl) 

print("initiate vars-done")

print("is realtion valid: ", e_jl_kl_ik_jk_in_vars == e_kl_ik_jk_jl_in_vars)