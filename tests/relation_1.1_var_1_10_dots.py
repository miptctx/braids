from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation

# Проверка соотношений образующих в группе крашенный кос b(i,j)b(k,l) = b(k,l)b(i,j) , k < l < i < j

# ссылка на конфигурацию:

# k = D4, l = F6, i = H8 j = K10



triangl = sort_triangulation({1,2,4}, {1,3,10},{1,4,5},{1,5,6},{1,6,7},{1,7,8},{1,8,9},{1,9,10},
                             {2,3,10},{2,4,5},{2,5,6},{2,6,7},{2,7,8},{2,8,9},{2,9,10})

                             
                             
                          
init_ribs = make_init_vars_for_edges(triangl)


t_ij_kl, e_ij_kl = braiding(triangl, init_ribs,                            
                            (1,9),(2,8),(7,8),(9,10),(1,8),(2,10),(8,9),(3,10),(2,8),(1,10),(3,8),(1,9),(7,9),(8,10),  #b(i,j) checked
                            (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6)) #b(k,l)


t_kl_ij, e_kl_ij = braiding(triangl, init_ribs,
                            (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6), #b(k,l)
                            (1,9),(2,8),(7,8),(9,10),(1,8),(2,10),(8,9),(3,10),(2,8),(1,10),(3,8),(1,9),(7,9),(8,10)) #b(i,j)


e_ij_kl_in_vars = make_subs_dict_for_edges(init_ribs, e_ij_kl)

print("init vars ij_kl - done")

e_kl_ij_in_vars = make_subs_dict_for_edges(init_ribs, e_kl_ij)

print("init vars kl_ij - done")

assert t_ij_kl == t_kl_ij

print("asserts - done")

print("is realtion valid: ", e_ij_kl_in_vars == e_kl_ij_in_vars)