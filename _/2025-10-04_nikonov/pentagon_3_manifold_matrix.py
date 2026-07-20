from sage.all import *

F = SR


a,b,c = var("a,b,c")

z_12 = matrix(F, [
  [(a+1/2)/a, 0              ,               0],
  [0        , (b+sqrt(3)/6)/b,               0],
  [0        , 0              , (c-sqrt(6)/3)/c]
])


z_13 = matrix(F, [
  [1+1/(2*a), 0              , 0],
  [0        , 1+sqrt(3)/(2*b), 0],
  [0        , 0              , 1]
])


z_14 = matrix(F, [
  [1+1/a, 0, 0],
  [0    , 1, 0],
  [0    , 0, 1]
])

z_15 = matrix(F, [
  [1+1/(2*a), 0              ,               0],
  [0        , 1+sqrt(3)/(6*b),               0],
  [0        , 0              , 1+sqrt(6)/(3*c)]
])

z_15 = matrix(F, [
  [1+1/(2*a), 0              ,               0],
  [0        , 1+sqrt(3)/(6*b),               0],
  [0        , 0              , 1+sqrt(6)/(3*c)]
])

z_23 = matrix(F, [
  [1, 0,                                         0],
  [0, (b+sqrt(3)/2)/(b+sqrt(3)/6),               0],
  [0, 0                          , c/(c-sqrt(6)/3)]
])

z_24 = matrix(F, [
  [(a+1)/(a+1/2),               0,               0],
  [0            , b/(b+sqrt(3)/6),               0],
  [0            , 0              , c/(c-sqrt(6)/3)]
])

z_25 = matrix(F, [
  [1, 0,                           0],
  [0, 1,                           0],
  [0, 0, (c+sqrt(6)/3)/(c-sqrt(6)/3)]
])

z_34 = matrix(F, [
  [(a+1)/(a+1/2),               0, 0],
  [0            , b/(b+sqrt(3)/2), 0],
  [0            , 0              , 1]
])

z_35 = matrix(F, [
  [1, 0,                                         0],
  [0, (b+sqrt(3)/6)/(b+sqrt(3)/2),               0],
  [0, 0                          , (c+sqrt(6)/3)/c]
])

z_45 = matrix(F, [
  [(a+1/2)/(a+1),               0,               0],
  [0            , (b+sqrt(3)/6)/b,               0],
  [0            , 0              , (c+sqrt(6)/3)/c]
])


z    = (z_25*z_34 + z_23*z_45)*z_35.inverse()    #(x*d + c*e)/y
zz_2 = (z_34*z_25 + z_23*z_45)*z_35.inverse()    #(x*d + c*e)/y
zz_3 = (z_25*z_34 + z_45*z_23)*z_35.inverse()    #(x*d + c*e)/y
zz_4 = (z_34*z_25 + z_45*z_23)*z_35.inverse()    #(x*d + c*e)/y
assert(z == zz_2)
assert(z == zz_3)
assert(z == zz_4)
print("### z_24 ###")
show(z_24.simplify_full())
print("---  z  ---")
show(z.simplify_full())

# t = (z_15*z_24 + z_12*z_45)*z_25.inverse()    #(b*z + a*c)/x
t = (z_15*z + z_12*z_45)*z_25.inverse()    #(b*z + a*c)/x
#  print("z_14?", z_14, "t=", t)

# u = (z_14*z_23 + z_12*z_34)*z_24.inverse()    #(e*t + a*d)/z
u = (z_14*t + z_12*z_34)*z.inverse()    #(e*t + a*d)/z
# print("z_13?", z_13, "u=", u)

# v = (z_13*z_45 + z_15*z_34)*z_14.inverse()    #(c*u + b*d)/t
v = (z_13*u + z_15*z_34)*t.inverse()    #(c*u + b*d)/t
# print("z_35?", z_35, "v=", v)


# w = (z_12*z_35 + z_15*z_23)*z_13.inverse()    #(a*v + e*b)/u
w = (z_12*v + z_15*z_23)*u.inverse()    #(a*v + e*b)/u
# print("### z_25 ###")
# show(z_25)
# print("---  w  ---")
# show(w)

result = w.simplify_full()

print("#######")
show(result)

print('Is relation satisfied:', result == z_25)

print("##### z_25 subs #####")
print(z_25.subs({a: 1, b: 2, c: 3}))

print("##### result subs #####")
print(result.subs({a: 1, b: 2, c: 3}))
