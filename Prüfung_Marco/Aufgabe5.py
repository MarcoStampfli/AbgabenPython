class Dachform:
    def __init__(self, name):
        self.name = name
        
    
    def __str__(self):
        return self.name

class Flachdach(Dachform):
    def __init__(self, name):
        super().__init__("Flachdach")

class Schraegdach(Dachform):
    def __init__(self,name):
        super().__init__("Schraegdach")

class Satteldach(Dachform):
    def __init__(self,name):
        super().__init__("Schraegdach")

dach1 = Schraegdach()
dach2 = Satteldach()
dach3 = Flachdach()

Dachform(dach1)

  
