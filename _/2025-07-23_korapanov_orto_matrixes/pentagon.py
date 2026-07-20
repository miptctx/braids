from sage.all import *


def cos_f(i, j, k, l):
  return sqrt((i-l)*(j-k)/(i-k)/(j-l))


def sin_f(i, j, k, l):
  return sqrt((i-j)*(k-l)/(i-k)/(j-l))



l_1 = matrix([[1, 0, 0], [0, cos_f(1,3,4,5), sin_f(1,3,4,5)], [0, -sin_f(1,3,4,5), cos_f(1,3,4,5)]])
l_2 = matrix([[cos_f(1,2,3,4), -sin_f(1,2,3,4), 0], [sin_f(1,2,3,4), cos_f(1,2,3,4), 0], [0, 0, 1]])

m_l = l_1*l_2

show(m_l)

print("")

r_1 = matrix([[cos_f(1,2,3,5), -sin_f(1,2,3,5), 0], [sin_f(1,2,3,5), cos_f(1,2,3,5), 0], [0, 0, 1]])
r_2 = matrix([[1, 0, 0], [0, cos_f(2,3,4,5), sin_f(2,3,4,5)], [0, -sin_f(2,3,4,5), cos_f(2,3,4,5)]])
r_3 = matrix([[cos_f(1,2,4,5), 0, sin_f(1,2,4,5)], [0, 1, 0], [-sin_f(1,2,4,5), 0, cos_f(1,2,4,5)]])

m_r = r_1*r_2*r_3

show(m_r)

