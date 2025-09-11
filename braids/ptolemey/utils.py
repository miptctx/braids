from sage.all import var


def make_init_vars_for_edges(basis:tuple):
  points = set()
  for t in basis:
    p_1, p_2, p_3 = tuple(t)
    points.add(p_1)
    points.add(p_2)
    points.add(p_3)

  edges = set()
  for t in basis:
    p_1, p_2, p_3 = tuple(sorted(t))
    edges.add((p_1, p_2))
    edges.add((p_1, p_3))
    edges.add((p_2, p_3))

  assert len(edges) == (len(basis) + 1 + len(points) - 2)   # this formula was given from the eulier characteristic of planar graph: v-e+f=2.

  edges_dict = dict()
  for i, e in enumerate(sorted(edges)):
    l_i = var(f"l_{i+1}")
    edges_dict.update({e: l_i})

  return dict(sorted(edges_dict.items()))


def make_subs_dict_for_edges(init_edges:dict, subs_edges:dict):
  subs_dict = {}
  for i, (k, v) in enumerate(init_edges.items()):
    subs_dict.update({v: i+1})

  result = dict(subs_edges)
  for k, v in subs_edges.items():
    result[k] = result[k].subs(subs_dict)

  return dict(sorted(result.items()))
