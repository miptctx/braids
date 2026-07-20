from sage.all import *

def sedr2(a, b, c, d):
    try:
        qe = (a * c + b * d) * (a * d + b * c) / (a * b + d * c)
        qf = (a * c + b * d) * (a * b + d * c) / (a * d + b * c)
        # print(f'{qe} - квадрат e, {qf} - квадрат f')
        return qe**0.5, qf**0.5
    except ZeroDivisionError:
        print("Деление на ноль в sedr2()")
        return None, None


def ptol(a, b, c, d, x):
    try:
        y = (a * c + b * d) / x
        return y
    except ZeroDivisionError:
        print("Деление на ноль в ptol()")
        return None


# Исходные значения
#a, b, c, d, e = 1, 1, 1, 1, 1
#x, y = 1.618033988749895, 1.618033988749895

#a, b, c, d, e, x, y = 1,2,3,4,5,6,7

# a, b, c, d, e, x, y = 1, 1, 1, 1, 4, 3, 2

z_1, z_2, z_3, z_4, z_5 = 1,2,3,4,5

a = z_2 - z_1
b = z_3 - z_2
c = z_4 - z_3
d = z_5 - z_4
e = z_1 - z_5 # ??????????????
x = z_5 - z_2
y = z_4 - z_2


'''
# Последовательность вычислений Sedr2
ys, zs = sedr2(b, c, d, x)
xs, fs = sedr2(a, b, zs, e)
zs, vs = sedr2(fs, c, d, e)
f_2, y_2 = sedr2(a, b, c, vs)
v_2, x_2 = sedr2(a, y_2, d, e)

# Последовательность вычислений Ptol
zp = ptol(b, c, d, x, y)
fp = ptol(a, b, zp, e, x)
vp = ptol(c, d, e, fp, zp)
y_3 = ptol(a,b,c,vp,fp)
x_3 = ptol(a, y, d, e, vp)

print("\n--- РЕЗУЛЬТАТЫ ---")
print(f'Седракян2: x = {x}, x_2 = {x_2}, y = {y}, y_2 = {y_2}, ys = {ys}, vs = {vs}, v_2 = {v_2}, f_2 = {f_2}, fs = {fs}')
print(f'Птолемей: x = {x}, x_3 = {x_3}, y={y}, y_3 = {y_3}')

'''

'''
#d1, d2 = sedr2(1, 2, 1, 2)
#print("d1:", d1, ", d2:", d2)

ys, zs = sedr2(b, c, d, x)
xs, fs = sedr2(a, b, zs, e)
zs, vs = sedr2(fs, c, d, e)
f_2, y_2 = sedr2(a, b, c, vs)
v_2, x_2 = sedr2(a, y_2, d, e)
'''

'''
a, b, c, d, e, x, y = 1,2,3,4,5,6,7

_z, _ = sedr2(b, c, d, x)
_, _f = sedr2(a, b, _z, e)
_, _v = sedr2(_f, c, d, e)
_y, _ = sedr2(a, b, c, _v)
_x, _ = sedr2(a, _y, d, e)


print(x == _x)
print("x:", x, ", _x:", _x)

print(y == _y)
print("y:", y, ", _y:", _y)
'''

a, b, c, d, e, x, y = 1,2,3,4,5,6,7

# Последовательность вычислений Sedr2
ys, zs = sedr2(b, c, d, x)
xs, fs = sedr2(e, a, b, zs)
zs, vs = sedr2(c, d, e, fs)
f_2, y_2 = sedr2(a, b, c, vs)
v_2, x_2 = sedr2(a, ys, d, e)


print("\n--- РЕЗУЛЬТАТЫ ---")
print(f'Седракян2: x = {x}, x_2 = {x_2}, y = {y}, y_2 = {y_2}, ys = {ys}, vs = {vs}, v_2 = {v_2}, f_2 = {f_2}, fs = {fs}')


a, b, c, d, e, x, y = 1,2,3,4,5,6,7

_z, _ = sedr2(b, c, d, x)
_, _f = sedr2(e, a, b, _z)
_, _v = sedr2(c, d, e, _f)
_y, _ = sedr2(a, b, c, _v)
_x, _ = sedr2(a, _y, d, e)


print(x == _x)
print("x:", x, ", _x:", _x)

print(y == _y)
print("y:", y, ", _y:", _y)


print("########################################")
print("### Invariants and pictures pentagon ###")
print("########################################")

a, b, c, d, e, x = var("a, b, c, d, e, x")

assume(a > 0)
assume(a == b)
assume(b == c)
assume(c == d)
assume(d == e)
assume(x > e)

_z, _y = sedr2(c, d, e, x)
_x, _t = sedr2(a, b, c, _z)
_u, __z = sedr2(a, _t, d, e)

print(__z)
print("")
print(__z.simplify_full())
quit()

__t, __y = sedr2(b, c, d, _u)
__x, __u = sedr2(a, b, __y, e)

print(__x.simplify_full())
print("")
print(__y.simplify_full())

#print(x == _x)
#print("x:", x, ", _x:", _x)

#print(y == _y)
#print("y:", y, ", _y:", _y)

