import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def g(x,y):
    return 1-3*x**2+2*y+0.1*(x**4+y**6) +2*x*y

def plot_2d_function(f):
    # Define the grid
    x0, y0 = 7, 3
    resolution = 200
    x = np.linspace(-x0, x0, resolution)
    y = np.linspace(-y0, y0, resolution)
    X, Y = np.meshgrid(x, y)
    Z = f(X,Y)
    # Plot
    plt.figure(figsize=(6, 5))
    # Colormesh
    mesh = plt.pcolormesh(X, Y, Z, shading='auto', cmap='viridis')
    plt.colorbar(mesh, label='f(x,y)')  # add colorbar
    # Contours
    contours = plt.contour(X, Y, Z, levels=50, colors='black', linewidths=0.8)
    plt.clabel(contours, inline=True, fontsize=8)  # label contour lines
    # Labels
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of f')
    plt.show()

def exercise():
    print("Question 1b, affichage de g")
    plot_2d_function(g)
    print("Question 1c, il semble qu'il y ait un minimiseur global, approximativement et [4,-1.75]")
    x0 = [0,0]
    print("Question 1e, lancement de 'minimize'")
    def gg(X):
        return g(X[0],X[1])
    R = sp.optimize.minimize(gg, x0)
    print("R")
    print("Minimiseur :",R.x, "; min de g :",R.fun)

exercise()
