import numpy as np
import matplotlib.pyplot as plt

# Erstelle 1000 Zufallszahlen im Bereich von [-100,-100] bis [100,100]
x = np.random.uniform(low=-100, high=100, size=1000)
y = np.random.uniform(low=-100, high=100, size=1000)

# Erstelle eine zufällige Farbe für jeden Punkt
colors = np.random.rand(1000)

# Plotten der Punkte mit den zufälligen Farben
plt.scatter(x, y, c=colors)

# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Zufällige Punkte im Bereich von [-100,-100] bis [100,100]')

# Anzeigen des Plots
plt.show()