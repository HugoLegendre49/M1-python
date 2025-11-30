import math
import random
import numpy as np
import matplotlib.pyplot
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
#exercice 1 question a)
L1 = []
L1 += [1,2,3]
L2 = [4,5,6,7]
L = []
L = L+L1+L2
L.insert(3-1,8)
n = len(L)
print(L1)
print(L2)
print(L)
print(L[4-1])
print(L[n-2])
print('la longueur est :', n, 'et la type est une liste d`entier')

#question b)
L3 = L[1-1:5]
del L3[3-1]
L3.remove(1)
print(L3)
M =[L1,L2,L3]
m = len(M)
print(M)
print(M[2-1][3-1])
M = M+M[0]+M[m-1]
print(M)
m = len(M)
print('la longeur est de',m,'et la nature est une liste de liste d`entier')

#exercice 2 question a
def f (x):  
    return (3*np.exp(x))/ (x**2 +1)
print(f(0))
def g(x):
    if x >= -np.pi and x <= np.pi:
        k = (np.cos(x)/(1+np.sin(x)**2)) 
        l = ((np.cos(x)*np.sin(x))/(1+np.sin(x)**2))
        return k,l
    else:
        return ('#valeur non autorisée')
print(g(0))
print(g(np.pi))
print(g(5))
print(type(g(0)[0]))

#question b 
x = np.linspace(-5, 5, 30)
y = f(x)
plt.plot(x,y)
plt.show()
N = 100
n = np.linspace(-np.pi, np.pi, N)

#pour chaque valeur de n on calcule g(n) et on affiche le resultat

def trace(x):
    y1 = []
    y2 = []
    for i in range(len(x)):
        y1.append(g(x[i])[0])
        y2.append(g(x[i])[1])
    return y1, y2
a,b = trace(n)

plt.plot(a,b)
plt.show()

#exercice 2 question 2 III
plt.plot(n,np.cos(n))
plt.plot(n,np.cos(2*n))
plt.plot(n,np.cos(3*n))

plt.show()

#exercice 3 question a
def fact(n):
    if n == 0:
        return 1
    else:
        for i in range(1,n):
            n = n*i
        return n
print(fact(5))

def test_fact():
    for i in range(0,10):
        a = random.randint(0,100)
        assert fact(a)-math.factorial(a) == 0, "la fonction ne marche pas"
    print("la fonction marche")
test_fact()

#exercice 4 question a
def compute_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        c = [0]
        for i in range(2, n + 1):
            c.append(b)
            a, b = b, a + b
        return c
c = compute_fibonacci(5)
print(c)

#exercice 4 question b
def compute_ratio():
    ratios = []
    r = random.randint(0,100)
    fib = compute_fibonacci(r)
    for i in range(2, len(fib)):
        ratios.append((fib[i] / fib[i - 1]))
    return r, ratios
r, ratios = compute_ratio()
x = []
y = []
for i in range(0, r-2):
    x.append(i)
    y.append((1+np.sqrt(5))/2)
plt.plot(x, ratios)
plt.plot(x, y)
plt.title("Suite des ratios")
plt.show()

"#exercice 4 question c"
def u(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b+np.exp(-n)
        return b
def def_alpha():
    alphas = []
    r = 100
    for i in range(2, r + 1):
        alphas.append((u(i) / u(i-1)))
    return r, alphas
r, alphas = def_alpha()
x = []
for i in range(0, r-1):
    x.append(i)
plt.plot(x, alphas)
plt.title("Suite alpha")
plt.show()
print(alphas[r-2])

ro = []
U = []
for i in range(0, r-1):
    U.append(u(i))
for i in range(0, r-1):
    ro.append(U[i]/alphas[r-2]**(r-2))
plt.plot(x, ro)
plt.title("Suite ro")
plt.show()
print(ro)

E = []
for i in range(0, r-1):
    E.append(abs((U[i]/ro[r-2]*alphas[r-2]**(r-2))-1))
plt.plot(x, E)
plt.title("Suite E")
plt.show()
