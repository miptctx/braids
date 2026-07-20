from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


var('z_1 z_2 z_3 z_4 z_5')

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)

t_0 = sort_triangulation({z_1,z_2,z_5}, {z_1,z_3,z_4}, {z_1,z_4,z_5}, {z_2,z_4,z_5}, {z_2,z_3,z_4})

edges_init = make_init_vars_for_edges(t_0)

t_1, edges = braiding(t_0, edges_init, {z_2,z_4}, {z_1,z_5}, {z_3,z_4})

print("Initial edges")
show(edges_init)

print("Result edges")
show(edges)


l_1 = edges_init[(z_1, z_2)]
l_2 = edges_init[(z_1, z_3)]
l_3 = edges_init[(z_1, z_4)]
l_4 = edges_init[(z_1, z_5)]
l_5 = edges_init[(z_2, z_3)]
l_6 = edges_init[(z_2, z_4)]
l_7 = edges_init[(z_2, z_5)]
l_8 = edges_init[(z_3, z_4)]
l_9 = edges_init[(z_4, z_5)]

eqs = [
  l_1 == l_1,
  l_2 == l_2,
  l_5 == l_5,

  l_3 == (l_2*l_9 + (l_7*l_8 + l_5*l_9)*l_3/l_6)/l_8,
  l_4 == l_3,
  l_6 == l_7,
  l_7 == (l_3*l_7 + l_1*l_9)/l_4,
  l_8 == (l_7*l_8 + l_5*l_9)/l_6,

  l_9 == l_9
]

print("")
print("Resolve equation system")
result = solve(eqs, l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8, l_9)
for res in result:
  print("")
  show(res)

print("")
print("Resolve equation system l_3, l_6, l_7, l_8, l_9")
result = solve(eqs, l_3, l_6, l_7, l_8, l_9)
for res in result:
  show(res)


print("")
print("Resolve equation system l_3, l_7, l_8")
result = solve(eqs, l_3, l_7, l_8)
for res in result:
  show(res)
