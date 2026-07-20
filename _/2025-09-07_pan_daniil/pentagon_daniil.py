import numpy as np
from sage.all import *

a,b,c,d,e,x,y,v,w = var("a,b,c,d,e,x,y,v,w")



def check_eq():

    x = var('x')
    a,b,c,d,e,y = 2,100,3,4,6,7
    z = (x*d + c*e)/y
    t = (b*z + a*c)/x
    u = (e*t + a*d)/z
    v = (c*u + b*d)/t
    w = (a*v + e*b)/u

    targ_val = 10

    sol = solve(w - targ_val, x)
    print(sol)




def flips_np(n_samples=10):
    results = []
    for _ in range(n_samples):
        # генерируем случайные числа для a,b,c,d,e,y,x
        a, b, c, d, e, y, x = np.random.rand(7)*10 + 0.1  # избегаем деления на 0

        # цепочка флипов
        z = (x*d + c*e)/y
        t = (b*z + a*c)/x
        u = (e*t + a*d)/z
        v = (c*u + b*d)/u
        w = (a*y + e*b)/u

        results.append((a,b,c,d,e,y,x,w))

    return results


#check_eq()


# Пример использования
samples = flips_np(n_samples=5)

for s in samples:
    print("a,b,c,d,e,y,x -> w:", s)