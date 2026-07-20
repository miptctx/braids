# This is trefoil on 2 strands

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

'''
PR = PolynomialRing(QQ, 't_125,t_134,t_145,t_234,t_245')
PR.inject_variables()

F = PR.fraction_field()
'''

t_127,t_134,t_145,t_156,t_167,t_234,t_245,t_256,t_267 = var("t_127,t_134,t_145,t_156,t_167,t_234,t_245,t_256,t_267")

F = QQ

T = sort_triangulation({1,2,7},{1,4,5},{1,3,4},{1,5,6},{1,6,7},{2,3,4},{2,4,5},{2,5,6},{2,6,7})

t, m = braiding(T,
                (2,5),(1,6),(6,7),(4,5), (2,6),(1,4),(5,6),(3,4),
                (2,4),(1,5),(4,6),(5,7),
                (2,5),(1,6),(4,5),(3,6),
                (2,4),(1,7),(4,6), # markov movement
                F=F)

print("Result matrix")
print_triangles_pretty(T)
print_triangles_pretty(t)
show(m)

print("Det: ", m.det())
print("Trace: ", m.trace())
print("Charpoly: ", m.charpoly())
print("Eigenvalues: ", m.eigenvalues())

basis = vector([t_127,t_134,t_145,t_156,t_167,t_234,t_245,t_256,t_267])

# basis_image = vector([t_127,t_134,t_145,t_156,t_167,t_234,t_245,t_256,t_267])

image = basis*m

print("Image")
show(image)


eqs = [
  basis[0] == image[0],
  basis[1] == image[1],
  basis[2] == image[2],
  basis[3] == image[3],
  basis[4] == image[4],
  basis[5] == image[5],
  basis[6] == image[6],
  basis[7] == image[7],
  basis[8] == image[8],
]

print("Eqs")
show(eqs)

res = solve(eqs, t_127,t_134,t_145,t_156,t_167,t_234,t_245,t_256,t_267)

show(res)

# res = m.solve_right(vector([1,1,1,1,1,1,1]))
# show(res)

# res = m.transpose().solve_right(vector([1,1,1,1,1,1,1]))
# show(res)
