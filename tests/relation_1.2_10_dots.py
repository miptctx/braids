from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges,make_subs_dict_for_edges
from braids.utils import sort_triangulation

# Проверка соотношений образующих в группе крашенный кос b(i,j)b(i,k)b(j,k) = b(j,k)b(i,j)b(i,k) = b(i,k)b(j,k)b(i,j),  i < j < k 

# ссылка на конфигурацию:

# i = D4, j = F6, k = K10



triangl = sort_triangulation({1,2,4}, {1,3,10},{1,4,5},{1,5,6},{1,6,7},{1,7,8},{1,8,9},{1,9,10},
                             {2,3,10},{2,4,5},{2,5,6},{2,6,7},{2,7,8},{2,8,9},{2,9,10})

                             
                             
                             
                             

init_ribs = make_init_vars_for_edges(triangl)

t_ij_ik_jk, e_ij_ik_jk = braiding(triangl, init_ribs,
                                  (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6), #b(i,j) checked
                                  (1,5),(2,4),(1,6),(4,5),(1,7),(4,6),(1,8),(1,9),(4,7),(4,8),(9,10),(1,4),(2,10),(4,9),(3,10),(2,4),(1,10),(3,4),(1,9),
                                  (4,10),(1,8),(4,9),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6), #b(i,k) checked
                                  (1,7),(2,6),(5,6),(1,8),(6,7),(1,9),(6,8),(9,10),(1,6),(2,10),(6,9),(3,10),(2,6),(1,10),(3,6),(1,9),(6,10),(1,8),
                                  (6,9),(1,7),(6,8),(5,7)) #b(j,k)   

t_jk_ij_ik, e_ik_ij_ik = braiding(triangl, init_ribs,
                                  (1,7),(2,6),(5,6),(1,8),(6,7),(1,9),(6,8),(9,10),(1,6),(2,10),(6,9),(3,10),(2,6),(1,10),(3,6),(1,9),(6,10),(1,8),
                                  (6,9),(1,7),(6,8),(5,7),  #b(j,k)                           
                                  (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6), #b(i,j) checked
                                  (1,5),(2,4),(1,6),(4,5),(1,7),(4,6),(1,8),(1,9),(4,7),(4,8),(9,10),(1,4),(2,10),(4,9),(3,10),(2,4),(1,10),(3,4),(1,9),
                                  (4,10),(1,8),(4,9),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6)) #b(i,k) checked                                  


t_ik_jk_ij, e_ik_jk_ij = braiding(triangl, init_ribs,
                                  (1,5),(2,4),(1,6),(4,5),(1,7),(4,6),(1,8),(1,9),(4,7),(4,8),(9,10),(1,4),(2,10),(4,9),(3,10),(2,4),(1,10),(3,4),(1,9),
                                  (4,10),(1,8),(4,9),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6), #b(i,k) checked                                  
                                  (1,7),(2,6),(5,6),(1,8),(6,7),(1,9),(6,8),(9,10),(1,6),(2,10),(6,9),(3,10),(2,6),(1,10),(3,6),(1,9),(6,10),(1,8),
                                  (6,9),(1,7),(6,8),(5,7),  #b(j,k) 
                                  (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6)) #b(i,j) checked 



assert t_ij_ik_jk == t_jk_ij_ik == t_ik_jk_ij

print("assert - done")


e_ij_ik_jk_in_vars = make_subs_dict_for_edges(init_ribs, e_ij_ik_jk) 

print("e_ij_ik_jk_in_vars - done")

e_ik_ij_ik_in_vars = make_subs_dict_for_edges(init_ribs, e_ij_ik_jk)

print("e_ij_ik_jk_in_vars - done") 

e_ik_jk_ij_in_vars = make_subs_dict_for_edges(init_ribs, e_ik_jk_ij) 

print("e_ik_jk_ij_in_vars - done") 

print("is realtion valid: ", e_ij_ik_jk_in_vars == e_ij_ik_jk_in_vars == e_ik_jk_ij_in_vars )