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

  a = in_edges[tuple(sorted({p_i, p_j}))]
  b = in_edges[tuple(sorted({p_j, p_k}))]
  c = in_edges[tuple(sorted({p_k, p_l}))]
  d = in_edges[tuple(sorted({p_l, p_i}))]
  x = in_edges[edge_old]

  '''
  a = (p_j - p_i) if p_i < p_j else (p_i - p_j) #in_edges[tuple(sorted({p_i, p_j}))]
  b = (p_k - p_j) if p_j < p_k else (p_j - p_k) #in_edges[tuple(sorted({p_j, p_k}))]
  c = (p_k - p_l) if p_l < p_k else (p_l - p_k) #in_edges[tuple(sorted({p_k, p_l}))]
  d = (p_l - p_i) if p_i < p_l else (p_i - p_l) #in_edges[tuple(sorted({p_l, p_i}))]
  x = (p_k - p_i) if p_i < p_k else (p_i - p_k) #in_edges[edge_old]
  '''

  y = (a*c+b*d)/x

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

  in_edges_basis = sorted(in_edges.keys(), key=lambda s: str(tuple(sorted(s))))
  old_edge_idx = in_edges_basis.index(edge_old)
  out_edges_basis = sorted(in_edges_basis[:old_edge_idx] + [edge_new] + in_edges_basis[old_edge_idx+1:], key=lambda s: str(tuple(sorted(s))))
  new_edge_idx = out_edges_basis.index(edge_new)
  # result_matrix = identity_matrix(F, len(out_edges_basis))
  result_matrix =  [[0]*len(out_edges_basis) for _ in range(len(out_edges_basis))]
  result_matrix[new_edge_idx][old_edge_idx] = y
  for col in range(len(out_edges_basis)):
    edge = in_edges_basis[col]
    try:
      row = out_edges_basis.index(edge)
      result_matrix[row][col] = 1
    except ValueError:
      assert col == old_edge_idx
      continue

  return out_basis, dict(sorted(out_edges.items())), matrix(result_matrix)


def braiding(in_basis:tuple, edges:dict, *diagonals, F=QQ):
  maps_matrix = identity_matrix(F, len(edges.keys()))
  for diagonal in diagonals:
    in_basis, edges, m = map(in_basis, edges, set(diagonal))
    show(m)
    maps_matrix = m * maps_matrix
    # maps_matrix = m * maps_matrix

  return in_basis, edges, maps_matrix
