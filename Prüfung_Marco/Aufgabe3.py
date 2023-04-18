class Stadt:
    def __init__(self,name,einw,land,kontinent,koordinate):
        self.name = name
        self.einww = einw
        self.land = land
        self.kontinent = kontinent
        self.koordinate = koordinate

    def __str__(self) -> str:
        return f"{self.name}{self.einww}{self.land}{self.kontinent}{self.koordinate}"
        