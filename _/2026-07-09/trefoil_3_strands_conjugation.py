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
t, m = braiding(T,
                {z_2,z_5},{z_1,z_6},{z_2,z_4},{z_5,z_6},{z_3,z_4},
                {z_2,z_4},{z_1,z_5},{z_2,z_6},{z_5,z_4},{z_3,z_6},
                F=F)

m = m.subs(subs_vars_val)

print()
print('######  matrix result for trefoil  ######')
show(latex(m))
print("Det:", m.det())
print("Trace:", latex(m.trace()))
print("Charpoly", m.charpoly())

################################
##### Conjugated trefoil #######
################################

t, m = braiding(T,
                {z_2,z_5},{z_1,z_4},{z_5,z_6},{z_3,z_4},
                {z_2,z_4},{z_1,z_6},{z_2,z_5},{z_4,z_6},{z_3,z_5},
                {z_2,z_5},{z_1,z_4},{z_2,z_6},{z_4,z_5},{z_3,z_6},
                {z_1,z_6},{z_2,z_4},{z_5,z_6},{z_3,z_4},
                F=F)

m = m.subs(subs_vars_val)

print()
print('######  matrix result conjugated trefoil ######')
show(latex(m))
print("Det:", m.det())
print("Trace:", latex(m.trace()))
print("Charpoly", m.charpoly())
