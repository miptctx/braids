from sage.all import *

F = RR

z_1 = vector(F, [0, 0, 0])
z_2 = vector(F, [1/2, sqrt(3)/6, -sqrt(6)/3])
z_3 = vector(F, [1/2, sqrt(3)/2, 0])
z_4 = vector(F, [1, 0, 0])
z_5 = vector(F, [1/2, sqrt(3)/6, sqrt(6)/3])

# norms of vectors are equal to 1

z_12 = (z_2 - z_1).norm()
z_13 = (z_3 - z_1).norm()
z_14 = (z_4 - z_1).norm()
z_15 = (z_5 - z_1).norm()
z_23 = (z_3 - z_2).norm()
z_24 = (z_4 - z_2).norm()
z_25 = (z_5 - z_2).norm()
z_34 = (z_4 - z_3).norm()
z_35 = (z_5 - z_3).norm()
z_45 = (z_5 - z_4).norm()

z = (z_25*z_34 + z_45*z_23)/z_35    #(x*d + c*e)/y
print("z_24", z_24, "z=", z)

t = (z_15*z_24 + z_12*z_45)/z_25    #(b*z + a*c)/x
print("z_14?", z_14, "t=", t)

u = (z_23*z_14 + z_12*z_34)/z_24    #(e*t + a*d)/z
print("z_13?", z_13, "u=", u)

v = (z_13*z_45 + z_15*z_34)/z_14    #(c*u + b*d)/t
print("z_35?", z_35, "v=", v)

w = (z_12*z_35 + z_15*z_23)/z_13    #(a*v + e*b)/u
print("z_25?", z_25, "w=", w)

result = w

print('Is relation satisfied:', result == z_25)
