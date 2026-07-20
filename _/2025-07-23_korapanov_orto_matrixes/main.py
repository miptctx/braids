from sage.all import *

i,j,k,l = var("i,j,k,l")


def cos_ijkl(i, j, k, l):
  return sqrt((i-l)*(j-k)/(i-k)/(j-l))


def sin_ijkl(i, j, k, l):
  return sqrt((i-j)*(k-l)/(i-k)/(j-l))


cos = cos_ijkl(1,2,3,4)
sin = sin_ijkl(1,2,3,4)


def f_dir(i,j,k,l):
  return matrix([
    [cos_ijkl(i,j,k,l), -sin_ijkl(i,j,k,l)],
    [sin_ijkl(i,j,k,l),  cos_ijkl(i,j,k,l)]
  ])


def f_inv(i,j,k,l):
  return matrix([
    [ cos_ijkl(i,j,k,l), sin_ijkl(i,j,k,l)],
    [-sin_ijkl(i,j,k,l), cos_ijkl(i,j,k,l)]
  ])


# m_1 = f_dir(1,2,3,4)
# m_2 = f_inv(1,2,3,4)

m_1 = f_dir(i, j, k, l)
m_2 = f_inv(i, j, k, l)

m = m_2 * m_1
# m = m_1 * m_2

show(m.simplify_full())
