import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.integrate import quad


def aproxima_ln1(x, n, debug=False, verbose=False):
    resulta = 0
    if x > -1:
        for i in range(1, n):
            valeur = (((-1)**(i+1)) * ((x**i) / i))
            resulta += valeur
            if debug:
                print("i=",i,"resulta=",resulta,"valeur=",valeur)
        return resulta
    else:
        return "x must be greater than -1"
    if verbose:
        print("Approximation of ln(1+",x,") at order",n,":",resulta)    
print('le logaritme de ln(1+X) avec x= 5 et n=100 est :', aproxima_ln1(5, 100))

def test_approx_ln():
    n = 100
    k = 10
    x_list = random.randint(0,k)
    tolerance = 1e-3

    assert abs(aproxima_ln1(x_list, n, verbose=True, debug=False) - np.log(1+x_list)) < tolerance, "PROBLEM with test approx ln"
    print("Test of approx_ln1: OK")

#exercice 1
def trapeze(f, a, b, N, debug=True):
    resultat = 0
    l = np.linspace(a, b, N, endpoint=False)
    for i in range(1,len(l)):
        valeur = ((f(l[i])-f(l[i-1]))*((f(l[i])+f(l[i-1]))/2))
        resultat += valeur
        if debug:
            print("i=",i,"resultat=",resultat,"valeur=",valeur)
    return resultat
print('l`integrale de sinus entre 0 et 3 avec N=100 est :', trapeze(np.sin, 0, 3, 100, debug=False))

def sinf(x):
        return (np.sin(x + np.exp(x)))

def test_trapeze():
    n=10000
    aprox = trapeze(sinf, 0, 3, n, debug=False)
    reel = quad(sinf, 0, 3)[0]
    return aprox - reel
print("Test of trapeze: ",test_trapeze())

# faire question d chez soit 

# exercice 2:
def montecarlo(f, a, b, N, debug=False):
    moyenne = 0
    variance = 0
    for i in range(N):
        x = random.uniform(a, b)
        valeur = f(x)
        moyenne += valeur
        if debug:
            print("i=",i,"resultat=",moyenne,"valeur=",valeur)
    moyenne = moyenne * (b - a) / N
    for i in range(N):
        x = random.uniform(a, b)
        resultat = (f(x) - (moyenne / (b - a)))**2
        variance += resultat
    variance = variance * ((b-a)**2/N)
    return moyenne, variance
print('l integrale de sinf entre 0 et 3 avec N=10000 est :', montecarlo(sinf, 0, 3, 10000, debug=False))
def test_montecarlo(debug=True):
    n=10000
    data = []
    aprox_exp = montecarlo(sinf, 0, 3, n, debug=False)[0]
    reel = quad(sinf, 0, 3)[0]
    if debug:
        print("aprox_exp=",aprox_exp,"reel=",reel)
    return aprox_exp - reel
print("Test of montecarlo: ",test_montecarlo(True))

x = np.linspace(1, 10**5, 1000)
y = montecarlo(sinf, 0, x, 1000, debug=False)[0]
plt.plot(x, y)
plt.show()
