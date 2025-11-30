import numpy as np
import random
import matplotlib.pyplot as plt

# definition des lois de probabilites (1.1.a):

def poisson(k,la):
    return ((la**k * np.exp(-la)) / np.math.factorial(k))

def normal_density(x, mu, var):
    return ((1 / np.sqrt(2 * np.pi * var))*np.exp(-((x-mu)**2)/(2*var)))

def cauchy_density(x, a, gamma):
    return (1/(np.pi*gamma*(1+((x-a)/gamma)**2)))

# calcul de variance et esperance (1.2):

def mean_and_deviation(xs):
    N=len(xs)
    mean = sum(xs)/N
    ys = np.zeros(N)
    for i in range(N):
        ys[i]=(xs[i]-mean)**2
    deviation = np.sqrt(sum(ys)/N)
    return mean, deviation

#donnée pour tester la fonction mean and deviation :

la = random.uniform(0,100)
mu = random.uniform(0,100)
var = random.uniform(0,100)
k = []
nor = []
cau = []
for i in range(200):
    a = random.randint(1,100)
    b = random.uniform(1,100)
    k.append(poisson(a, la))
    nor.append(normal_density(b,mu,var))
    cau.append(cauchy_density(b, mu, var))

def test(xs, debug=False):
    epsilon = 0.000001
    a = mean_and_deviation(xs)[1]
    b = np.std(xs)
    if debug:
        print ("fonction =",a," réels =",b, "difference = ", abs(a-b))
    if abs(a-b) <= epsilon :
        return "fonction ok"
    return "fonction pas ok"

print("poisson :",test(k), "normal :", test(nor), "cauchy :", test(cau))

# fonction qui renvoie la densité et la distribution de la loi normale (1.3):

def normal_density_on_array(xs, mu, var):
    N=len(xs)
    density=np.zeros(N)
    for i in range(N):
        density[i]=normal_density(xs[i],mu,var)
    return density

# génération de 10 valeur aléatoire de poisson (1.4):

print (np.random. poisson(2,10))

# création de fonction de répétition de poisson (1.5):

def samples_poisson(la, N, M):
    total = []
    numpy = []
    long = []
    for i in range(N):
        total.append(np.random.poisson(la,M))
        numpy.append(mean_and_deviation(total[i])[0])
        for a in range(M):
            long.append(total[i][a])
    var_exp_tota = mean_and_deviation(long)

    return N*M, total, numpy, var_exp_tota

print (samples_poisson(2,10000,10)[2])
# faire un chemas des N experiance precedant (1.6):

def histogrammes(X):
    N =len(X)
    x = range(N)
    y = X
    plt.hist(y)
    plt.show()

histogrammes(samples_poisson(2,10000,10)[2])