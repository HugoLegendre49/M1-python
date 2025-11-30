import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

document = pd.read_csv('BTT_TD_POP1A_2018.CSV', sep=';')

#exercice 1 :

def benford (d):
    return np.log10(1+1/d)

def firstdigit1(n, debug=True):
    if n < 1:
        return 'error'
    return int(str(n)[0])

def firstdigit2(n, debug=True):
    if n >= 1:
        return int(n/10**(int(np.log10(n))))
    return 'error'
r = np.random.randint(1,10**3)
print ('firstdigit1(',r,') =',firstdigit1(r, debug=True), 'firstdigit2(',r,') =',firstdigit2(r, debug=True))
def test_firstdigit(debug=False):
    n=100
    r = 0
    for i in range(1,n):
        p = np.random.randint(1,10**3)
        if firstdigit1(p, debug=False) == firstdigit2(p, debug=False):
            r += 1
        if debug:
            print("i=",i,"p=",p,"firstdigit1=",firstdigit1(p, debug=False),"firstdigit2=",firstdigit2(p, debug=False), 'r=',r)
    if r == n-1:
        print("Test of firstdigit: OK")
    else:
        print("Test of firstdigit: PROBLEM")

test_firstdigit(debug=False)

def temps():
    t = time.time()
    firstdigit1(r, debug=False)
    t1 = time.time() - t
    t = time.time()
    firstdigit2(r, debug=False)
    t2 = time.time() - t
    print("Time of firstdigit1:",t1)
    print("Time of firstdigit2:",t2)
temps()

def occureences(list):
    occurences = [0,0,0,0,0,0,0,0,0]
    for i in range(len(list)):
        a= firstdigit1(list[i], debug=False)
        if a in range(1,10):
            occurences[a-1] += 1
    return occurences
liste = []
for n in range(100):
    liste.append(2**n)
print('occurences =', occureences(liste))
names = [1,2,3,4,5,6,7,8,9]
values = occureences(liste)

def théorique(liste):
    h = []
    for i in range(9):
        h.append(benford(i+1)*len(liste)) 
    return h

plt.bar(names, values)
plt.plot(names, théorique(liste), label="nombre d'occurence de chaque chiffre", color='red', marker='o')
plt.legend()
plt.show()

NB = occureences(document['NB'])
print('occurences in document =', NB)
plt.bar(names, NB)
plt.plot(names, théorique(document['NB']), label="nombre d'occurence de chaque chiffre", color='red', marker='o')
plt.legend()
plt.show()

# exercice 2 :

def random_sign():
    if np.random.rand()<0.5:
        return -1
    return 1

def simulate_W(n):
    W = [0]
    for i in range(1, n+1):
        W.append(W[i-1]+ random_sign()/i)
    return W

n = 1000
W = simulate_W(n)
plt.plot(range(n+1), W)
plt.title("Simulation de W")
plt.show()

# exercice 3 :

def X(p):
    if np.random.rand()<p:
        return 1
    return -1

def simulate(p,k,N, debug=True):
    if k < 1 :
        return k
    S = [k]
    for i in range(1,N+1):
        S.append(S[i-1]+X(p))
        if debug:
            print("i=",i,"S=",S[i], 'X(p)=',S[i]-S[i-1])
        if S[i] == 0:
            return 0
    return S
print(simulate(0.5,10,100))