from sage.all import *


a = 0 #0         #0
b = 1 #sqrt(-1)  #0
c = 1 #-sqrt(-1) #1
d = 0 #0         #1

q = matrix([[a,b],[c,d]])
q_2 = q*q
print("q")
print(q)
print("q^2")
print(q_2)
print("")

al_1 = matrix([[a,0,b],[c,0,d],[0,1,0]])
print("al_1:")
print(al_1)
print("al_1^2")
print(al_1*al_1)
print("")

al_2 = matrix([[1,0,0],[0,a,b],[0,c,d]])
print("al_2:")
print(al_2)
print("al_2^2")
print(al_2*al_2)
print("")

ar_1 = matrix([[a,b,0],[0,0,1],[c,d,0]])
print("ar_1:")
print(ar_1)
print("ar_1^2")
print(ar_1*ar_1)
print("")

ar_2 = matrix([[1,0,0],[0,a,b],[0,c,d]])
print("ar_2:")
print(ar_2)
print("ar_2^2")
print(ar_2*ar_2)
print("")

ar_3 = matrix([[a,b,0],[b,c,0],[0,0,1]])
print("ar_3:")
print(ar_3)
print("ar_3^2")
print(ar_3*ar_3)
print("")


lhs = al_2*al_1
rhs = ar_3*ar_2*ar_1

print('lhs')
print(lhs)
print("")
print('rhs')
print(rhs)

print("")
print("lhs == rhs: ", lhs==rhs)