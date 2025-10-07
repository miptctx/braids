from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges,make_subs_dict_for_edges
from braids.utils import sort_triangulation

# Проверка соотношений образующих в группе крашенный кос b(j,l)b(k,l)b(i,k)b(j,k) = b(k,l)b(i,k)b(j,k)b(j,l), i < j < k < l 

# ссылка на конфигурацию:

# i = D4, j = F6, k = H8 l = K10



triangl = sort_triangulation({1,2,4}, {1,3,10},{1,4,5},{1,5,6},{1,6,7},{1,7,8},{1,8,9},{1,9,10},
                             {2,3,10},{2,4,5},{2,5,6},{2,6,7},{2,7,8},{2,8,9},{2,9,10})

                             
                             
                             
                             

init_ribs = make_init_vars_for_edges(triangl)

t_jl_kl_ik_jk, e_jl_kl_ik_jk = braiding(triangl, init_ribs,
                            (1,7),(2,6),(5,6),(1,8),(6,7),(1,9),(6,8),(9,10),(1,6),(2,10),(6,9),(3,10),(2,6),(1,10),(3,6),(1,9),(6,10),(1,8),
                            (6,9),(1,7),(6,8),(5,7),  #b(j,l) -checked
                            (1,9),(2,8),(7,8),(9,10),(1,8),(2,10),(8,9),(3,10),(2,8),(1,10),(3,8),(1,9),(7,9),(8,10), #b(k,l)-checked
                            (1,5),(2,4),(1,6),(4,5),(1,7),(4,6),(7,8),(1,4),(2,8),(4,7),(8,9),(2,4),(1,8),(4,9),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6), #b(i,k)
                            (1,7),(2,6),(5,6),(7,8),(1,6),(2,8),(6,7),(8,9),(2,6),(1,8),(6,9),(1,7),(5,7),(6,8)) #b(j,k) - checked

t_kl_ik_jk_jl, e_kl_ik_jk_jl = braiding(triangl, init_ribs,                            
                            (1,9),(2,8),(7,8),(9,10),(1,8),(2,10),(8,9),(3,10),(2,8),(1,10),(3,8),(1,9),(7,9),(8,10), #b(k,l)-checked
                            (1,5),(2,4),(1,6),(4,5),(1,7),(4,6),(7,8),(1,4),(2,8),(4,7),(8,9),(2,4),(1,8),(4,9),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6), #b(i,k)
                            (1,7),(2,6),(5,6),(7,8),(1,6),(2,8),(6,7),(8,9),(2,6),(1,8),(6,9),(1,7),(5,7),(6,8), #b(j,k) - checked
                            (1,7),(2,6),(5,6),(1,8),(6,7),(1,9),(6,8),(9,10),(1,6),(2,10),(6,9),(3,10),(2,6),(1,10),(3,6),(1,9),(6,10),(1,8),
                            (6,9),(1,7),(6,8),(5,7))  #b(j,l) -checked

assert t_jl_kl_ik_jk == t_kl_ik_jk_jl

print("assert -done")

e_jl_kl_ik_jk_in_vars = make_subs_dict_for_edges(init_ribs, e_jl_kl_ik_jk) 
e_kl_ik_jk_jl_in_vars = make_subs_dict_for_edges(init_ribs, e_kl_ik_jk_jl) 

print("initiate vars-done")

print("is realtion valid: ", e_jl_kl_ik_jk_in_vars == e_kl_ik_jk_jl_in_vars)