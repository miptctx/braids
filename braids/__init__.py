from sage.all import *
from braids.prints import basis2str


def _show(*args):
  # show(latex(*args))
  show(*args)


def map(in_basis:tuple, diagonal:set, F=QQ):
  # detect quadrate in which the flip happened and triangles
  left_right_triangles = set()
  quadrate = set(diagonal)
  for triangle in in_basis:
    if len(triangle & diagonal) == 2:
      quadrate |= triangle
      left_right_triangles.add(frozenset(triangle))

  # print(quadrate)
  assert len(quadrate) == 4
  assert len(left_right_triangles) == 2

  # this helper function fixes formulas for different types of rectangles
  def helper(quadrate:set, diag:set, triangles:set):
    assert len(quadrate)  == 4
    assert len(diag)      == 2
    assert len(triangles) == 2

    p_i, p_k = tuple(diag)
    p_i, p_k = (p_i, p_k) if p_i < p_k else (p_k, p_i)  # consider that point i is the smallest
    assert p_i != p_k

    p_j, p_l = tuple(quadrate - diag)
    p_j, p_l = (p_j, p_l) if p_j < p_l else (p_l, p_j)  # consider that point j is the smallest

    t_left, t_right = tuple(triangles)
    t_left, t_right = (t_left, t_right) if p_j in t_left else (t_right, t_left)
    assert p_j in t_left and p_l in t_right

    t_up, t_down = (quadrate - {p_k}, quadrate - {p_i})
    assert p_i in t_up and p_k in t_down

    assert \
      t_left != t_right and t_left != t_up and t_left != t_down and \
      t_right != t_up and t_right != t_down and \
      t_up != t_down

    def make_matrix(p_i, p_k, p_j, p_l):
      image_left  = vector(F, [(p_i-p_l)/(p_i-p_k), (p_l-p_k)/(p_i-p_k)])
      image_right = vector(F, [(p_i-p_j)/(p_i-p_k), (p_j-p_k)/(p_i-p_k)])
      return matrix(F, [image_left, image_right]).transpose()

    matrix_ikjl = make_matrix(p_i, p_k, p_j, p_l)  # A_{ikjl} matrix
    matrix_jlik = make_matrix(p_j, p_l, p_i, p_k)  # A_{jlik} matrix

    assert matrix_ikjl == matrix_jlik.inverse()   # relation (1)

    map_matrix = matrix_ikjl

    # coordinates of the basis vector images
    image_left  = vector(F, [map_matrix[0][0], map_matrix[1][0]])
    image_right = vector(F, [map_matrix[0][1], map_matrix[1][1]])

    return t_left, t_right, t_up, t_down, image_left, image_right

  t_left, t_right, t_up, t_down, image_left, image_right = helper(quadrate, diagonal, left_right_triangles)

  t_left_index  = in_basis.index(t_left)
  t_right_index = in_basis.index(t_right)

  assert t_left_index != t_right_index

  out_basis =  \
    list(in_basis[:t_left_index])  + [t_up]   + list(in_basis[t_left_index+1:t_right_index]) + [t_down] + list(in_basis[t_right_index+1:]) if t_left_index < t_right_index else \
    list(in_basis[:t_right_index]) + [t_down] + list(in_basis[t_right_index+1:t_left_index]) + [t_up]   + list(in_basis[t_left_index+1:])

  vectors_images = []
  for i in range(len(out_basis)):
    image = [0]*(len(out_basis))
    if out_basis[i] in in_basis:
      image[i] = 1

    vectors_images.append(image)

  vectors_images[t_left_index ][t_left_index ] = image_left[0]
  vectors_images[t_left_index ][t_right_index] = image_left[1]
  vectors_images[t_right_index][t_left_index ] = image_right[0]
  vectors_images[t_right_index][t_right_index] = image_right[1]

  # indices = sorted(range(len(out_basis)), key=lambda i: tuple(sorted(out_basis[i], key=lambda s: str(s))))
  indices = sorted(range(len(out_basis)), key=lambda i: "".join([str(x) for x in sorted(out_basis[i], key=lambda s: str(s))]))

  out_basis = [out_basis[i] for i in indices]

  map_matrix = []
  for i in range(len(vectors_images)):
    map_matrix.append([vectors_images[i][j] for j in indices])

  map_matrix = matrix(F, map_matrix).transpose()

  # print(basis2str(in_basis), '-->', basis2str(out_basis))
  # _show(map_matrix)
  # print("")

  return tuple(out_basis), map_matrix


def braiding(in_basis:tuple, *diagonals, F=QQ):
  maps_matrix = identity_matrix(F, len(in_basis))
  for diagonal in diagonals:
    t, m = map(in_basis, set(diagonal), F=F)
    in_basis = t
    maps_matrix = m * maps_matrix

  return in_basis, maps_matrix


def knotting_max(in_basis:tuple, triangle:set, p_4, F=QQ, param=1, vars=None):
  p_1, p_2, p_3 = tuple(sorted(triangle))

  t_124 = {p_1, p_2, p_4}
  t_234 = {p_2, p_3, p_4}
  t_134 = {p_1, p_3, p_4}

  t_index = in_basis.index(triangle)

  out_basis = list(in_basis[:t_index]) + [t_124] + list(in_basis[t_index+1:]) + [t_234, t_134]

  vectors_images = []
  for i in range(len(in_basis)):
    image = [0]*(len(out_basis))
    if out_basis[i] in in_basis:
      image[i] = 1

    vectors_images.append(image)

  vectors_images[t_index][out_basis.index(t_124)] = param * ( (-p_1*p_3/(p_1*p_2-p_2*p_2-p_1*p_3+p_2*p_3) ) if vars is None else vars[0])
  vectors_images[t_index][out_basis.index(t_234)] = param * ( ( p_1*p_2/(p_1*p_2-p_1*p_3-p_2*p_3+p_3*p_3) ) if vars is None else vars[1])
  vectors_images[t_index][out_basis.index(t_134)] = param * ( ( p_2*p_3/(p_1*p_1-p_1*p_2-p_1*p_3+p_2*p_3) ) if vars is None else vars[2])

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


def knotting_min(in_basis:tuple, p_4, F=QQ, param=1, vars=None):
  triangle = set()
  for vect in in_basis:
    if p_4 in vect:
      triangle |= vect
  
  assert len(triangle) == 4

  t_123 = set(triangle - {p_4})

  p_1, p_2, p_3 = tuple(sorted(t_123))

  t_124 = triangle - {p_3}
  t_234 = triangle - {p_1}
  t_134 = triangle - {p_2}

  t_124_index = in_basis.index(t_124)
  t_234_index = in_basis.index(t_234)
  t_134_index = in_basis.index(t_134)

  out_basis = list(in_basis)
  out_basis.remove(t_124)
  out_basis.remove(t_234)
  out_basis.remove(t_134)
  out_basis.append(t_123)

  vectors_images = []
  for in_vect in in_basis:
    image = [0]*(len(out_basis))
    if in_vect in out_basis:
      image[out_basis.index(in_vect)] = 1

    vectors_images.append(image)

  vectors_images[t_124_index][out_basis.index(t_123)] = param if vars is None else vars[0]
  vectors_images[t_234_index][out_basis.index(t_123)] = param if vars is None else vars[1]
  vectors_images[t_134_index][out_basis.index(t_123)] = param if vars is None else vars[2]

  indices = sorted(range(len(out_basis)), key=lambda i: tuple(sorted(out_basis[i])))

  out_basis = [out_basis[i] for i in indices]

  map_matrix = []
  for i in range(len(vectors_images)):
    map_matrix.append([vectors_images[i][j] for j in indices])

  map_matrix = matrix(F, map_matrix).transpose()

  # print(basis2str(in_basis), '=', basis2str(out_basis))
  # _show(map_matrix)
  # print("")

  return tuple(out_basis), map_matrix
