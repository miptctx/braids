from sage.all import *


def _show(*args):
  # show(latex(*args))
  show(*args)


def map(in_basis:tuple, in_edges:dict, diagonal:set, F=QQ):
  # detect quadrate in which the flip happened and triangles
  quadrate = set(diagonal)
  for triangle in in_basis:
    if len(triangle & diagonal) == 2:
      quadrate |= triangle

  assert len(quadrate) == 4

  edge_old = tuple(sorted(diagonal))
  edge_new = tuple(sorted(quadrate - diagonal))

  p_i, p_k = edge_old
  p_j, p_l = edge_new

  a = (in_edges[tuple(sorted({p_i, p_j}))])#**2
  b = (in_edges[tuple(sorted({p_j, p_k}))])#**2
  c = (in_edges[tuple(sorted({p_k, p_l}))])#**2
  d = (in_edges[tuple(sorted({p_l, p_i}))])#**2
  x = (in_edges[edge_old])**2

  # y = (a*c+b*d)/x
  # y = sqrt(a + b + c + d - x + ((a-b)*(c-d))/(x) + sqrt((4*a*b - (a+b-x)**2)*(4*c*d-(c+d-x)**2))/(x))/2
  y = (a + b + c + d - x + ((a-b)*(c-d))/(x) + sqrt((4*a*b - (a+b-x)**2)*(4*c*d-(c+d-x)**2))/(x))/2

  out_edges = dict(in_edges)
  assert edge_old in out_edges
  del out_edges[edge_old]

  assert edge_new not in out_edges
  out_edges[edge_new] = y

  t_old_1 = {p_i, p_k, p_j}
  t_old_2 = {p_i, p_k, p_l}

  t_new_1 = {p_j, p_l, p_i}
  t_new_2 = {p_j, p_l, p_k}

  out_basis = list(in_basis)
  out_basis.remove(t_old_1)
  out_basis.remove(t_old_2)
  out_basis.append(t_new_1)
  out_basis.append(t_new_2)

  out_basis = tuple(sorted(out_basis, key=lambda s: str(tuple(sorted(s)))))

  return out_basis, dict(sorted(out_edges.items()))


def braiding(in_basis:tuple, edges:dict, *diagonals):
  for diagonal in diagonals:
    in_basis, edges = map(in_basis, edges, set(diagonal))

  return in_basis, edges
