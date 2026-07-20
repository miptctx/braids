import numpy as np
from sage.all import *

z_1, z_2, z_3, z_4, z_5 = var("z_1, z_2, z_3, z_4, z_5")
# a,b,c,d,e,x,y,v,w = var("a,b,c,d,e,x,y,v,w")


z_12 = z_2 - z_1
z_13 = z_3 - z_1
z_14 = z_4 - z_1
z_15 = z_5 - z_1
z_23 = z_3 - z_2
z_24 = z_4 - z_2
z_25 = z_5 - z_2
z_34 = z_4 - z_3
z_35 = z_5 - z_3
z_45 = z_5 - z_4


z = (z_25*z_34 + z_45*z_23)/z_35    #(x*d + c*e)/y
print("z_24?", z.simplify_full())

t = (z_15*z_24 + z_12*z_45)/z_25    #(b*z + a*c)/x
print("z_14?", t.simplify_full())

u = (z_23*z_14 + z_12*z_34)/z_24    #(e*t + a*d)/z
print("z_13?", u.simplify_full())

v = (z_13*z_45 + z_15*z_34)/z_14    #(c*u + b*d)/t
print("z_35?", v.simplify_full())

w = (z_12*z_35 + z_15*z_23)/z_13    #(a*v + e*b)/u
print("z_25?", w.simplify_full())

show(w)

result = w.simplify_full()

print('Is relation satisfied:', result == z_25)

exit()

x_v, y_v, c_v, d_v, e_v, z_v, t_v, u_v, v_v, w_v = tuple([randint(-100, 100) for _ in range(10)])

print("Rand numbers:", x_v, y_v, c_v, d_v, e_v, z_v, t_v, u_v, v_v, w_v)
print("x =", x_v)

result = w.subs(x=x_v, y=y_v, c=c_v, d=d_v, e=e_v, z=z_v, t=t_v, u=u_v, v=v_v)

print("Rand numbers result:", result)

