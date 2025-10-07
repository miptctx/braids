from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges,make_subs_dict_for_edges
from braids.utils import sort_triangulation

# Проверка соотношений образующих в группе крашенный кос b(i,j)b(i,k)b(j,k) = b(j,k)b(i,j)b(i,k) = b(i,k)b(j,k)b(i,j),  i < j < k 

# ссылка на конфигурацию:

# i = D4, j = E5, k = G7 l = H8



triangl = sort_triangulation({1,2,4}, {1,3,8},{1,4,5},{1,5,6},{1,6,7},{1,7,8},
                             {2,3,8},{2,4,5},{2,5,6},{2,6,7},{2,7,8})

                             
                             
                             
                             

init_ribs = make_init_vars_for_edges(triangl)

t_ij_ik_jk, e_ij_ik_jk = braiding(triangl, init_ribs,
                            (2,5),(1,4),(5,6),(2,4),(1,5),(4,6), #b(i,j)
                            (1,5),(2,4),(1,6),(4,5),(6,7),(1,4),(2,7),(4,6),(7,8),(2,4),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6), #b(i,k)
                            (1,6),(2,5),(4,5),(6,7),(1,5),(2,7),(5,6),(7,8),(2,5),(1,7),(5,8),(1,6),(4,6),(5,7)) #b(j,k)

t_jk_ij_jk, e_ij_ik_jk = braiding(triangl, init_ribs,                            
                            (1,6),(2,5),(4,5),(6,7),(1,5),(2,7),(5,6),(7,8),(2,5),(1,7),(5,8),(1,6),(4,6),(5,7), #b(j,k)
                            (2,5),(1,4),(5,6),(2,4),(1,5),(4,6), #b(i,j)
                            (1,5),(2,4),(1,6),(4,5),(6,7),(1,4),(2,7),(4,6),(7,8),(2,4),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6)) #b(i,k)


t_ik_jk_ij, e_ik_jk_ij = braiding(triangl, init_ribs,
                            (1,5),(2,4),(1,6),(4,5),(6,7),(1,4),(2,7),(4,6),(7,8),(2,4),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6), #b(i,k)                                                              
                            (1,6),(2,5),(4,5),(6,7),(1,5),(2,7),(5,6),(7,8),(2,5),(1,7),(5,8),(1,6),(4,6),(5,7), #b(j,k)
                            (2,5),(1,4),(5,6),(2,4),(1,5),(4,6)) #b(i,j)



assert t_ij_ik_jk == t_jk_ij_jk == t_ik_jk_ij


e_ij_ik_jk_in_vars = make_subs_dict_for_edges(init_ribs, e_ij_ik_jk) 
e_ij_ik_jk_in_vars = make_subs_dict_for_edges(init_ribs, e_ij_ik_jk) 
e_ik_jk_ij_in_vars = make_subs_dict_for_edges(init_ribs, e_ik_jk_ij) 

print("is realtion valid: ", e_ij_ik_jk_in_vars == e_ij_ik_jk_in_vars == e_ik_jk_ij_in_vars )