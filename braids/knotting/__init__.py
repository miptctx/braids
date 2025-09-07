from sage.all import *
from braids.prints import basis2str


def _show(*args):
  # show(latex(*args))
  show(*args)


def knotting_max(in_basis:tuple, triangle_1:set, p_5, triangle_2:set, p_6, F=QQ, param=1, vars=None):
  # find the less 3 points
  all_points = set()
  for t in in_basis:
    all_points |= t

  all_points = sorted(tuple(all_points))
  assert len(all_points) >= 3
  p_l_1, p_l_2, p_l_3 = all_points[0], all_points[1], all_points[2]
  assert (p_l_1 < p_l_2) and (p_l_2 < p_l_3)
  triangle_outer = {p_l_1, p_l_2, p_l_3}

  diagonal = triangle_1 & triangle_2
  assert len(diagonal) == 2

  p_1, p_4 = tuple(diagonal)
  p_1, p_4 = (p_1, p_4) if (p_1 < p_4) else (p_4, p_1)

  is_diagonal_major = True
  if not diagonal.issubset(triangle_outer):     # we consider that initial points are 1,2,3; in this case the edge of the triangle 1,2,3 is always a major diagonal
    triangles_have_diagonal = []
    for t in in_basis:
      if diagonal.issubset(t):
        triangles_have_diagonal.append(t)

    assert len(triangles_have_diagonal) == 2
    assert triangles_have_diagonal[0] != triangles_have_diagonal[1]
    assert triangles_have_diagonal[0] == triangle_1 or triangles_have_diagonal[1] == triangle_1

    t_1, t_2 = tuple(triangles_have_diagonal)
    _p = (t_1 - diagonal) if (t_1 != triangle_1) else (t_2 - diagonal)
    assert len(_p) == 1
    _p = _p.pop()
    is_diagonal_major = (p_1 < _p) and (p_1 < p_6)

  a_1 = 0 # --> 136, 125
  a_2 = 0 # --> 346, 245,  346, 245
  a_3 = 0 # -->    ,    ,  136, 125

  if is_diagonal_major:
    a_1 = (p_1 - p_5)/(p_1 - p_4)
    a_2 = (p_4 - p_5)/(p_4 - p_1)
  else:
    a_2 = (p_4 - p_5)/(p_4 - p_1)
    a_3 = (p_1 - p_5)/(p_1 - p_4)

  t_a_1 = (triangle_1 - diagonal) | {p_1, p_5}
  t_a_2 = (triangle_1 - diagonal) | {p_4, p_5}
  assert len(t_a_1) == 3
  assert len(t_a_2) == 3


  t_b_1 = diagonal | {p_6}
  t_b_2 = {p_1, p_5, p_6}
  t_b_3 = {p_4, p_5, p_6}

  t_index = in_basis.index(triangle_1)

  out_basis = list(in_basis[:t_index]) + [t_a_1] + list(in_basis[t_index+1:]) + [t_a_2] + [t_b_1, t_b_2, t_b_3]

  vectors_images = []
  for i in range(len(in_basis)):
    image = [0]*(len(out_basis))
    if out_basis[i] in in_basis:
      image[i] = 1

    vectors_images.append(image)

  vectors_images[t_index][out_basis.index(t_a_1)] = param * ( (a_1 if is_diagonal_major else a_3) if vars is None else vars[0] )
  vectors_images[t_index][out_basis.index(t_a_2)] = param * (  a_2 if vars is None else vars[0] )
  vectors_images[t_index][out_basis.index(t_b_1)] = param * (    0 if vars is None else vars[0] )
  vectors_images[t_index][out_basis.index(t_b_2)] = param * (    0 if vars is None else vars[0] )
  vectors_images[t_index][out_basis.index(t_b_3)] = param * (    0 if vars is None else vars[0] )

  indices = sorted(range(len(out_basis)), key=lambda i: tuple(sorted(out_basis[i])))

  out_basis = [out_basis[i] for i in indices]

  map_matrix = []
  for i in range(len(vectors_images)):
    map_matrix.append([vectors_images[i][j] for j in indices])

  map_matrix = matrix(F, map_matrix).transpose()

  # print(basis2str(in_basis), '-->', basis2str(out_basis))
  # _show(map_matrix)
  # print("")

  return tuple(out_basis), map_matrix


# p_5 dissapears first, then p_6
def knotting_min(in_basis:tuple, p_5, p_6, F=QQ, param=1, vars=None):

  t_around_p_5 = set()
  t_around_p_6 = set()

  for t in in_basis:
    if {p_5}.issubset(t):
      t_around_p_5 |= t
    if {p_6}.issubset(t):
      t_around_p_6 |= t

  t_around_p_5 -= {p_5}
  t_around_p_6 -= {p_5, p_6}
  assert len(t_around_p_6) == 3
  assert len(t_around_p_5) == 3

  p_root = t_around_p_6 - t_around_p_5
  assert len(p_root) == 1
  p_root = p_root.pop()

  p_1, p_4 = tuple(t_around_p_6 - {p_root})
  p_1, p_4 = (p_1, p_4) if (p_1 < p_4) else (p_4, p_1)

  a_1 = (p_root - p_4)/(p_root - p_6)
  a_2 = (p_root - p_1)/(p_root - p_6)

  t_a_1 = {p_1, p_root, p_6}
  t_a_2 = {p_4, p_root, p_6}

  t_145 = {p_1, p_4, p_5}
  t_156 = {p_1, p_5, p_6}
  t_456 = {p_4, p_5, p_6}

  t_final = {p_1, p_4, p_root}

  t_a_1_index = in_basis.index(t_a_1)
  t_a_2_index = in_basis.index(t_a_2)
  t_145_index = in_basis.index(t_145)
  t_156_index = in_basis.index(t_156)
  t_456_index = in_basis.index(t_456)

  out_basis = list(in_basis)
  out_basis.remove(t_a_1)
  out_basis.remove(t_a_2)
  out_basis.remove(t_145)
  out_basis.remove(t_156)
  out_basis.remove(t_456)
  out_basis.append(t_final)

  vectors_images = []
  for in_vect in in_basis:
    image = [0]*(len(out_basis))
    if in_vect in out_basis:
      image[out_basis.index(in_vect)] = 1

    vectors_images.append(image)

  vectors_images[t_a_1_index][out_basis.index(t_final)] = (param*a_1) if vars is None else vars[0]
  vectors_images[t_a_2_index][out_basis.index(t_final)] = (param*a_2) if vars is None else vars[1]
  vectors_images[t_145_index][out_basis.index(t_final)] = 0 if vars is None else vars[2]
  vectors_images[t_156_index][out_basis.index(t_final)] = 0 if vars is None else vars[3]
  vectors_images[t_456_index][out_basis.index(t_final)] = 0 if vars is None else vars[4]

  indices = sorted(range(len(out_basis)), key=lambda i: tuple(sorted(out_basis[i])))

  out_basis = [out_basis[i] for i in indices]

  map_matrix = []
  for i in range(len(vectors_images)):
    map_matrix.append([vectors_images[i][j] for j in indices])

  map_matrix = matrix(F, map_matrix).transpose()

  return tuple(out_basis), map_matrix
