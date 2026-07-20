from sage.all import *
from braids.prints import basis2str


def _show(*args):
  # show(latex(*args))
  show(*args)


def map(in_basis:tuple, diagonal:set, F=QQ, i_cos=0, i_sin=0, parity=False, z_sign=False, sum_parity=False, p_k_p_l=False, cos_f=None, sin_f=None):
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

    '''
    # p_i = min(quadrate)
    p_i = max(quadrate)
    p_k = tuple(((diag if p_i in diag else (quadrate - diag))) - {p_i})[0]
    # p_j = min(quadrate - {p_i, p_k})
    p_j = max(quadrate - {p_i, p_k})
    # p_l = max(quadrate - {p_i, p_k})
    p_l = min(quadrate - {p_i, p_k})
    '''

    p_i = min(quadrate)
    p_k = max(diag if p_i in diag else (quadrate - diag))
    p_j = min(quadrate - {p_i, p_k})
    p_l = max(quadrate - {p_i, p_k})

    print(p_i, p_j, p_k, p_l, "---- k > l" if p_k > p_l else "")
    assert len({p_i, p_j, p_k, p_l}) == 4

    t_left, t_right, t_up, t_down = (quadrate - {p_l}, quadrate - {p_j}, quadrate - {p_k}, quadrate - {p_i}) if p_i in diag else \
                                    (quadrate - {p_k}, quadrate - {p_i}, quadrate - {p_l}, quadrate - {p_j})

    # p_i, p_j, p_k, p_l = tuple(sorted(quadrate))
    # print("quadrate: ", p_i, p_j, p_k, p_l)

    assert \
      t_left != t_right and t_left != t_up and t_left != t_down and \
      t_right != t_up and t_right != t_down and \
      t_up != t_down

    assert t_left in triangles and t_right in triangles

    def zeta_cos(i, j, k, l):
      unit = 1
      #if l > k:
      #  k, l = l, k
        #unit = -1
      #if j < k:
        #return ((i-l)*(k-j)) / ((i-k)*(j-l))
        #j, k = k, j
        #unit = -1

      return unit*((i-l)*(j-k)) / ((i-k)*(j-l))

    def zeta_sin(i, j, k, l):
      unit = 1
      #if l > k:
        #return ((i-j)*(l-k)) / ((i-k)*(j-l))
        # k, l = l, k
        #unit = -1
      #elif j < k:
      #  j, k = k, j
      #  #unit = -1

      return unit*((i-j)*(k-l)) / ((i-k)*(j-l))

    #def make_matrix(p_i, p_k, p_j, p_l):
    #  image_left  = vector(F, [(p_i-p_l)/(p_i-p_k), (p_l-p_k)/(p_i-p_k)])
    #  image_right = vector(F, [(p_i-p_j)/(p_i-p_k), (p_j-p_k)/(p_i-p_k)])
    #  return matrix(F, [image_left, image_right]).transpose()

    def _cos_f(i, j, k, l):
      # i_cos = (-1 if (i < k < j < l) else 1) if i_cos is None else i_cos
      # i_cos = (-1 if (i < k < j < l) else 1)
      zeta = zeta_cos(i, j, k, l) #((i-l)*(j-k)) / ((i-k)*(j-l))
      # zeta = ( ((i-l)*(j-k)) / ((i-k)*(j-l)) ) * (1 if ((i+k) < (j+l)) else -1)
      return ((-1)**i_cos)*abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)
      # return ((-1)**i_cos)*abs(sqrt(abs(zeta))) * ((-1) if zeta < 0 else 1)
      # return abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)
      # return sqrt(complex(tmp) if F==CC else tmp)
      # return ((-1)**i_cos)*sqrt(complex(tmp) if F==CC else tmp)
      # return sqrt(complex(tmp) if (F==CC or F==SR) else tmp)
      # return sqrt(complex(tmp))
      # return ((-1)**sgn(tmp))*sqrt(complex(tmp) if F==CC else tmp)
      # return ((-1)**(i+j+k+l))*sqrt(complex(tmp) if F==CC else tmp)
      # return sqrt(abs(tmp))

    def _sin_f(i, j, k, l):
      # i_sin = (-1 if (i < j < l < k) else 1) if i_sin is None else i_sin
      # i_sin = (-1 if (i < j < l < k) else 1)
      zeta = zeta_sin(i, j, k, l) # ((i-j)*(k-l)) / ((i-k)*(j-l))
      # zeta = ((i-j)*(k-l)) / ((i-k)*(j-l)) * (1 if ((i+k) < (j+l)) else -1)
      return ((-1)**i_sin)*abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)
      # return ((-1)**i_sin)*abs(sqrt(abs(zeta))) * ((-1) if zeta < 0 else 1)
      # return (-1)*abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)
      # return sqrt(complex(tmp) if F==CC else tmp)
      # return ((-1)**i_sin)*sqrt(complex(tmp) if F==CC else tmp)
      # return sqrt(complex(tmp) if (F==CC or F==SR) else tmp)
      # return sqrt(complex(tmp))
      # return ((-1)**sgn(tmp))*sqrt(complex(tmp) if F==CC else tmp)
      # return ((-1)**(i+j+k+l))*sqrt(complex(tmp) if F==CC else tmp)
      # return sqrt(abs(tmp))

    root_c = cos_f if cos_f else _cos_f
    root_s = sin_f if sin_f else _sin_f

    def f_dir(i,j,k,l):
      return matrix(F, [
        [ root_c(i,j,k,l), root_s(i,j,k,l)],
        [-1*root_s(i,j,k,l), root_c(i,j,k,l)]
      ])

    def f_inv(i,j,k,l):
      return matrix(F, [
        [root_c(i,j,k,l), -1*root_s(i,j,k,l)],
        [root_s(i,j,k,l),  root_c(i,j,k,l)]
      ])

    # matrix_ikjl = make_matrix(p_i, p_k, p_j, p_l)  # A_{ikjl} matrix
    # matrix_jlik = make_matrix(p_j, p_l, p_i, p_k)  # A_{jlik} matrix

    # print("i=", p_i, ", j=", p_j, ", k=", p_k, ", l=", p_l)

    matrix_ikjl = f_dir(p_i, p_j, p_k, p_l)  # direct flip
    matrix_jlik = f_inv(p_i, p_j, p_k, p_l)  # inverse flip

    # assert matrix_ikjl == matrix_jlik.inverse()   # relation (1)
    relation_1_product = (matrix_ikjl * matrix_jlik)
    if F==CC:
      relation_1_product = relation_1_product.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
    # print(relation_1_product)
    # assert relation_1_product == matrix(F, [[1,0],[0,1]])   # relation (1)

    # print("p_i < p_j: ", p_i < p_j)
    # map_matrix = matrix_ikjl if p_i < p_j else matrix_jlik
    # map_matrix = matrix_ikjl if p_i not in diag else matrix_jlik
    map_matrix = matrix_ikjl if p_i in diag else matrix_jlik

    if parity:
      parity_major = (p_j + p_l) % 2
      parity_minor = (p_i + p_k) % 2
      print("parity: ", parity_major, parity_minor)
    
    if z_sign:
      zc = zeta_cos(p_i, p_j, p_k, p_l)
      zs = zeta_sin(p_i, p_j, p_k, p_l)
      print("z_sign: ", "-" if zc < 0 else "+", "-" if zs < 0 else "+")

    if sum_parity:
      print("sum_parity: ", (p_i + p_j + p_k + p_l) % 2)

    if p_k_p_l:
      zc = zeta_cos(p_i, p_j, p_k, p_l)
      zs = zeta_sin(p_i, p_j, p_k, p_l)
      print("p_j > p_k:" , 0 if p_j > p_k else 1, \
            "    p_k > p_l:", 0 if p_k > p_l else 1, \
            "    direction:", 0 if (p_i not in diag) else 1, \
            "    sum_parity: ", (p_i + p_j + p_k + p_l) % 2, \
            "    z_sign: ", "-" if zc < 0 else "+", "-" if zs < 0 else "+")

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

  '''
  print(basis2str(in_basis), '-->', basis2str(out_basis))
  _show(map_matrix.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I) if F==CC else map_matrix)
  print("")
  '''

  return tuple(out_basis), map_matrix


def braiding(in_basis:tuple, *diagonals, F=CC, **kwargs):
  maps_matrix = identity_matrix(F, len(in_basis))
  for diagonal in diagonals:
    t, m = map(in_basis, set(diagonal), F=F, **kwargs)
    #show(m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
    #print("")
    # show(latex(m))
    in_basis = t
    maps_matrix = m * maps_matrix

  return in_basis, maps_matrix




def map_ext(in_basis:tuple, quadril:tuple, diagonal:set, F=QQ, i_cos=0, i_sin=0, parity=False, z_sign=False, sum_parity=False, p_k_p_l=False, cos_f=None, sin_f=None):
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

  # print("Flip", diagonal, " --> ", quadrate - diagonal)

  # this helper function fixes formulas for different types of rectangles
  def helper(quadrate:set, diag:set, triangles:set):
    assert len(quadrate)  == 4
    assert len(diag)      == 2
    assert len(triangles) == 2

    p_i = min(quadrate)
    p_k = max(diag if p_i in diag else (quadrate - diag))
    p_j = min(quadrate - {p_i, p_k})
    p_l = max(quadrate - {p_i, p_k})

    # print(p_i, p_j, p_k, p_l, "---- k > l" if p_k > p_l else "")
    assert len({p_i, p_j, p_k, p_l}) == 4

    t_left, t_right, t_up, t_down = (quadrate - {p_l}, quadrate - {p_j}, quadrate - {p_k}, quadrate - {p_i}) if p_i in diag else \
                                    (quadrate - {p_k}, quadrate - {p_i}, quadrate - {p_l}, quadrate - {p_j})

    # p_i, p_j, p_k, p_l = tuple(sorted(quadrate))
    # print("quadrate: ", p_i, p_j, p_k, p_l)

    assert \
      t_left != t_right and t_left != t_up and t_left != t_down and \
      t_right != t_up and t_right != t_down and \
      t_up != t_down

    assert t_left in triangles and t_right in triangles

    def zeta_cos_enum(i,j,k,l):
      return (i-l)*(j-k)

    def zeta_cos_denum(i,j,k,l):
      return (i-k)*(j-l)

    def zeta_cos(i, j, k, l):
      return (zeta_cos_enum(i,j,k,l))/(zeta_cos_denum(i,j,k,l))
      # return ((i-l)*(j-k)) / ((i-k)*(j-l))

    def zeta_sin_enum(i,j,k,l):
      return (i-j)*(k-l)

    def zeta_sin_denum(i,j,k,l):
      return (i-k)*(j-l)

    def zeta_sin(i, j, k, l):
      return (zeta_sin_enum(i,j,k,l))/(zeta_sin_denum(i,j,k,l))
      # return ((i-j)*(k-l)) / ((i-k)*(j-l))

    p_1, p_2, p_3, p_4 = quadril
    assert p_1 == p_i
    assert p_3 == p_k
    assert set(quadril) == quadrate
    # print("quadrilaterial:", p_1, p_2, p_3, p_4, "flip:", f"{diag} --> {quadrate-diag}")

    def _cos_f(i, j, k, l):
      sign = -1 if ((p_2 > p_3) and (p_2 < p_4)) else 1
      zeta = zeta_cos(i, j, k, l) #((i-l)*(j-k)) / ((i-k)*(j-l))
      return sign*( (abs(zeta_cos_enum(i,j,k,l))**(1/2))/(abs(zeta_cos_denum(i,j,k,l))**(1/2)) ) * ((1*I) if zeta < 0 else 1)
      # return sign*((-1)**i_cos)*abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)
      # return sign*sqrt(zeta)

    def _sin_f(i, j, k, l):
      sign = -1 if ((p_4 > p_2) and (p_4 < p_3)) else 1
      zeta = zeta_sin(i, j, k, l) # ((i-j)*(k-l)) / ((i-k)*(j-l))
      return sign*( (abs(zeta_sin_enum(i,j,k,l))**(1/2))/(abs(zeta_sin_denum(i,j,k,l))**(1/2)) ) * ((1*I) if zeta < 0 else 1)
      # return sign*((-1)**i_sin)*abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)
      # return sign*sqrt(zeta)

    root_c = cos_f if cos_f else _cos_f
    root_s = sin_f if sin_f else _sin_f

    def f_dir(i,j,k,l):
    # def f_inv(i,j,k,l):
      return matrix(F, [
        [ root_c(i,j,k,l), root_s(i,j,k,l)],
        [-1*root_s(i,j,k,l), root_c(i,j,k,l)]
      ])

    def f_inv(i,j,k,l):
    # def f_dir(i,j,k,l):
      return matrix(F, [
        [root_c(i,j,k,l), -1*root_s(i,j,k,l)],
        [root_s(i,j,k,l),  root_c(i,j,k,l)]
      ])

    matrix_ikjl = f_dir(p_i, p_j, p_k, p_l)  # direct flip
    matrix_jlik = f_inv(p_i, p_j, p_k, p_l)  # inverse flip

    # assert matrix_ikjl == matrix_jlik.inverse()   # relation (1)
    relation_1_product = (matrix_ikjl * matrix_jlik)
    if F==CC:
      relation_1_product = relation_1_product.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
      assert relation_1_product == matrix(F, [[1,0],[0,1]])   # relation (1)

    map_matrix = matrix_ikjl if p_i in diag else matrix_jlik

    # coordinates of the basis vector images
    image_left  = vector(F, [map_matrix[0][0], map_matrix[1][0]])
    image_right = vector(F, [map_matrix[0][1], map_matrix[1][1]])

    return t_left, t_right, t_up, t_down, image_left, image_right

  t_left, t_right, t_up, t_down, image_left, image_right = helper(quadrate, diagonal, left_right_triangles)

  t_left_index  = in_basis.index(t_left)
  t_right_index = in_basis.index(t_right)

  assert t_left_index != t_right_index
  assert t_left_index < t_right_index   # This must be satisfied all the time

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
  #indices = sorted(range(len(out_basis)), key=lambda i: "".join(
  #  [str(triangle) for triangle in sorted(out_basis[i], key=lambda point: str(point))]
  #))
  indices = sorted(range(len(out_basis)), key=lambda i: tuple(
    [triangle for triangle in tuple(sorted(out_basis[i], key=lambda point: point))]
  ))


  out_basis = [out_basis[i] for i in indices]

  map_matrix = []
  for i in range(len(vectors_images)):
    map_matrix.append([vectors_images[i][j] for j in indices])

  map_matrix = matrix(F, map_matrix).transpose()

  '''
  print(basis2str(in_basis), '-->', basis2str(out_basis))
  _show(map_matrix.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I) if F==CC else map_matrix)
  print("")
  '''

  return tuple(out_basis), map_matrix


def braiding_ext(in_basis:tuple, *diagonals, F=CC, **kwargs):
  maps_matrix = identity_matrix(F, len(in_basis))
  for component in diagonals:
    quadril, diag = component
    t, m = map_ext(in_basis, quadril, set(diag), F=F, **kwargs)
    # show(m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
    # show(latex(m.apply_map(lambda x: round(x.real(), 8) + round(x.imag(), 8) * I)))
    # print("")
    in_basis = t
    maps_matrix = m * maps_matrix

  return in_basis, maps_matrix

