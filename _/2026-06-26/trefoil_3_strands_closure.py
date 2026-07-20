from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation
# from .utils import eqs_and_vars, resolve_eqs


def eqs_and_vars(edges_init, edges_result, edges_changed=dict()):
  eqs = []
  solver_variables = []

  for lhs, rhs in edges_changed.items():
    print(lhs, rhs)
    solver_variables.append(edges_init[lhs])
    if edges_result[rhs] != edges_init[lhs]:
      eqs.append(edges_result[rhs] - edges_init[lhs] == 0)
    else:
      print("Exclude", edges_result[rhs], '==', edges_init[lhs], 'equation')

  return eqs, tuple(solver_variables)


def resolve_eqs(eqs:list, solver_variables:tuple):
  print("### Resolve equations ###")
  print("variables:", *solver_variables)
  for e in eqs:
    print(e)

  res = solve(eqs, *solver_variables)
  print("### Equation system solutions ###")
  #for i, r in enumerate(res):
  #  print('solution', i)
  #  print(r)
  print(res)



z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)


T = sort_triangulation({z_1,z_3,z_4}, {z_1,z_5,z_6}, {z_1,z_2,z_6}, {z_1,z_4,z_5}, {z_2,z_3,z_4}, {z_2,z_4,z_5}, {z_2,z_5,z_6})

edges_init = make_init_vars_for_edges(T)

t, edges_result = braiding(T, edges_init,
                           {z_2,z_5},{z_1,z_6},{z_2,z_4},{z_5,z_6},{z_3,z_4},
                           {z_2,z_4},{z_1,z_5},{z_2,z_6},{z_5,z_4},{z_3,z_6})

edges_result_subs = make_subs_dict_for_edges(edges_init, edges_result)

print('######  edges init  ######')
show(edges_init)

print('######  edges result  ######')
show(edges_result)

eqs, solver_variables = eqs_and_vars(edges_init, edges_result, edges_changed={
    (z_1,z_2): (z_1,z_2),
    (z_1,z_3): (z_1,z_3),
    (z_2,z_3): (z_2,z_3),
    (z_1,z_4): (z_1,z_5),
    (z_1,z_5): (z_1,z_6),
    (z_1,z_6): (z_1,z_4),
    (z_2,z_4): (z_2,z_5),
    (z_2,z_5): (z_2,z_6),
    (z_2,z_6): (z_2,z_4),
    (z_3,z_4): (z_3,z_5),
    (z_4,z_5): (z_5,z_6),
    (z_5,z_6): (z_4,z_6)
  })

resolve_eqs(eqs, solver_variables)

exit()

###########################
###### Add conjugacy ######
###########################

print()
print('#######################')
print('###### Conjugacy ######')
print('#######################')

t, edges_result = braiding(T, edges_init,
                           {z_2,z_5},{z_1,z_4},{z_5,z_6},{z_3,z_4},
                           {z_2,z_4},{z_1,z_6},{z_2,z_5},{z_4,z_6},{z_3,z_5},
                           {z_2,z_5},{z_1,z_4},{z_2,z_6},{z_4,z_5},{z_3,z_6},
                           {z_1,z_6},{z_2,z_4},{z_5,z_6},{z_3,z_4})

edges_result_subs = make_subs_dict_for_edges(edges_init, edges_result)

print('######  edges init  ######')
show(edges_init)

print('######  edges result  ######')
show(edges_result)

eqs, solver_variables = eqs_and_vars(edges_init, edges_result, edges_changed={
    (z_1,z_2): (z_1,z_2),
    (z_1,z_3): (z_1,z_3),
    (z_2,z_3): (z_2,z_3),
    (z_1,z_4): (z_1,z_6),
    (z_1,z_5): (z_1,z_4),
    (z_1,z_6): (z_1,z_5),
    (z_2,z_4): (z_2,z_6),
    (z_2,z_5): (z_2,z_4),
    (z_2,z_6): (z_2,z_5),
    (z_3,z_4): (z_3,z_6),
    (z_4,z_5): (z_4,z_6),
    (z_5,z_6): (z_4,z_5),
  })
resolve_eqs(eqs, solver_variables)


exit()


print('######  edges result  simplified ######')
edges_result_simplified = {}
for e, k in edges_result.items():
  edges_result_simplified[e] = edges_result[e].simplify_full()

show(edges_result_simplified)

print('###### edges result ######')
show(edges_result_subs)

