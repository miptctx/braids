import numpy as np
from sage.all import *

a,b,c,d,e,x,y,v,w = var("a,b,c,d,e,x,y,v,w")


z = (x*d + c*e)/y
t = (b*z + a*c)/x
u = (e*t + a*d)/z
v = (c*u + b*d)/t
w = (a*v + e*b)/u

result = w.simplify_full()

show(result)

x_v, y_v, c_v, d_v, e_v, z_v, t_v, u_v, v_v, w_v = tuple([randint(-100, 100) for _ in range(10)])

print("Rand numbers:", x_v, y_v, c_v, d_v, e_v, z_v, t_v, u_v, v_v, w_v)
print("x =", x_v)

result = w.subs(x=x_v, y=y_v, c=c_v, d=d_v, e=e_v, z=z_v, t=t_v, u=u_v, v=v_v)

print("Rand numbers result:", result)

