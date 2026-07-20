from sage.all import *

i,j,k,l = var("i,j,k,l")

a = i-j
b = j-k
c = k-l
d = i-l

e_sq = ((a*c+b*d)*(a*d+b*c))/(a*b+c*d)
f_sq = ((a*c+b*d)*(a*b+c*d))/(a*d+b*c)

e_simple = e_sq.simplify_full()
f_simple = f_sq.simplify_full()

show(e_simple)
show(f_simple)


cos = ((i-l)*(j-k))/((i-k)*(j-l))  # cos = bd/ef = bd/(ac+bd); cos = (ef-ac)/ef = 1 - ac/ef
sin = ((i-j)*(k-l))/((i-k)*(j-l))  # sin = ac/ef = ac/(ac+bd); sin = (ef-bd)/ef = 1 - bd/ef

cos_simple = cos.simplify_full()
sin_simple = sin.simplify_full()
show(cos_simple)
show(sin_simple)
