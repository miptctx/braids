from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

F = SR

z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)

subs_vars_val = {z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5, z_6: 6}


T = sort_triangulation({z_1,z_3,z_4}, {z_1,z_5,z_6}, {z_1,z_2,z_6}, {z_1,z_4,z_5}, {z_2,z_3,z_4}, {z_2,z_4,z_5}, {z_2,z_5,z_6})


##################################
##### trefoil on 3 strands #######
##################################
t, m_t = braiding(T,
                {z_2,z_5},{z_1,z_6},{z_2,z_4},{z_5,z_6},{z_3,z_4},
                {z_2,z_4},{z_1,z_5},{z_2,z_6},{z_5,z_4},{z_3,z_6},
                F=F)

m_t_int = m_t.subs(subs_vars_val)

print()
print('######  matrix result for trefoil  ######')
show(latex(m_t_int))
print("Det:", m_t_int.det())
print("Trace:", latex(m_t_int.trace()))
print("Charpoly", latex(m_t_int.charpoly()))

################################
##### Conjugated trefoil #######
################################

t_top, m_top = braiding(T, {z_2,z_5},{z_1,z_4},{z_5,z_6},{z_3,z_4}, F=F)
t_bot, m_bot = braiding(T, {z_2,z_4},{z_1,z_5},{z_5,z_6},{z_3,z_4}, F=F)
assert t_top == t_bot

m = m_bot.subs({z_4:z_5, z_5:z_6, z_6:z_4})*m_t
m = m.subs({z_4:z_5, z_5:z_4})*m_top

m_conj_int = m.subs(subs_vars_val)

print()
print('######  matrix result conjugated trefoil ######')
show(latex(m_conj_int))
print("Det:", m_conj_int.det())
print("Trace:", latex(m_conj_int.trace()))
print("Charpoly", latex(m_conj_int.charpoly()))


print()
print("#### Check ####")
m_check = m_bot.subs({z_4:z_5, z_5:z_4})*m_top
m_check = m_check.simplify_full()
show(m_check)
