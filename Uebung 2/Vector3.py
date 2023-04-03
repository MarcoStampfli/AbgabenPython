import math
class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        #Diese Methode gibt den Vektor als String aus. wird mit z.B. print(v1) aufgerufen!!!
        return "({}, {}, {})".format(self.x, self.y, self.z)
       
    def __add__(self, other):
        #Diese Methode addiert zwei Vektoren.
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        #Diese Methode subtrahiert zwei Vektoren.
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        #Diese Methode multipliziert zwei Vektoren oder ein Vektor mit Skalar (Lamda).
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vector3(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def cross(self, other):
        #Die Methode cross(b) berechnet das Kreuzprodukt zwischen dem Vektor und einem anderen Vektor.
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3(x, y, z)
    
    def dot(self, other):
        #Die Methode dot(b) berechnet das Skalarprodukt zwischen den beiden Vektoren (Ergebnis = 0 == Vektoren rechtwinklig zueinander!!!).
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def length(self):
        #Die Methode length() gibt die Länge des Vektors zurück.
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self):
        #Die Methode normalize() gibt den normalisierten Vektor zurück.
        length = self.length()
        if length == 0:
            return Vector3(0, 0, 0)
        x = self.x / length
        y = self.y / length
        z = self.z / length
        return Vector3(x, y, z)
    
def vectortype(self):
    if type(self) == Vector3:
        return(f"{self} ist eine Vektor3-Klasse")
    if type(self) == float:
        return(f"{self} ist ein float")
    if type(self) == int:
        return(f"{self} ist ein Integer")
    
v1 = Vector3(1, 2, 8)
v2 = Vector3(0, 4, 0)

print(v1)
print(v2)

print(2.5 * v1)
print(v1 * 2.5)
print(3 * v1)
print(v1 * 3)

print(v1.dot(v2))
print(v1.normalize())
print(v1.length())

print(v1 - v2)
print(v1 + v2)
print(v1 * v2)
print(2 * v1)
vectortype(v1)
vectortype(v1.dot(v2))