from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation


z_1,z_2,z_3,z_4,z_5 = var("z_1,z_2,z_3,z_4,z_5")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)


T = sort_triangulation({z_1,z_3,z_4}, {z_1,z_2,z_5}, {z_1,z_4,z_5}, {z_2,z_3,z_4}, {z_2,z_4,z_5})

edges_init = make_init_vars_for_edges(T)

t, edges_result = braiding(T, edges_init, {z_1,z_4},{z_2,z_5},{z_3,z_4})

edges_result_subs = make_subs_dict_for_edges(edges_init, edges_result)

print('######  edges init  ######')
show(edges_init)

print('######  edges result  ######')
show(edges_result)

raise("Система уравнений составляет некорректно, ребра нужно сопоставлять как в файле trefoil_3_strands_conjugation_and_closure")

eqs = []
helper_variables = []
for lhs, rhs in zip(edges_init.keys(), edges_result.keys()):
  # только ребро 34 сменяется на 35 и все.
  if lhs != (z_3, z_4) and rhs != (z_3, z_5):
    assert lhs == rhs

  print("add variable:", edges_init[lhs])
  helper_variables.append(edges_init[lhs])
  eqs.append(edges_init[lhs] == edges_result[rhs])

print("### Resolve equations ###")
print("variables:", *tuple(helper_variables))
for e in eqs:
  print(e)

res = solve(eqs, *tuple(helper_variables))
print("### Results ###")
for r in res:
  print(r)


exit()


print('######  edges result  simplified ######')
edges_result_simplified = {}
for e, k in edges_result.items():
  edges_result_simplified[e] = edges_result[e].simplify_full()

show(edges_result_simplified)

print('###### edges result ######')
show(edges_result_subs)

