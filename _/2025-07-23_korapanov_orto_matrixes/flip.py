from sage.all import *

z_1 = 4
z_2 = 5
z_3 = 3
z_4 = 1


def cos_f(i, j, k, l):
  tmp = ((i-l)*(j-k)) / ((i-k)*(j-l))
  return sqrt(complex(tmp) if F==CC else tmp)

def sin_f(i, j, k, l):
  tmp = ((i-j)*(k-l)) / ((i-k)*(j-l))
  return sqrt(complex(tmp) if F==CC else tmp)


cos_1 = cos_f()