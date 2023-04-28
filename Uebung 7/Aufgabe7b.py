import numpy as np
import matplotlib.pyplot as plt


#Definiere Funktion

def f(x,y):
    return np.exp(-x**2) * np.sin(y)

g = 5 #Bereich der min/max x y Werte
pixel = 100
x = np.linspace(-g, g, pixel) #Array mit x-Werte
y = np.linspace(-g, g, pixel) #Array mit y-Werte
X,Y = np.meshgrid(x,y) #Flächenraster mit x y Werte

#Funktion aufrufen
Z = f(X,Y)

# Plotten der Punkte mit den zufälligen Farben
#plt.scatter(X,Y,Z, c=colors)

# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Funktion f(x,y) = exp(-x^2) * sin(y)')

# Anzeigen des Plots
plt.pcolormesh(X, Y, Z)
plt.show()