from sage.all import *

t = var('t')

n = matrix(SR, [0, t, -t**(-1), 0])
show(n)
print("")

u = matrix(SR, [0, -t, t**(-1), 0]).transpose()
show(u)
print("")

nu = n*u
print("nu")
show(nu[0][0].simplify_full())
print("")


R = matrix(SR, [
  [t,0,0,0],
  [0,0,t**(-1),0],
  [0,t**(-1),t-t**(-3),0],
  [0,0,0,t]
])
# show(R)

idv = matrix(SR, [[1,0],[0,1]])


print('trefoil')
a_0 = u
a_1 = idv.tensor_product(idv.tensor_product(u))
a_2 = idv.tensor_product(R.inverse().tensor_product(idv))
a_3 = R.tensor_product(idv.tensor_product(idv))
a_4 = idv.tensor_product(R.inverse().tensor_product(idv))
a_5 = idv.tensor_product(idv.tensor_product(n))
a_6 = n

# m = a_0*a_1*a_2*a_3*a_4*a_5*a_6
m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
# m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m = m.simplify_full()

show(m)


print('opposit trefoil')
a_0 = u
a_1 = idv.tensor_product(idv.tensor_product(u))
a_2 = idv.tensor_product(R.tensor_product(idv))
a_3 = R.inverse().tensor_product(idv.tensor_product(idv))
a_4 = idv.tensor_product(R.tensor_product(idv))
a_5 = idv.tensor_product(idv.tensor_product(n))
a_6 = n

m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
# m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m = m.simplify_full()

show(m)


print('trivial')
a_0 = u
a_1 = idv.tensor_product(idv.tensor_product(u))
a_2 = idv.tensor_product(R.inverse().tensor_product(idv))
a_3 = R.tensor_product(idv.tensor_product(idv))
a_4 = idv.tensor_product(R.tensor_product(idv))
a_5 = idv.tensor_product(idv.tensor_product(n))
a_6 = n

m = a_6*a_5*a_4*a_3*a_2*a_1*a_0
# m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m = m.simplify_full()

show(m)