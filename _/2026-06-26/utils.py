def eqs_and_vars(edges_init, edges_result, edges_changed=dict()):
  eqs = []
  helper_variables = []

  for lhs, rhs in edges_changed.items():
    print(lhs, rhs)
    if edges_result[rhs] != edges_init[lhs]:
      helper_variables.append(edges_init[lhs])
      eqs.append((edges_result[rhs] - edges_init[lhs]).simplify_full() == 0)

  return eqs, tuple(helper_variables)


def resolve_eqs(eqs:list, helper_variables:tuple):
  print("### Resolve equations ###")
  print("variables:", *helper_variables)
  for e in eqs:
    print(e)

  res = solve(eqs, *helper_variables)
  print("### Equation system solutions ###")
  #for i, r in enumerate(res):
  #  print('solution', i)
  #  print(r)
  print(res)
