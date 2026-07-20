from sage.all import *
from braids.ptolemey import braiding
from braids.ptolemey.utils import make_init_vars_for_edges, make_subs_dict_for_edges
from braids.utils import sort_triangulation
#from .utils import eqs_and_vars, resolve_eqs


def eqs_and_vars(edges_init, edges_result, edges_changed=dict(), exclude=True):
  eqs = []
  solver_variables = []
  all_variables = []
  trivial_variables = []
  non_trivial_variables = []

  for lhs, rhs in edges_changed.items():
    print(lhs, rhs)
    solver_variables.append(edges_init[lhs])
    if exclude:
      if edges_result[rhs] != edges_init[lhs]:
        eqs.append((edges_result[rhs] - edges_init[lhs]).simplify_full() == 0)
      else:
        print("Exclude", edges_result[rhs], '==', edges_init[lhs], 'equation')
    else:
      # eqs.append((edges_result[rhs] - edges_init[lhs]).simplify_full() == 0)
      eqs.append(edges_result[rhs] == edges_init[lhs])

  return eqs, tuple(solver_variables)


def resolve_eqs(eqs:list, solver_variables:tuple):
  print("### Resolve equations ###")
  print("variables:", *solver_variables)
  for e in eqs:
    print(e)

  res = solve(eqs, *solver_variables, solution_dict=True)
  print("### Equation system solutions ###")
  #for i, r in enumerate(res):
  #  print('solution', i)
  #  print(r)
  print(res)
  return res


def check_solutions(system, solutions):
  """
  system    — список уравнений, например [x + y == 1, x - y == 3]
  solutions — результат solve(...)
  """

  for i, sol in enumerate(solutions):
    print(f"Проверка решения {i}: {sol}")

    ok = True

    for eq in system:
      lhs_tmp = ""
      rhs_tmp = ""
      try:
        lhs_tmp = eq.lhs().simplify_full()
        rhs_tmp = eq.rhs().simplify_full()
        # Подставляем решение в левую и правую части
        lhs_val = lhs_tmp.subs(sol)
        rhs_val = rhs_tmp.subs(sol)
      except ValueError  as error:
        print(error)
        print(" lhs:", lhs_tmp)
        print(" rhs:", rhs_tmp)
        print(" sol:", sol)
        ok = False
        break

      # Проверяем равенство
      diff = (lhs_val - rhs_val).simplify_full()

      if diff != 0:
        ok = False
        print(f"  Не выполнено: {eq}")
        print(f"    левая часть  = {lhs_val}")
        print(f"    правая часть = {rhs_val}")
        print(f"    разность     = {diff}")
      else:
        print(f"  Выполнено: {eq}")

    if ok:
      print("  Это решение подходит")
    #else:
    #  print("  Это решение НЕ подходит")


z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)

T = sort_triangulation({z_1,z_3,z_4}, {z_1,z_5,z_6}, {z_1,z_2,z_6}, {z_1,z_4,z_5}, {z_2,z_3,z_4}, {z_2,z_4,z_5}, {z_2,z_5,z_6})

edges_init = make_init_vars_for_edges(T)

edges_vars = [edges_init[k] for k in edges_init.keys()]
for i in range(len(edges_vars) - 1):
  var_1 = edges_vars[i]
  var_2 = edges_vars[i+1]
  assume(var_1 < var_2)
  print(var_1, '<', var_2)

print('######  edges init  ######')
show(edges_init)


##################################
##### trefoil on 3 strands #######
##################################
t, edges_result = braiding(T, edges_init,
                           {z_2,z_5},{z_1,z_6},{z_2,z_4},{z_5,z_6},{z_3,z_4},
                           {z_2,z_4},{z_1,z_5},{z_2,z_6},{z_5,z_4},{z_3,z_6})

edges_result_subs = make_subs_dict_for_edges(edges_init, edges_result)

print()
print('######  edges result for trefoil  ######')
show(edges_result)
show(edges_result_subs)

trefoil_eqs, solver_variables = eqs_and_vars(edges_init, edges_result, edges_changed={
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
  }, exclude=False)

print()
trefoil_resolved = resolve_eqs(trefoil_eqs, solver_variables)
# resolve_eqs(trefoil_eqs, tuple([l_var for l_var in solver_variables if (str(l_var) != 'l_1' and str(l_var) != 'l_2' and str(l_var) != 'l_6')]))

check_solutions(trefoil_eqs, trefoil_resolved)

################################
##### Conjugated trefoil #######
################################

t, edges_result = braiding(T, edges_init,
                           {z_2,z_5},{z_1,z_4},{z_5,z_6},{z_3,z_4},
                           {z_2,z_4},{z_1,z_6},{z_2,z_5},{z_4,z_6},{z_3,z_5},
                           {z_2,z_5},{z_1,z_4},{z_2,z_6},{z_4,z_5},{z_3,z_6},
                           {z_1,z_6},{z_2,z_4},{z_5,z_6},{z_3,z_4})

edges_result_subs = make_subs_dict_for_edges(edges_init, edges_result)

print()
print('######  edges result conjugated trefoil ######')
show(edges_result)
show(edges_result_subs)

print()
print("###### close trefoil and resolve equation system #######")
conjugated_trefoil_eqs, solver_variables = eqs_and_vars(edges_init, edges_result, edges_changed={
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
  }, exclude=False)

print()
# resolve_eqs(conjugated_trefoil_eqs, solver_variables)
conjugated_trefoil_resolved = resolve_eqs(conjugated_trefoil_eqs, tuple([l_var for l_var in solver_variables if (str(l_var) != 'l_1' and str(l_var) != 'l_2' and str(l_var) != 'l_6')]))
check_solutions(conjugated_trefoil_eqs, conjugated_trefoil_resolved)

print()
print("###### equation system -- trefoil, result -- conjugated trefoil ######")
check_solutions(trefoil_eqs, conjugated_trefoil_resolved)
print()
print("###### equation system -- conjugated trefoil, result -- trefoil ######")
check_solutions(conjugated_trefoil_eqs, trefoil_resolved)

exit()


print('######  edges result  simplified ######')
edges_result_simplified = {}
for e, k in edges_result.items():
  edges_result_simplified[e] = edges_result[e].simplify_full()

show(edges_result_simplified)

print('###### edges result ######')
show(edges_result_subs)

