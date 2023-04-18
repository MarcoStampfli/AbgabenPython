import math

class Figur2D:
    def __init__(self, name):
        self.name = name
        
    def Umfang(self):
        return 0
        
    def __str__(self):
        return self.name

class Punkt(Figur2D):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def distanz(self, other):
        return math.sqrt((self.p2.x - other.p1.x) ** 2 + (self.p2.y - other.p1.y) ** 2)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

class Kreis(Figur2D):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius
        
    def Umfang(self):
        return 2 * math.pi * self.radius
    
    def flaeche(self):
        return self.radius**2 * math.pi
    
    def __str__(self):
        return "{0} M={1} r={2}".format(self.name, self.mittelpunkt, self.radius)

class Rechteck(Figur2D):
    def __init__(self, pmin, pmax):
        super().__init__("Rechteck")
        self.p1 = pmin
        self.p2 = pmax
        
    def Umfang(self):
        return 2 * abs((self.p2.x - self.p1.x) + 2 * abs(self.p2.y - self.p1.y))
    
    def __str__(self):
        return "{0} ({1})-({2})".format(self.name, self.p1, self.p2)

class Dreieck(Figur2D):
    def __init__(self, p1, p2, p3):
        super().__init__("Dreieck")
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    #def Umfang(self):
        #a = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        #b = math.sqrt((self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2)
        #c = math.sqrt((self.p1.x - self.p3.x) ** 2 + (self.p1.y - self.p3.y) ** 2)
        #return a + b + c
    
    def Umfang(self):
        return self.p1.distanz(self.p2) + self.p2.distanz(self.p3) + self.p3.distanz(self.p1)
    
    def __str__(self):
        return "{0} ({1}) ({2}) ({3})".format(self.name, self.p1, self.p2, self.p3)

class Polygon(Figur2D):
    def __init__(self, *koordinaten):
        super().__init__("Polygon")
        self.koordinaten = koordinaten
        
    def Umfang(self):
        Umfang = 0
        for i in range(len(self.koordinaten)):
            p1 = self.koordinaten[i]
            if i == len(self.koordinaten) - 1:
                p2 = self.koordinaten[0]
            else:
                p2 = self.koordinaten[i+1]
            Umfang += math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
        return Umfang



p1 = Punkt(1,1)
p2 = Punkt(4,4)
um = Rechteck(p1, p2).Umfang()
print(um)

# Erstellen von Objekten der verschiedenen Figuren

#p1 = Punkt(1,1)
#p2 = Punkt(4,4)

#r = 2
#M = (1, 2)
#k = Kreis(M, r)
#k = Kreis(Punkt(0,0), 1.2732)
#r = Rechteck(Punkt(0, 0), Punkt(3, 4))
#d = Dreieck(Punkt(0, 0), Punkt(3, 0), Punkt(0, 4))
#po = Polygon(Punkt(0, 0), Punkt(3, 0), Punkt(3, 4), Punkt(0, 4))

#print(d.Umfang())


# Ausgabe der Umfänge der verschiedenen Figuren
#print("{0}: Umfang={1}".format(k, k.Umfang()))
#print("{0}: Umfang={1}".format(r, r.Umfang()))
#print("{0}: Umfang={1}".format(d, d.Umfang()))
#print("{0}: Umfang={1}".format(po, po.Umfang()))
