from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation

# Проверка соотношений образующих в группе крашенный кос b(i,j)b(k,l) = b(k,l)b(i,j) , k < l < i < j

# ссылка на конфигурацию:

# k = D4, l = E5, i = G7 j = H8



triangl = sort_triangulation({1,2,4}, {1,3,8},{1,4,5},{1,5,6},{1,6,7},{1,7,8},
                             {2,3,8},{2,4,5},{2,5,6},{2,6,7},{2,7,8})

                             
                             
                          
init_ribs = make_init_vars_for_edges(triangl)

t_ij_kl, e_ij_kl = braiding(triangl, init_ribs,
                            (2,5),(1,4),(5,6),(2,4),(1,5),(4,6), #b(k,l)
                            (1,7),(2,8),(6,7),(3,8),(2,7),(1,8),(6,8),(3,7)) #b(i,j)


t__kl_ij, e_kl_ij = braiding(triangl, init_ribs,                            
                            (1,7),(2,8),(6,7),(3,8),(2,7),(1,8),(6,8),(3,7),  #b(i,j) checked
                            (2,5),(1,4),(5,6),(2,4),(1,5),(4,6),) #b(k,l)


e_ij_kl_in_vars = make_subs_dict_for_edges(init_ribs, e_ij_kl)
e_kl_ij_in_vars = make_subs_dict_for_edges(init_ribs, e_kl_ij)

assert t_ij_kl == t__kl_ij

print("is realtion valid: ", e_ij_kl_in_vars == e_kl_ij_in_vars)